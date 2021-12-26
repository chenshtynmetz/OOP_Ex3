# OOP_Ex3

### In this task we asked to peresent graph and do algorinms on him in Pyhton.
### For do this we implement a few classes:
### Node: 
the node class present a vertex that include: id (int), location(Geolocation), information(String), tag (int) and weight(flout).<br />	
### Edge:
the edge class present a edge on the graph that include: source node(Node), destination node(Node), weight (flout), information (string) and tag (int).<br /> 
### DiGraph:
this object present the graph. This class include a few dictionaries:<br /> 1. nodes: a dictionary of all the nodes.<br /> 2. edges: a dictionary of all the edges.<br /> 3. e_dictOfSrc: a dictionary that for all node on the graph, keep a dictionary that the key is node that connect to our node with edge and the value is the edge.<br /> 4. e_dictOfDest: the opsite from the e_dictOfSrc.<br /> This class implements get and set methods.<br /> In addition this class implemntes the functions:<br /> add_node, remove_noade, remove_edge,  connect- connect 2 nodes with edge, v_size, e_size, get_all_v, all_in_edeges_of_node, all_out_edges_of_node and toString
### GraphAlgo: 
this class implements methods that activate algorithems on the graph:
Isconnected: return true if the graph is connected. We implements BFS algorithem to help us with this methods.<br />
Center: conculate the center of the graph.<br />
Shortestpath: return the shortest path between to vertexes and all the vertex that need to pass for the short path in list.<br />
Tsp: conculate tsp problem.<br />
Save: save the graph to json file.<br />
Load: load graph.<br />

#### running times on big graphs:
you can see our result on our Wiki page {adrees}
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
