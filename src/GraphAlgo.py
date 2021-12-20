import json
import math

import mathplotlib.pyplot as plt
from typing import List
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

    # def shortest_path(self, id1: int, id2: int) -> (float, list):
    #
    # def TSP(self, node_lst: List[int]) -> (List[int], float):
    #
    # def centerPoint(self) -> (int, float):
    #
    # def plot_graph(self) -> None:
