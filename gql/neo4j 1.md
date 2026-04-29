## Neo4j basics
#### Software download page
https://neo4j.com/deployment-center/
**Choose:** Neo4j Desktop - Download.
### Neo4j installation on Windows
Neo4j Desktop is the standard deployment model for management and analytics students. It bundles the graph database engine, a management UI, and visualization tools without requiring command-line configuration.
#### Prerequisites
- **Operating System:** Windows 10 or 11 (64-bit).
- **Memory:** 8GB RAM minimum.
- **Storage:** 2GB free disk space.
- **Processor:** Intel Core i5 or AMD Ryzen 5 equivalent.
**Installation instructions:**
1. Create Instance:
    With new name for an Instance of a database.
2. Set up a user name (neo4j on default).
3. Set up a password.
4. Connect to an instance
5. Create a database
   With new name for a database project.
### Graph Thinking basics
- Connections between the data are as important as the data itself.
- Graph is a set of objects that are related to each other.
- Vertices (objects or entities) are connected by edges (relationships).
- Neo4j is storing data as a labelled property graph.
- Data in Neo4j are stored using:
	- Nodes
	- Relationships
	- Labels
	- Properties
- Nodes examples:
  - People
  - Companies
  - Locations
- Nodes are grouped and categorized using labels (node of "Michael" can have a label of a "person" and a label of an "employee") which describe what the nodes are.
- Relationships describe how nodes within the graph are connected.
- Relationships have a type and a direction (bidirectional relationship is allowed).
- Nodes can have multiple relationships to other nodes. 
- Data about nodes and relationships can be stored as properties (any number of properties).
- Properties are named key value pairs (dictionaries) for example "firstName: Michael", "lastName: Faraday", "born: 1981-03-02"
#### Why graph database?
1. **Relationships importance:** Relationships in a graph are treated with the same importance as nodes that connect them.
2. **Hierarchical data is not suitable for tables:** Dealing with hierarchical data or trees, where the answer may lie at an unknown or varying depth requires storing data not in tables as rows but as relationships in graphs. Graph databases enable efficient modeling and querying of complex relationships.
3. **Speed for making joins for large datasets:** When querying across tables, the joins are computed at read-time, using an index to find the corresponding rows in the target table. The more data added to the database, the larger the index grows, the slower the response time. In the graph database the latency grows with the number of nodes and not with the number of connections like in a traditional database.
#### Graph databases use cases
Graphs allow you to uncover patterns in your data, whether that be:
- **Customer**: using customer data for recommendations, churn prevention, tailored offers, and targeted ads, enhancing customer retention and revenue growth.
- **Network & Security**: analyzing IT asset data to support comprehensive security monitoring and proactive threat response.
- **Employee**: storing employee data to support talent development, career management, and resource allocation, helping align workforce capabilities with business needs.
- **Transactions**: capturing transactional data to detect illegal activities, supporting anti-money laundering, fraud detection, credit risk assessment, and credit fraud detection by revealing hidden patterns, anomalies, and connections.
- **Product**: centralizing product data to support personalized recommendations, optimize new product launches, enhance customization, manage inventory, and refine pricing strategies.
- **Suppliers**: storing data on supplier performance, inventory, costs, logistics, and compliance to optimize supply chain management, supporting programs like route planning, real-time visibility, inventory planning, and risk analysis.
- **Process**: creating a graph of process-related data can identify bottlenecks, improve efficiency, automate tasks, and monitor performance by analyzing operational, resource, quality, and cost data.
#### Knowledge Graphs & Generative AI
GenAI applications need access to the _meaning_ in data, and _knowledge graphs_ can provide this context. Knowledge graphs provide a structured way to represent entities, their attributes, and their relationships, allowing for a comprehensive and interconnected understanding of the information.

Knowledge graphs can break down sources of information and integrate them, allowing you to see the relationships between the data. Search engines typically use knowledge graphs to provide information about people, places, and things.

**Author:**
Zbigniew Galar
