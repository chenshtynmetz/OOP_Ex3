import json
import math

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
        data = f'"Edges":{self.graph.edges.values()}"Nodes:{self.graph.edges.values()}'
        with open(file_name, "w") as f:
            json_object = json.dumps(data, indent=0, sort_keys=True, separators=('\n'))
            f.write(json_object)
            # data = f'"Edges": \n {self.graph.edges.values()}"Nodes:\n{self.graph.edges.values()}'
            # json.dump(data, fp=f, indent=4, default=lambda o: o.__dict__)
            # f.close()
        return True

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        ans = []
        self.diakstra(id1, id2)
        ans.append(self.graph.nodes.get(id2))
        node_temp = self.graph.nodes.get(id2).tag
        while node_temp != id1:
            ans.append(node_temp)
            node_temp = self.graph.nodes.get(self.graph.nodes.get(node_temp).tag)
        ans.append(self.graph.nodes.get(id1))
        return self.graph.nodes.get(id2).weight, ans

    def diakstra(self, id1: int, id2: int):  # -> (float):
        queue = PriorityQueue()
        for node in self.graph.nodes.values():
            node.weight = math.inf
        self.graph.nodes.get(id1).wight = 0
        queue.put(self.graph.nodes.get(id1).wight, self.graph.nodes.get(self, id1))
        while not queue.empty():
            (tempDis, tempNode) = queue.get()
            for i in self.graph.e_dictOfSrc.get(tempNode.id).keys():
                if tempNode.weight + self.graph.e_dictOfSrc[tempNode.id][i].weight < self.graph.nodes.get(i).weight:
                    new_dis = tempNode.weight + self.graph.e_dictOfSrc[tempNode.id][i]
                    self.graph.nodes.get(i).weight = new_dis
                    self.graph.nodes.get(i).tag = tempNode.id
                    queue.put(new_dis, self.graph.nodes.get(i))

    # return self.graph.nodes.get(id2).weight

    def clean_tag(self):
        for i in self.graph.nodes.values():
            i.tag = 0

    # def TSP(self, node_lst: List[int]) -> (List[int], float):

    def centerPoint(self) -> (int, float):
        min = math.inf
        ind = -1
        for node in self.graph.nodes.keys():
            self.diakstra(node, 0)
            max_short_path = -1 * math.inf
            if self.graph.nodes.get(node).weight > max_short_path:
                max_short_path = self.graph.nodes.get(node).weight
            if min > max_short_path:
                min = max_short_path
                ind = node
        return ind, self.graph.nodes.get(ind).weight

    # def plot_graph(self) -> None:


if __name__ == '__main__':
    g = DiGraph()
    t = (5, 6, 7)
    g.add_node(5, GeoLocation(t))
    g.add_node(3, GeoLocation(t))
    g.add_edge(3, 5, 8)
    alg = GraphAlgo(g)
    alg.save_to_json("sve.json")
