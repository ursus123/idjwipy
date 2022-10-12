# Table: </br> Idjwi.Addresses

This is how to use the table addresses to map objects of the real world. <br/>
This table is going to be build on the top of **[OpenStreetMap](/www.openstreetmap.org)**.
How to use Open Street Map Api Click [Here](https://towardsdatascience.com/loading-data-from-openstreetmap-with-python-and-the-overpass-api-513882a27fd0)
# Map Features
OpenStreetMap represents physical features on the ground (e.g., roads or buildings) using **tags** attached to its basic data structures (its nodes, ways, and relations). <br/> 
Each tag describes a geographic attribute of the feature being shown by that specific node, way or relation.
For More information [Read Here](https://wiki.openstreetmap.org/wiki/Map_features).

## Nodes
- A **Node** represents a specific point on the earth's surface defined by its ***latitude*** and ***longitude***. 
- Each node comprises at least an id number and a pair of coordinates.<br />
Nodes can be used to define standalone point features. <br />
For example, a node could represent a park bench or a water well. <br/>

**highway=traffic_signals:** marks signals on the road <br />
highway is a node and traffic_signals a **tag**. <br />

## Ways
- A **way** is an ordered list of between 2 and 2,000 nodes that define a polyline. <br/>
- Ways are used to represent linear features such as rivers and roads. <br/>
- Ways can also represent the boundaries of areas (solid polygons) such as buildings or forests.<br/>
- In this case, the way's first and last node will be the same. This is called a **closed way**

## Relations
- A **relation** is a multi-purpose data structure that documents a relationship between two or more data elements (nodes, ways, and/or other relations). <br/>

## Open Street Map Query Examples:

- node(id); out body; : returns node (using OSM database Id)
- way **['name'='New York']*(50.7,7.1,50.8,7.25)*** this returns **New York** from the box of the specified coordiantes format is like this way[]*(s,w,n,e)*
- (node['name'='Foo']; node['name'='bar'];)->.__; finds the two elements and sends them to the default set ._
- (node['name'='bar']; node['name'='Foo'];)->.a; writes elements to set named **a**
- settings : [timeout:180] run-time allowed (more than 180 sec query might be rejected)
- settings: [maxsize:1073741824] memory allowed (Default is 536870912 (521 MB))
- settings: [out:csv(::id,::type,'name')]; area[name='Boston']*nwr(area)[railway =station]*
- [out:csv(::type,::id,'name',::count)];area[name='Bonn]->.a;(node())