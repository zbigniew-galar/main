## Network infrastructure database
#### Creating an infrastructure database
``` cypher
// Clear graph
MATCH (n)
DETACH DELETE n;

// Create CRM database
CREATE (crm1:Application { 
			ip:'10.10.32.1', 
			host:'CRM-APPLICATION',
			type: 'APPLICATION',
			system: 'CRM'
		}) 

// Create ERP
CREATE (erp1:Application { 
			ip:'10.10.33.1', 
			host:'ERP-APPLICATION',
			type: 'APPLICATION',
			system: 'ERP'
		}) 

// Create Data Warehouse
CREATE (datawarehouse1:Application { 
			ip:'10.10.34.1', 
			host:'DATA-WAREHOUSE',
			type: 'DATABASE',
			system: 'DW'
		}) 

// Create Public Website 1
CREATE (Internet1:Internet { 
			ip:'10.10.35.1', 
			host:'global.acme.com',
			type: "APPLICATION",
			system: "INTERNET"
		}) 

// Create Public Website 2
CREATE (Internet2:Internet { 
			ip:'10.10.35.2', 
			host:'support.acme.com',
			type: "APPLICATION",
			system: "INTERNET"
		}) 

// Create Public Website 3
CREATE (Internet3:Internet { 
			ip:'10.10.35.3', 
			host:'shop.acme.com',
			type: "APPLICATION",
			system: "INTERNET"
		}) 

// Create Public Website 4
CREATE (Internet4:Internet { 
			ip:'10.10.35.4', 
			host:'training.acme.com',
			type: "APPLICATION",
			system: "INTERNET"
		}) 

// Create Public Website 5
CREATE (Internet5:Internet { 
			ip:'10.10.35.1', 
			host:'partners.acme.com',
			type: "APPLICATION",
			system: "INTERNET"
		}) 

// Create Internal Website 1
CREATE (Intranet1:Intranet { 
			ip:'10.10.35.2', 
			host:'events.acme.net',
			type: "APPLICATION",
			system: "INTRANET"
		}) 

// Create Internal Website 2
CREATE (Intranet2:Intranet { 
			ip:'10.10.35.3', 
			host:'intranet.acme.net',
			type: "APPLICATION",
			system: "INTRANET"
		}) 

// Create Internal Website 3
CREATE (Intranet3:Intranet { 
			ip:'10.10.35.4', 
			host:'humanresources.acme.net',
			type: "APPLICATION",
			system: "INTRANET"
		}) 

// Create Webserver VM 1
CREATE (webservervm1:VirtualMachine { 
			ip:'10.10.35.5', 
			host:'WEBSERVER-1',
			type: "WEB SERVER",
			system: "VIRTUAL MACHINE"
		}) 

// Create Webserver VM 2
CREATE (webservervm2:VirtualMachine { 
			ip:'10.10.35.6', 
			host:'WEBSERVER-2',
			type: "WEB SERVER",
			system: "VIRTUAL MACHINE"
		}) 

// Create Database VM 1
CREATE (customerdatabase1:VirtualMachine { 
			ip:'10.10.35.7', 
			host:'CUSTOMER-DB-1',
			type: "DATABASE SERVER",
			system: "VIRTUAL MACHINE"
		}) 

// Create Database VM 2
CREATE (customerdatabase2:VirtualMachine { 
			ip:'10.10.35.8', 
			host:'CUSTOMER-DB-2',
			type: "DATABASE SERVER",
			system: "VIRTUAL MACHINE"
		}) 

// Create Database VM 3
CREATE (databasevm3:VirtualMachine { 
			ip:'10.10.35.9', 
			host:'ERP-DB',
			type: "DATABASE SERVER",
			system: "VIRTUAL MACHINE"
		}) 

// Create Database VM 4
CREATE (dwdatabase:VirtualMachine { 
			ip:'10.10.35.10', 
			host:'DW-DATABASE',
			type: "DATABASE SERVER",
			system: "VIRTUAL MACHINE"
		}) 

// Create Hardware 1
CREATE (hardware1:Hardware { 
			ip:'10.10.35.11', 
			host:'HARDWARE-SERVER-1',
			type: "HARDWARE SERVER",
			system: "PHYSICAL INFRASTRUCTURE"
		}) 

// Create Hardware 2
CREATE (hardware2:Hardware { 
			ip:'10.10.35.12', 
			host:'HARDWARE-SERVER-2',
			type: "HARDWARE SERVER",
			system: "PHYSICAL INFRASTRUCTURE"
		}) 

// Create Hardware 3
CREATE (hardware3:Hardware { 
			ip:'10.10.35.13', 
			host:'HARDWARE-SERVER-3',
			type: "HARDWARE SERVER",
			system: "PHYSICAL INFRASTRUCTURE"
		}) 

// Create SAN 1
CREATE (san1:Hardware { 
			ip:'10.10.35.14', 
			host:'SAN',
			type: "STORAGE AREA NETWORK",
			system: "PHYSICAL INFRASTRUCTURE"
		}) 

// Connect CRM to Database VM 1
CREATE (crm1)-[:DEPENDS_ON]->(customerdatabase1)

// Connect Public Websites 1-3 to Database VM 1
CREATE 	(Internet1)-[:DEPENDS_ON]->(customerdatabase1),
	   	(Internet2)-[:DEPENDS_ON]->(customerdatabase1),
	   	(Internet3)-[:DEPENDS_ON]->(customerdatabase1)

// Connect Database VM 1 to Hardware 1
CREATE 	(customerdatabase1)-[:DEPENDS_ON]->(hardware1)

// Connect Hardware 1 to SAN 1
CREATE 	(hardware1)-[:DEPENDS_ON]->(san1)

// Connect Public Websites 1-3 to Webserver VM 1
CREATE 	(webservervm1)<-[:DEPENDS_ON]-(Internet1),
		(webservervm1)<-[:DEPENDS_ON]-(Internet2),
		(webservervm1)<-[:DEPENDS_ON]-(Internet3)

// Connect Internal Websites 1-3 to Webserver VM 1
CREATE 	(webservervm1)<-[:DEPENDS_ON]-(Intranet1),
		(webservervm1)<-[:DEPENDS_ON]-(Intranet2),
		(webservervm1)<-[:DEPENDS_ON]-(Intranet3)

// Connect Webserver VM 1 to Hardware 2
CREATE 	(webservervm1)-[:DEPENDS_ON]->(hardware2)

// Connect Hardware 2 to SAN 1
CREATE 	(hardware2)-[:DEPENDS_ON]->(san1)

// Connect Webserver VM 2 to Hardware 2
CREATE 	(webservervm2)-[:DEPENDS_ON]->(hardware2)

// Connect Public Websites 4-6 to Webserver VM 2
CREATE 	(webservervm2)<-[:DEPENDS_ON]-(Internet4),
		(webservervm2)<-[:DEPENDS_ON]-(Internet5)

// Connect Database VM 2 to Hardware 2
CREATE 	(hardware2)<-[:DEPENDS_ON]-(customerdatabase2)

// Connect Public Websites 4-5 to Database VM 2
CREATE 	(Internet4)-[:DEPENDS_ON]->(customerdatabase2),
	   	(Internet5)-[:DEPENDS_ON]->(customerdatabase2)

// Connect Hardware 3 to SAN 1
CREATE 	(hardware3)-[:DEPENDS_ON]->(san1)

// Connect Database VM 3 to Hardware 3
CREATE 	(hardware3)<-[:DEPENDS_ON]-(databasevm3)

// Connect ERP 1 to Database VM 3
CREATE 	(erp1)-[:DEPENDS_ON]->(databasevm3)

// Connect Database VM 4 to Hardware 3
CREATE 	(hardware3)<-[:DEPENDS_ON]-(dwdatabase)

// Connect Data Warehouse 1 to Database VM 4
CREATE 	(datawarehouse1)-[:DEPENDS_ON]->(dwdatabase)

RETURN *
```
#### Exploratory analysis
**Schema Overview:**
``` cypher
CALL db.schema.visualization()
```
**Show all:**
``` cypher
MATCH (n) RETURN n;
```
**Check how many nodes are in the database:**
``` cypher
MATCH ()
RETURN count (*)
```
**View all Nodes and Relationships:**
``` cypher
MATCH (n)
RETURN n LIMIT 100
```
**Count of different types of Nodes:**
``` cypher
MATCH (n)
RETURN labels(n) AS type, count(*) AS Count
ORDER BY Count DESC
```
**Examine Relationships types between Nodes:**
``` cypher
MATCH ()-[r]->()
RETURN type(r) AS DEPENDS_ON, count(*) AS Count
ORDER BY Count DESC
```
**Find shortest path between two Nodes:**
``` cypher
MATCH (a:Hardware {host: 'HARDWARE-SERVER-2'})
MATCH (b:Hardware {host: 'HARDWARE-SERVER-3'})
MATCH p = shortestPath((a)-[*..15]-(b))
RETURN p
```
**Graph Density:**
``` cypher
MATCH (n:Hardware)
WITH toFloat(count(n)) AS nodes
MATCH (:Hardware)-[r]->(:Hardware)
WITH nodes, count(r) AS edges
RETURN edges / (nodes * (nodes - 1.0)) AS Density
```
**Top 10 Nodes with the most Relationships:**
``` cypher
MATCH (n)
RETURN n.host AS Host, count { (n)--() } AS Degree
ORDER BY Degree DESC
LIMIT 10
```
**Show graph with 25 nodes that have a certain Relationship:**
``` cypher
MATCH p=()-[:DEPENDS_ON]->() RETURN p LIMIT 25;
```
#### Advanced analysis
**Query generates a data table that gives a quick overview of ACME's network infrastructure:**
``` cypher
MATCH 	(n) 
RETURN 	labels(n)[0] as type,
		count(*) as count, 
		collect(n.host) as names
```
**Find the most depended-upon component:**
``` cypher
MATCH 		(n)<-[:DEPENDS_ON*]-(dependent)
RETURN 		n.host as Host, 
			count(DISTINCT dependent) AS Dependents
ORDER BY 	Dependents DESC
LIMIT 		1
```
**Path of dependent components from left to right for ACME's CRM application:**
``` cypher
MATCH 		(dependency)<-[:DEPENDS_ON*]-(dependent)
WITH 		dependency, count(DISTINCT dependent) AS Dependents
ORDER BY 	Dependents DESC
LIMIT		1
WITH		dependency
MATCH 		p=(resource)-[:DEPENDS_ON*]->(dependency)
WHERE		resource.system = "CRM"
RETURN		"[" + head(nodes(p)).host + "]" + 
			reduce(s = "", n in tail(nodes(p)) | s + " -> " + "[" + n.host + "]") as Chain
```
**Path of dependent components from left to right for ACME's ERP (Enterprise Resource Planning) application:**
``` cypher
MATCH 		(dependency)<-[:DEPENDS_ON*]-(dependent)
WITH 		dependency, count(DISTINCT dependent) AS Dependents
ORDER BY 	Dependents DESC
LIMIT		1
WITH		dependency
MATCH 		p=(resource)-[:DEPENDS_ON*]->(dependency)
WHERE		resource.system = "ERP"
RETURN		"[" + head(nodes(p)).host + "]" + 
			reduce(s = "", n in tail(nodes(p)) | s + " -> " + "[" + n.host + "]") as Chain
```
**Query finds the applications depending on ACME's HARDWARE-SERVER-3:**
``` cypher
MATCH (application:Application)-[:DEPENDS_ON*]->(server)
WHERE       server.host = "HARDWARE-SERVER-3"
RETURN  application.type as Type,
        application.host as Host
```
**Query the data model to find all business web applications that are on the public facing internet for ACME:**
``` cypher
MATCH 		(website)-[:DEPENDS_ON]->(downstream)
WHERE		website.system = "INTERNET"
RETURN 		website.host as Host, 
			collect(downstream.host) as Dependencies
ORDER BY 	Host
```

**Author:**
Zbigniew Galar
