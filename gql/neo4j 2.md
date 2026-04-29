## Cypher a Graph Query Language (GQL) in Neo4j
Cypher is a declarative language, meaning the database is responsible for finding the most optimal way of executing that query.

Cypher allows you to identify **patterns** in your data using an **ASCII-art style syntax** consisting of **brackets**, **dashes** and **arrows**.
### Cypher syntax basics
- Nodes in the pattern are expressed with parentheses - `( )`
- Labels are prefixed a colon - `(:Label)`
- Relationships are drawn with two dashes (`--`) and an arrow to specify the direction (`<` or `>`) - `- →`.
- Relationship information is contained within square brackets -`[ ]`.
- The relationship type is prefixed with a colon - `[:TYPE]`
- The pattern contains one relationship `-[:ACTED_IN]→` between `(:Person)` and `(:Movie)` nodes.
- The nodes and relationships in the pattern are assigned to variables. These variables are positioned before the information about the node or relationship.
- The keyword `AS` is used to define an alias.
``` c
(p:Person)-[r:ACTED_IN]->(m:Movie)
```
### Neo4j basic operations
- View the node properties by selecting the node.
- Expand the node’s relationships by doubling click the node.
### Movie database dataset examples
Find a `Person` node with the `name` attribute 'Tom Hanks':
``` cypher
MATCH (n:Person)
WHERE n.name = 'Actor Name'
RETURN n
```
Find the movie 'Toy Story' and the people who acted in the movie:
``` cypher
MATCH (m:Movie)<-[r:ACTED_IN]-(p:Person)
WHERE m.title = 'Movie Title'
RETURN m, r, p
```
Find all the movies that have been rated by the user "Mr. Jason Love". The **rating** the user has given for the movie is stored as a property on the `RATED` relationship:
``` cypher
MATCH (u:User)-[r:RATED]->(m:Movie)
WHERE u.name = "Mr. Jason Love"
RETURN u, r, m
```
Show a table of movie ratings:
``` cypher
MATCH (u:User)-[r:RATED]->(m:Movie)
WHERE u.name = "User Name"
RETURN u.name, r.rating, m.title
```
### Search database with MATCH clause in Cypher
The `MATCH` clause is used to find patterns in the data. Patterns can be as simple as a single node, or contain multiple relationships.
``` cypher
MATCH (p:Person)-[r:ACTED_IN]->(m:Movie)
WHERE p.name = 'Actor Name'
RETURN p,r,m
```
Find all people who have acted in movies with 'Tom Hanks', and uses the `RETURN` clause to define the properties. The pattern uses the ACTED_IN relationship to find the movies Tom Hanks is in, and then a second time to find the actors in the movies with Tom Hanks:
``` cypher
MATCH (p:Person)-[:ACTED_IN]->(m:Movie)<-[r:ACTED_IN]-(p2:Person)
WHERE p.name = 'Actor Name'
RETURN p2.name AS actor, m.title AS movie, r.role AS role
```
### Expand database with Merge clause in Cypher
Use `MERGE` to create a new `Movie` node:
``` cypher
MERGE (m:Movie {title: "Movie Title"})
SET m.year = 2024
RETURN m
```
Run this Cypher statement, that creates `Movie` and `User` nodes and a `RATED` relationship between them. Modify this query to add your favorite movie and a user rating:
``` cypher
MERGE (m:Movie {title: "Movie Title"})
MERGE (u:User {name: "New User"})
MERGE (u)-[r:RATED {rating: 5}]->(m)
RETURN u, r, m
```

**Author:**
Zbigniew Galar
