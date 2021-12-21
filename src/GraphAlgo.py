import json
import math

import mathplotlib.pyplot as plt
from typing import List
from queue import PriorityQueue
from src.GeoLocation import GeoLocation
from src.DiGraph import DiGraph
from src.GraphAlgoInterface import GraphAlgoInterface
from src.GraphInterface import GraphInterface


class GraphAlgo(GraphAlgoInterface):
    # todo deep copy or not?
    def __init__(self, graph: DiGraph):
        self.graph = graph

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        dict = {}
        with open(file_name, "r") as f:
            dict = json.load(f)
        for n in dict["Nodes"].values():
            self.graph.add_node(n["id"], pos=GeoLocation(n["pos"]))
        for e in dict["Edges"].values():
            self.graph.add_edge(e["src"], e["dest"], e["w"])
        return True

    # todo how to save to json in the same way that they want?
    def save_to_json(self, file_name: str) -> bool:
        with open(file_name, "w") as f:
            json.dump(self, fp=f, indent=4, default=lambda o: o.__dict__)
        return True

    # def diakstra(self, ):

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        Pqueue = PriorityQueue()
        for node in self.graph.nodes.values():
            node.wight = math.inf
        self.graph.nodes.get(id1).wight = 0
        Pqueue.put(self.graph.nodes.get(id1).wight,self.graph.nodes.get(self, id1))
        while not Pqueue.empty():
            (tempDis, tempNode) = Pqueue.get()
            for i in self.graph.e_dictOfSrc.get(tempNode.id).keys():
                if (tempNode.wight + self.graph.e_dictOfSrc[tempNode.id][i] < self.graph.nodes.get(i).wight):
                    newDis = tempNode.wight + self.graph.e_dictOfSrc[tempNode.id][i]
                    self.graph.nodes.get(i).wight = newDis
                    self.graph.nodes.get(i).tag = tempNode.id
                    Pqueue.put(newDis, self.graph.nodes.get(i))

        return self.graph.nodes.get(id2).wight






    def clean_tag(self):
        for i in self.graph.nodes.values():
            i.tag = 0

            # def TSP(self, node_lst: List[int]) -> (List[int], float):
    #
    # def centerPoint(self) -> (int, float):
    #
    # def plot_graph(self) -> None:
