# Table: Idjwi.Addresses

## Nodes
- A **Node** represents a specific point on the earth's surface defined by its ***latitude*** and ***longitude***. 
- Each node comprises at least an id number and a pair of coordinates.<br />
Nodes can be used to define standalone point features. <br />
For example, a node could represent a park bench or a water well. <br/ >

**highway=traffic_signals:** marks signals on the road <br />
highway is a node and traffic_signals a **tag**. <br />

## Ways
- A **way** is an ordered list of between 2 and 2,000 nodes that define a polyline. <br/>
- Ways are used to represent linear features such as rivers and roads. <br/>
- Ways can also represent the boundaries of areas (solid polygons) such as buildings or forests.<br/>
- In this case, the way's first and last node will be the same. This is called a **closed way**

## Relations
- A **relation** is a multi-purpose data structure that documents a relationship between two or more data elements (nodes, ways, and/or other relations). <br/>
- Examples include:
