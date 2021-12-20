from typing import List

from src import DiGraph
from src.GraphAlgoInterface import GraphAlgoInterface
from src.GraphInterface import GraphInterface


class GraphAlgo(GraphAlgoInterface):
    def __init__(self, graph: DiGraph):
        self.graph = graph

    def get_graph(self) -> GraphInterface:
        return self.graph

#    def load_from_json(self, file_name: str) -> bool:


   # def save_to_json(self, file_name: str) -> bool:

  #  def shortest_path(self, id1: int, id2: int) -> (float, list):

 #   def TSP(self, node_lst: List[int]) -> (List[int], float):

#    def centerPoint(self) -> (int, float):

#    def plot_graph(self) -> None:







