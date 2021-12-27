import random

from src.GraphInterface import GraphInterface


# class of node on the graph
class Node:
    def __init__(self, _id: int, pos: tuple = None):
        self.id = _id
        self.pos = pos
        self.tag = 0
        self.info = ""
        self.weight = 0

    def __repr__(self):
        return f'"pos": {str(self.pos)}\n"id": {self.id}'


# class of edge on the graph
class Edge:
    def __init__(self, src: int, dest: int, weight: float):
        self.src = src
        self.dest = dest
        self.weight = weight
        self.tag = 0
        self.info = ""

    def __repr__(self):
        return f'"src": {self.src}\n"w": {self.weight}\n"dest": {self.dest}'


class DiGraph(GraphInterface):
    # init graph
    def __init__(self):
        self.nodes = {}
        self.e_dictOfSrc = {}
        self.e_dictOfDest = {}
        self.edges = {}
        self.mc = 0

    # return the number of vertexes on the graph
    def v_size(self) -> int:
        return len(self.nodes)

    # return the number of edges on the graph
    def e_size(self) -> int:
        return len(self.edges)

    # return a dictionary of all the vertexes in the graph
    def get_all_v(self) -> dict:
        return self.nodes

    # return a dictionary of all the edges that have the same specific destination vertex
    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.e_dictOfDest.get(self, id1)

    # return a dictionary of all the edges that have the same specific source vertex
    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.e_dictOfSrc.get(self, id1)

    # return the number of update that the graph pass
    def get_mc(self) -> int:
        return self.mc

    # add a new edge to the graph
    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 in self.e_dictOfDest[id2]:
            return False
        if id1 in self.nodes and id2 in self.nodes:
            edge = Edge(id1, id2, weight)
            self.edges[(id1, id2)] = edge
            self.e_dictOfSrc[id1][id2] = edge
            self.e_dictOfDest[id2][id1] = edge
            self.mc = self.mc + 1
            return True
        return False

    # add a new node to the graph
    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id in self.nodes:
            return False
        if pos is None:
            x = random.uniform(35.19, 35.22)
            y = random.uniform(32.05, 32.22)
            pos = (x, y, 0.0)
        self.nodes[node_id] = Node(node_id, pos)
        self.e_dictOfSrc[node_id] = {}
        self.e_dictOfDest[node_id] = {}
        self.mc = self.mc + 1
        return True

    # remove specific node from the graph
    def remove_node(self, node_id: int) -> bool:
        if node_id in self.nodes:
            self.nodes.pop(self, node_id)
            self.e_dictOfSrc.pop(self, node_id)
            self.e_dictOfDest.pop(self, node_id)
            self.mc = self.mc + 1
            return True
        return False

    # remove specific edge from the graph
    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id1 in self.e_dictOfDest[node_id2] and node_id2 in self.e_dictOfSrc[node_id1]:
            del self.edges[(node_id1, node_id2)]
            del self.e_dictOfSrc[node_id1][node_id2]
            del self.e_dictOfDest[node_id2][node_id1]
            self.mc = self.mc + 1
            return True
        return False

    def __str__(self):
        return f'"Edges":{self.edges.values()}"Nodes": {self.nodes.values()}'
