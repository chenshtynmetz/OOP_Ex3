from src.GraphInterface import GraphInterface


class Node:
    def __init__(self, _id: int, pos: tuple):
        self.id = _id
        self.pos = pos
        self.tag = 0
        self.info = ""
        self.wight = 0

    def __repr__(self):
        return f"pos: {self.pos}\nid: {self.id}"


class DiGraph(GraphInterface):
    def __init__(self):
        self.nodes = {}
        self.e_dictOfSrc = {}
        self.e_dictOfDest = {}
        self.mc = 0

    def v_size(self) -> int:
        return len(self.nodes)

    def e_size(self) -> int:
        return len(self.e_dictOfSrc)

    def get_all_v(self) -> dict:
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.e_dictOfDest.get(self, id1)

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.e_dictOfSrc.get(self, id1)

    def get_mc(self) -> int:
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 in self.e_dictOfDest[id2]:
            return False
        if id1 in self.nodes and id2 in self.nodes:
            self.e_dictOfSrc[id1][id2] = weight
            self.e_dictOfDest[id2][id1] = weight
            self.mc = self.mc + 1
            return True
        return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id in self.nodes:
            return False
        self.nodes[node_id] = Node(node_id, pos)
        self.e_dictOfSrc[node_id] = {}
        self.e_dictOfDest[node_id] = {}
        self.mc = self.mc + 1
        return True

    def remove_node(self, node_id: int) -> bool:
        if node_id in self.nodes:
            self.nodes.pop(self, node_id)
            self.e_dictOfSrc.pop(self, node_id)
            self.e_dictOfDest.pop(self, node_id)
            self.mc = self.mc + 1
            return True
        return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id1 in self.e_dictOfDest[node_id2] and node_id2 in self.e_dictOfSrc[node_id1]:
            # self.e_dictOfSrc.pop(self, self.e_dictOfSrc[node_id1][node_id2])
            # self.e_dictOfSrc[node_id1].pop([node_id2])
            del self.e_dictOfSrc[node_id1][node_id2]
            self.mc = self.mc + 1
            return True
        return False

    def __str__(self):
        return f"Edges:\n{self.e_dictOfSrc}\nNodes:{self.nodes}"
