import json
import math

from typing import List
from queue import PriorityQueue
import queue
from src.GeoLocation import GeoLocation
from src.DiGraph import DiGraph, Node
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
        try:

            with open(file_name, "r") as f:
                dict = json.load(f)
            for n in dict["Nodes"]:
               # self.graph.add_node(n["id"], pos=GeoLocation(n["pos"]))
                self.graph.add_node(n["id"], n["pos"])
            for e in dict["Edges"]:
                self.graph.add_edge(e["src"], e["dest"], e["w"])
        except Exception:
                return False
        return True

    # todo how to save to json in the same way that they want?
    def save_to_json(self, file_name: str) -> bool:
        data = f'"Edges":{self.graph.edges.values()}"Nodes:{self.graph.edges.values()}'
        with open(file_name, "w") as f:
            json_object = json.dumps(str(self.graph), indent=0, sort_keys=True)
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
        distance = self.graph.nodes.get(id2).weight
        return distance, ans

    def diakstra(self, id1: int, id2: int):#-> (float)
        if id1 == id2:
            return 0
        queue = PriorityQueue()
        for node in self.graph.nodes.values():
            node.weight = math.inf
        self.clean_tag()
        self.graph.nodes.get(id1).weight = 0.0
        queue.put((self.graph.nodes.get(id1).weight, self.graph.nodes.get(id1)))
        while not queue.empty():
            (tempDis, tempNode) = queue.get()
            for i in self.graph.e_dictOfSrc.get(tempNode.id).keys():
                if tempNode.weight + self.graph.e_dictOfSrc[tempNode.id][i].weight < self.graph.nodes.get(i).weight:
                    new_dis = tempNode.weight + self.graph.e_dictOfSrc[tempNode.id][i].weight
                    self.graph.nodes.get(i).weight = new_dis
                    self.graph.nodes.get(i).tag = tempNode.id
                    queue.put((new_dis, self.graph.nodes.get(i)))

        return self.graph.nodes.get(id2).weight

    def clean_tag(self):
        for i in self.graph.nodes.values():
            i.tag = 0

    def clean_info(self):
        for i in self.graph.nodes.values():
            i.info = ''

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        path = []
        mini = math.inf
        temp_key = -1
        len_path = 0
        temp_node = node_lst.pop(0)
        path.append(temp_node)
        while len(node_lst) != 0:
            for node in node_lst:
                dis = self.diakstra(temp_node , node)
                if mini > dis:
                    mini = dis
                    temp_key = node
            temp_node = node_lst.pop(temp_key)
            path.append(temp_node)
            len_path = len_path + mini
            mini = math.inf
        return path, len_path


    def centerPoint(self) -> (int, float):
        mini = math.inf
        ind = -1
        for node in self.graph.nodes.keys():
            self.clean_tag()
            self.clean_info()
            if node == 0:
                self.diakstra(node, 1)
            else:
                self.diakstra(node, 0)
            max_short_path = -1 * math.inf
            for other in self.graph.nodes.keys():
                if other == node:
                    continue
                if self.graph.nodes.get(other).weight > max_short_path:
                    max_short_path = self.graph.nodes.get(other).weight
            if mini > max_short_path:
                mini = max_short_path
                ind = node
        return ind, mini

    # def plot_graph(self) -> None:

    # reverse and regular because the function get a dict
    def BFS(self, src_node: Node, dic: {}) -> bool:
        my_queue = [src_node]
        while len(my_queue) > 0:
            node_temp = my_queue.pop()
            for i in self.graph.e_dictOfSrc.get(node_temp).keys():
                if node_temp.info == "white":
                    edge_temp = dic.get(node_temp).i
                    my_queue.append(self.graph.nodes.get(edge_temp.dest))
            node_temp.info = "black"
        for i in self.graph.nodes.keys():
            if self.graph.nodes.get(i).info == "white":
                return False
        return True

    def isConnect(self) -> bool:
        head = self.graph.nodes.get(0)
        self.clean_tag()
        self.clean_info()
        path = self.BFS(head, self.graph.e_dictOfSrc)
        if not path:
            return False
        path = self.BFS(head, self.graph.e_dictOfDest)
        return path


if __name__ == '__main__':
    g = DiGraph()
    t = (5, 6, 7)
    g.add_node(5, GeoLocation(t))
    g.add_node(3, GeoLocation(t))
    g.add_edge(3, 5, 8)
    alg = GraphAlgo(g)
    alg.save_to_json("sve.json")
