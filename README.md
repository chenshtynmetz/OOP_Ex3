# OOP_Ex3

### In this task we asked to peresent graph and do algorinms on him in Pyhton.
### For do this we implement a few classes:
### Node: 
the node data present a vertex that include: id (int), location(Geolocation), information(String) and tag (int). This class implements get and set methods.
### Edge:
the edge data present a edge on the graph that include: source node(Node_Data), destination node(Node_Data), weight (double), information (string) and tag (int).  This class implements get and set methods.
### DiGraph:
this object present the graph. This class include a few hashmap: 1.mapOfNode: a hash of all the nodes. 2.mapOfEdge: a hash of all the edges. 3.mapOfSrc: a hash that for all node on the graph, keep a hashmap that the key is node that connect to our node with edge and the value is the edge. 4.mapOfDst: the opsite from the mapOfSrc. This class implements get and set methods. In addition this class implemntes the functions: addnode, removenoade, removeedge, connect- connect 2 nodes with edge, iteredge- a iterator of the edge, iternode- a iterator of the nodes, iteredge(int key)- a iterator of all the edge that connect to the node with id key.
### GraphAlgo: 
this class implements methods that activate algorithems on the graph:
Isconnected: return true if the graph is connected. We implements BFS algorithem to help us with this methods.
Center: conculate the center of the graph.
Shortestpathdis: return the shortest path between to vertexes.
Shortestpath: return all the vertex that need to pass for the short path in list.
Tsp: conculate tsp problem.
Save: save the graph to json file.
Load: load graph

#### running times on big graphs:
##### load:
1000: 
10000: 
100000: 
##### save:
1000: 
10000: 
100000: 
##### is connected:
1000: 
10000: 
100000: 
##### short path:
1000: 
10000: 
100000: 
##### tsp: 
1000: 
10000: 
100000:
##### center:
1000: 

### How to run:
to run the program plese enter the next line to the comand line: java -jar Ex2.jar and in the end the name of the json file, for example: G1.json 

### Our GUI:
to start our GUI you need to run the program in the way that we describe before, now it's possible to activate algoritemes on the graph, but if you want to change the graph, you need first to load the json file. 
