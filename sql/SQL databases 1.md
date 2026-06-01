### Why we use databases
##### Databases terminology
- **concurrency**: the ability of the database to allow multiple users access to the same record without adversely affecting transaction processing
- **concurrency control strategies**: features of a database that allow several users access to the same data item at the same time
- **data element**: a single fact or piece of information
- **data inconsistency**: a situation where various copies of the same data are conflicting
- **data isolation**: a property that determines when and how changes made by one operation become visible to other concurrent users and systems
- **data integrity**: refers to the maintenance and assurance that the data in a database are correct and consistent
- **data redundancy**: a situation that occurs in a database when a field needs to be updated in more than one table
- **database**: a shared collection of related data used to support the activities of a particular organization
- **database approach**: allows the management of large amounts of organizational information
- **database management software**: a powerful software tool that allows you to store, manipulate and retrieve data in a variety of ways
- **database management system (DBMS)**:  a collection of programs that enables users to create and maintain databases and control all access to them
- **database constraint**: a restriction that determines what is allowed to be entered or edited in a table
- **data elements**: facts that represent real-world information
- **data type**: determines the sort of data permitted in a field, for example numbers only
- **data uniqueness**: ensures that no duplicates are entered
- **file-based system**: an application program designed to manipulate data files
- **metadata**: defines and describes the data and relationships between tables in the database
- **read and write privileges:** the ability to both read and modify a file
- **read-only** **access:** the ability to read a file but not make changes
- **schema:** describes all the data items and relationships in the entire database.
- **self-describing**: a database system is referred to as self-describing because it not only contains the database itself, but also metadata which defines and describes the data and relationships between tables in the database
- **table**: a combination of fields
- **view**: a subset of the database
##### About data
- Data is a collection of symbols representing numbers, text, pictures, videos, audio, and so on.
- How this data is represented gives the meaning (or semantics) to their symbols.
- Additional semantics are provided by the relationships that data has with other data.
##### Database definition
A _database_ is a shared collection of related data used to support the activities of a particular organization. A database can be viewed as a repository of data that is defined once and then accessed by various users.
##### Database properties
- It is a representation of some aspect of the real world or a collection of _data element_s (facts) representing real-world information.
- A database is logical, coherent and internally consistent.
- A database is designed, built and populated with data for a specific purpose.
- Each data item is stored in a field.
- A combination of fields makes up a _table_. For example, each field in an employee table contains data about an individual employee.
##### Databases vs programming
- In programming, the semantics of data are provided by program documentation and the programming language.
- In databases, the semantics of the data is provided by a data model, which includes the representation of the data, relationships among the data, and metadata (data that defines other data).
##### About information
- Semantics makes data useful.
- We define useful data as information.
- All information is data, but not all data is information.
- The type and amount of semantics determines the usefulness of some given data.
- Usefulness is relative to a given user.
##### Advantages of databases vs file-based approach
- Limited data redundancy
- Limited data isolation (a property that determines when and how changes made by one operation become visible to other concurrent users and systems)
- Limited data integrity problems via assigning field constraints
- Better security (multiuser system with access on need to know basis)
- Insulation between program and data (In the file-based system, the structure of the data files is defined in the application programs so if a user wants to change the structure of a file, all the programs that access that file might need to be changed as well.)
- Data constraints (data types, field uniqueness requirements, field rules like postal code format)
- Data independence (the system data descriptions or data describing data (metadata) are separated from the application programs)
- Better backup and recovery
![[Pasted image 20260301175739.png]]
##### Database Management System (DBMS) definition
**Database Management System (DBMS)** is a collection of programs that enables users to create and maintain databases and control all access to them. The primary goal of a DBMS is to provide an environment that is both convenient and efficient for users to retrieve and store information.
##### Management Information Systems definition
**Management Information Systems** are in the middle of the pyramid and are used primarily by middle management to control the organization. These systems derive much of their information by summarizing and abstracting data from transaction processing systems. They tend to be report oriented; standard reports are produced periodically (weekly, monthly, or annually) for use by middle managers to support tasks such as budget decisions and personnel assignments. 
##### Decision Support Systems definition
**Decision support systems** are designed to provide information for managerial decision making in cases where the decision is not clear-cut. These problems tend to occur at the apex of the organizational pyramid. Decision support systems often use mathematical and statistical techniques to manipulate and analyze data. It is difficult to anticipate information needs in a DSS environment, so these systems must be flexible and adaptable.
##### Effective vs Efficient Systems
- **Effective** systems provide correct, current information that is relevant to the decision at hand. Ahituv and Neumann (1986) refer to effectiveness as "doing the right thing".
- **Efficient** systems, on the other hand, perform a task in a cost-effective manner. A database system must provide the required information at a reasonable cost. Ahituv and Neumann call this "doing the thing right".
#### Core Architecture

|**Feature**|**PostgreSQL**|**SQLite**|**DuckDB**|
|---|---|---|---|
|**Paradigm**|Client-Server|Embedded|Embedded|
|**Storage Model**|Row-oriented|Row-oriented|Columnar|
|**Execution Engine**|Row-by-row (Iterator)|Row-by-row (Iterator)|Vectorized (Batch)|
|**Workload Optimization**|OLTP & HTAP|OLTP|OLAP|
|**Concurrency**|Full MVCC, concurrent writers|Single-writer, multi-reader|Single-writer, multi-reader|
|**Data Types**|Strict typing|Dynamic typing|Strict typing|
#### PostgreSQL
##### Pros
- **High Concurrency:** Full MVCC handles massive parallel read/write workloads without locking the entire database.
- **Ecosystem:** Over 1,000 extensions (e.g., PostGIS for spatial data, pgvector for AI embeddings).
- **Data Integrity:** Enforces strict schemas, constraints, and custom data types.
- **Scalability:** Supports multi-terabyte databases across distributed clusters.
##### Cons
- **Overhead:** Requires a dedicated server process, configuration, daemon management, and network connections.
- **Analytical Inefficiency:** Row-oriented storage reads unnecessary columns during aggregate scans, bottlenecking OLAP performance.
#### SQLite
##### Pros
- **Zero Configuration:** Runs entirely in-process as a single C library dependency. No server to configure.
- **Portability:** The entire database is a single `.db` file, making it easily transferable.
- **Point-Query Speed:** Sub-millisecond latency for single-row lookups and inserts on local hardware.
##### Cons
- **Concurrency Bottlenecks:** Write operations lock the entire database (or use WAL for single-writer/multi-reader limits).
- **Dynamic Typing:** Allows inserting text into integer columns, requiring strict application-level validation.
- **OLAP Performance:** Sequential row processing degrades exponentially on large dataset aggregations.
#### DuckDB
##### Pros
- **Analytical Speed:** Columnar storage and vectorized execution yield 10x–50x faster aggregations and joins than SQLite.
- **Direct Ingestion:** Executes queries directly against raw Parquet, CSV, and JSON files without prior loading.
- **Out-of-Core Processing:** Gracefully handles larger-than-memory datasets by spilling to disk efficiently.
##### Cons
- **Transactional Limitations:** Extremely poor performance for frequent, single-row updates and inserts.
- **Process Isolation:** A database file can only be opened in write mode by a single process at a time. Multiple read-only connections are permitted only if no write connection exists.
#### Decisive Selection Heuristics
##### Select PostgreSQL when
- You require multi-user concurrent write access.
- You are building a web application, SaaS backend, or production API.
- You need advanced extensions (geospatial routing, vector search).
##### Select SQLite when
- You are building a mobile application, desktop software, or IoT device requiring local state persistence.
- You are storing application configurations or offline data sync queues.
- The workload is strictly single-tenant with fast, frequent point reads/writes.
##### Select DuckDB when
- You are performing data science workflows, BI dashboards, or exploratory data analysis in Python/R.
- You need to run complex aggregations (OLAP) on datasets ranging from millions to billions of rows.
- You are querying static data lakes composed of Parquet or CSV files.

**Author:**
Zbigniew Galar
