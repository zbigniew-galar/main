## Employees satisfaction database
#### Creating Neo4j via Python loader
``` python
import pandas as pd
from neo4j import GraphDatabase
from pathlib import Path
from typing import List, Dict

class AttritionGraphLoader:
    def __init__(self, uri: str, user: str, password: str):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def run_ingestion(self, csv_path: Path, database: str = "employees"):
        """
        Executes a full purge and batch ingestion using native randomUUID().
        """
        # 1. Prepare Data
        df = pd.read_csv(csv_path, sep=";")
        df.columns = df.columns.str.strip()
        records = df.to_dict('records')

        with self.driver.session(database=database) as session:
            # 2. Cleanup & Schema Setup
            print(f"Purging existing data and setting constraints in '{database}'...")
            session.run("MATCH (n) DETACH DELETE n")
            
            # Constraints and Indexes often need to be separate from data MERGEs
            session.run("CREATE CONSTRAINT emp_id IF NOT EXISTS FOR (e:Employee) REQUIRE e.id IS UNIQUE")
            session.run("CREATE INDEX dept_name IF NOT EXISTS FOR (d:Department) ON (d.name)")

            # 3. Batch Cypher Execution
            query = """
            UNWIND $rows AS row
            MERGE (e:Employee {id: randomUUID()})
            SET e.last_evaluation = toFloat(row.last_evaluation_percent),
                e.monthly_hours = toInteger(row.average_montly_hours),
                e.tenure = toInteger(row.time_spend_company_years),
                e.left = toInteger(row.left_yes_no),
                e.had_accident = toInteger(row.Work_accident_yes_no),
                e.promoted = toInteger(row.promotion_last_5years_yes_no)
            
            MERGE (d:Department {name: row.department_name})
            MERGE (s:SalaryLevel {tier: row.salary_level})
            MERGE (p:ProjectCohort {count: toInteger(row.number_of_project)})
            
            MERGE (e)-[:BELONGS_TO]->(d)
            MERGE (e)-[:PAID_AT]->(s)
            MERGE (e)-[:LOADED_WITH]->(p)
            """
            
            print("Executing batch ingestion...")
            result = session.run(query, rows=records)
            summary = result.consume()
            
            print(f"--- Ingestion Complete ---")
            print(f"Nodes Created: {summary.counters.nodes_created}")
            print(f"Relationships Created: {summary.counters.relationships_created}")

if __name__ == "__main__":
    # Configuration
    CONFIG = {
        "uri": "neo4j://127.0.0.1:7687",
        "user": "neo4j",
        "password": "password123",
        "database": "db_name"
    }

    source_csv = Path(__file__).parent / "input_data" / "Employee satisfaction.csv"

    loader = AttritionGraphLoader(CONFIG["uri"], CONFIG["user"], CONFIG["password"])
    try:
        loader.run_ingestion(source_csv, CONFIG["database"])
    except Exception as e:
        print(f"CRITICAL ERROR: {e}")
    finally:
        loader.close()
```
**Cypher loading statement:**
``` cypher
UNWIND $rows AS row
            MERGE (e:Employee {id: randomUUID()})
            SET e.last_evaluation = toFloat(row.last_evaluation_percent),
			    e.monthly_hours = toInteger(row.average_montly_hours),
			    e.tenure = toInteger(row.time_spend_company_years),
			    e.left = toInteger(row.left_yes_no),
			    e.had_accident = toInteger(row.Work_accident_yes_no), 
			    e.promoted = toInteger(row.promotion_last_5years_yes_no) 
            
            MERGE (d:Department {name: row.department_name})
            MERGE (s:SalaryLevel {tier: row.salary_level})
            MERGE (p:ProjectCohort {count: toInteger(row.number_of_project)})
            
            MERGE (e)-[:BELONGS_TO]->(d)
            MERGE (e)-[:PAID_AT]->(s)
            MERGE (e)-[:LOADED_WITH]->(p)
```
**Script output:**
``` powershell
>>> (venv) PS C:\Python repositories\Testing Project> & "c:/Python repositories/Testing Project/venv/Scripts/python.exe" "c:/Python repositories/Testing Project/src/neo4j_load.py"
Ingestion Complete: 14999 nodes created/updated in 'employees'.
Relationships created: 44997
```
**Schema Overview:**
``` cypher
CALL db.schema.visualization()
```
**Output check:**
``` cypher
MATCH (e:Employee)-[r]->(target)
RETURN e, r, target LIMIT 50
```
#### Basic analysis
**Number of Nodes by type:**
``` cypher
MATCH (n) RETURN labels(n), count(*)
```
**Show 10 Employees belonging to sales department:**
``` cypher
MATCH (d:Department {name: 'sales'})<-[:BELONGS_TO]-(e:Employee) RETURN e LIMIT 10
```
**Number of leavers by the project count:**
``` cypher
MATCH (p:ProjectCohort)<-[:LOADED_WITH]-(e:Employee {left: 1}) RETURN p.count, count(e) AS leavers ORDER BY leavers DESC
```
#### Exploratory analysis
##### The "High-Performer" Flight Risk (The Poaching Zone)
This query identifies "Stars" (Top 20% evaluation) who are stuck in the **Low Salary** tier and haven't left yet. These are your most likely candidates for being poached by competitors.
**Why it matters:** It highlights which departments are failing to reward their top talent, creating a "talent drain" waiting to happen.
``` cypher
MATCH (s:SalaryLevel {tier: 'low'})<-[:PAID_AT]-(e:Employee {left: 0})
WHERE e.last_evaluation > 0.85
MATCH (e)-[:BELONGS_TO]->(d:Department)
RETURN d.name AS Dept, count(e) AS At_Risk_Stars
ORDER BY At_Risk_Stars DESC
```
##### The Promotion Paradox (Career Stagnation)
This explores the "5-Year Itch." It looks for employees with high tenure ($\ge 5$ years) who have **never** been promoted and calculates their current attrition rate.
**Why it matters:** If the "Left" count is significantly higher than "Stayed," your 5-year tenure mark is a "dead end" in the company’s current career pathing logic.
``` cypher
MATCH (e:Employee)
WHERE e.tenure >= 5 AND e.promoted = 0
WITH e.left AS status, count(*) AS total
RETURN 
    CASE WHEN status = 1 THEN 'Left (Stagnated)' ELSE 'Stayed (Stagnated)' END AS Status,
    total
```
##### Workload Efficiency vs. Performance
Does working more hours actually lead to better evaluations? This query buckets employees by project count to see the relationship between "Grind" and "Result."
**Why it matters:** It identifies the "Diminishing Returns" point. If scores drop or plateau while hours keep rising, your employees are likely "spinning their wheels" rather than producing quality work.
``` cypher
MATCH (p:ProjectCohort)<-[:LOADED_WITH]-(e:Employee)
RETURN 
    p.count AS Projects, 
    avg(e.monthly_hours) AS Avg_Hours, 
    avg(e.last_evaluation) AS Avg_Score
ORDER BY Projects ASC
```
##### The "Accident" Loyalty Audit
This query checks if employees who suffered a `Work_accident` are more or less likely to stay. This is a proxy for how well the company treats employees during a crisis.
**Why it matters:** A high "Left" count here suggests a toxic recovery culture or poor support systems following workplace incidents.
``` cypher
MATCH (e:Employee {had_accident: 1})
WITH e.left AS left_status, count(e) AS count
RETURN 
    CASE WHEN left_status = 1 THEN 'Left after Accident' ELSE 'Stayed after Accident' END AS Category,
    count
```
##### Departmental Overload Mapping
Which departments are "Sweatshops"? This query finds the concentration of employees working more than **250 hours/month** across different silos.
**Why it matters:** High "Overloaded_Count" combined with low "Avg_Eval" indicates a department in total collapse. High count with high evaluation indicates a high-performance/high-burnout culture like Sales or Technical.
``` cypher
MATCH (d:Department)<-[:BELONGS_TO]-(e:Employee)
WHERE e.monthly_hours > 250
RETURN d.name AS Dept, count(e) AS Overloaded_Count, avg(e.last_evaluation) AS Avg_Eval
ORDER BY Overloaded_Count DESC
```

**Author:**
Zbigniew Galar
