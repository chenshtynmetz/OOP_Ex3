import json
import math
import random

from typing import List
from queue import PriorityQueue
import easygui
import pygame
import matplotlib.pyplot as plt

from src.Button import Button
from src.GUI import GUI
from src.GeoLocation import GeoLocation
from src.DiGraph import DiGraph, Node
from src.GraphAlgoInterface import GraphAlgoInterface
from src.GraphInterface import GraphInterface


class GraphAlgo(GraphAlgoInterface):

    # todo deep copy or not?
    def __init__(self, graph: DiGraph):
        self.graph = graph
        self.WIDHT = 800
        self.HIGHT = 600
        self.screen = pygame.display.set_mode((self.WIDHT, self.HIGHT), depth=32)
        self.r = 12
        self.clock = pygame.time.Clock()
        self.Font = pygame.font.SysFont('david', 20)
        self.result = []
        self.nodes_screen = []
        self.tsp = []
        self.margin = 50
        self.button_center = Button(pygame.Rect((10, 10), (70, 20)), "center", (255, 255, 0))
        self.button_tsp = Button(pygame.Rect((10, 33), (70, 20)), "tsp", (255, 255, 0))
        self.button_load = Button(pygame.Rect((10, 56), (70, 20)), "load", (255, 255, 0))
        self.button_save = Button(pygame.Rect((10, 79), (70, 20)), "save", (255, 255, 0))
        self.button_short = Button(pygame.Rect((10, 101), (120, 20)), "shortest path", (255, 255, 0))
        self.button_nadd = Button(pygame.Rect((90, 10), (120, 20)), "add node", (255, 255, 0))
        self.button_eadd = Button(pygame.Rect((90, 33), (120, 20)), "add edge", (255, 255, 0))
        self.button_nremove = Button(pygame.Rect((90, 56), (120, 20)), "remove node", (255, 255, 0))
        self.button_eremove = Button(pygame.Rect((90, 79), (120, 20)), "remove edge", (255, 255, 0))
        self.min_x = math.inf
        self.max_x = math.inf * -1
        self.min_y = math.inf
        self.max_y = math.inf * -1

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        dict = {}
        try:

            with open(file_name, "r") as f:
                dict = json.load(f)
                list_nodes = dict["Nodes"]
                list_edge = dict["Edges"]
                for n in list_nodes:
                    try:
                        temp = n['pos'].split(",")
                        x = float(temp[0])
                        y = float(temp[1])
                        z = float(temp[2])
                        pos = (x, y, z)
                        self.graph.add_node(n['id'], pos)
                    except Exception:
                        x = random.uniform(35.19, 35.22)
                        y = random.uniform(32.05, 32.22)
                        pos = (x, y, 0.0)
                        self.graph.add_node(n['id', pos])
                for ed in list_edge:
                    self.graph.add_edge(ed['src'], ed['dest'], ed['w'])
            # for n in dict["Nodes"]:
            #    # self.graph.add_node(n["id"], pos=GeoLocation(n["pos"]))
            #     self.graph.add_node(n["id"], n["pos"])
            # for e in dict["Edges"]:
            #     self.graph.add_edge(e["src"], e["dest"], e["w"])
        except:
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
        ans.insert(0, id2)
        node_temp = self.graph.nodes.get(id2).tag
        while node_temp != id1:
            ans.insert(0, node_temp)
            node_temp = self.graph.nodes.get(node_temp).tag
        ans.insert(0, id1)
        distance = self.graph.nodes.get(id2).weight
        return distance, ans

    def diakstra(self, id1: int, id2: int):  # -> (float)
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
                dis = self.diakstra(temp_node, node)
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

    def plot_graph(self) -> None:
        self.min_x = float(min(list(self.graph.nodes.values()), key=lambda n: n.pos[0]).pos[0])
        self.max_x = float(max(list(self.graph.nodes.values()), key=lambda n: n.pos[0]).pos[0])
        self.min_y = float(min(list(self.graph.nodes.values()), key=lambda n: n.pos[1]).pos[1])
        self.max_y = float(max(list(self.graph.nodes.values()), key=lambda n: n.pos[1]).pos[1])
        pygame.init()
        pygame.font.init()
        self.display()
        # x = []
        # y = []
        # for node in self.graph.nodes.values():
        #     x.append(node.pos[0])
        #     y.append(node.pos[1])
        # plt.plot(x, y)
        # plt.show()

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

    def display(self):
        with open('data/A1.json', 'r') as file:
            remove = [-1, -1]
            self.button_center.func = self.centerPoint
            self.button_tsp.func = self.TSP
            self.button_nadd.func = self.graph.add_node
            # stop_button = Button(pygame.Rect((500, 33), (50, 50)), "", pygame.Color(250, 0, 0))
            while True:
                for eve in pygame.event.get():
                    if eve.type == pygame.QUIT:
                        pygame.quit()
                        exit(0)
                    if eve.type == pygame.MOUSEBUTTONDOWN:
                        if self.button_center.rect.collidepoint(eve.pos):
                            self.button_center.pressed()
                        if self.button_tsp.rect.collidepoint(eve.pos):
                            self.button_tsp.pressed()
                        if self.button_load.rect.collidepoint(eve.pos):
                            self.button_load.pressed()
                        if self.button_save.rect.collidepoint(eve.pos):
                            self.button_save.pressed()
                        if self.button_short.rect.collidepoint(eve.pos):
                            self.button_short.pressed()
                        if self.button_nadd.rect.collidepoint(eve.pos):
                            self.button_nadd.pressed()
                            # if button_nadd.is_pressed:
                            #     n1 = Node(alg.graph.v_size() + 1, eve.pos)
                            #     alg.graph.add_node(n1.id)
                        if self.button_nremove.rect.collidepoint(eve.pos):
                            self.button_nremove.pressed()
                        if self.button_eadd.rect.collidepoint(eve.pos):
                            self.button_eadd.pressed()
                        if self.button_eremove.rect.collidepoint(eve.pos):
                            self.button_eremove.pressed()

                self.draw(remove)
                pygame.display.update()
                self.screen.fill(pygame.Color(255, 250, 250))
                pygame.display.set_caption("Graph")
                self.clock.tick(60)

    def scale(self, data, min_screen, max_screen, min_data, max_data):
        return ((float(data) - float(min_data)) / (float(max_data) - float(min_data))) * (
                max_screen - min_screen) + min_screen

    def draw_arrow(self, src, dst, d, hi, color):
        dx = float(dst[0]) - float(src[0])
        dy = float(dst[1]) - float(src[1])
        s = float(math.sqrt(dx * dx + dy * dy))
        x1 = float(s - d)
        x2 = float(x1)
        y1 = float(hi)
        y2 = hi * -1
        sin = dy / s
        cos = dx / s
        x_temp = x1 * cos - y1 * sin + float(src[0])
        y1 = x1 * sin + y1 * cos + float(src[1])
        x1 = x_temp
        x_temp = x2 * cos - y2 * sin + float(src[0])
        y2 = x2 * sin + y2 * cos + float(src[1])
        x2 = x_temp
        points = [(dst[0], dst[1]), (int(x1), int(y1)), (int(x2), int(y2))]
        pygame.draw.line(self.screen, color, src, dst, width=2)
        pygame.draw.polygon(self.screen, color, points)

    def on_click(self, button: Button, list: []):
        global result
        result = button.func(list)
        print(result)

    def draw(self, remove):
        # if src1 != -1:
        #     src_text = Font.render(str(src1), True, (0, 0, 0))
        pygame.draw.rect(self.screen, self.button_center.color, self.button_center.rect)
        pygame.draw.rect(self.screen, self.button_tsp.color, self.button_tsp.rect)
        pygame.draw.rect(self.screen, self.button_load.color, self.button_load.rect)
        pygame.draw.rect(self.screen, self.button_save.color, self.button_save.rect)
        pygame.draw.rect(self.screen, self.button_short.color, self.button_short.rect)
        pygame.draw.rect(self.screen, self.button_nadd.color, self.button_nadd.rect)
        pygame.draw.rect(self.screen, self.button_nremove.color, self.button_nremove.rect)
        pygame.draw.rect(self.screen, self.button_eadd.color, self.button_eadd.rect)
        pygame.draw.rect(self.screen, self.button_eremove.color, self.button_eremove.rect)
        if self.button_load.is_pressed:
            button_load_text = self.Font.render(self.button_load.text, True, (0, 250, 250))
            self.load_from_json("./data/A2.json")  # todo change this to user input
            self.min_x = float(min(list(self.graph.nodes.values()), key=lambda n: n.pos[0]).pos[0])
            self.max_x = float(max(list(self.graph.nodes.values()), key=lambda n: n.pos[0]).pos[0])
            self.min_y = float(min(list(self.graph.nodes.values()), key=lambda n: n.pos[1]).pos[1])
            self.max_y = float(max(list(self.graph.nodes.values()), key=lambda n: n.pos[1]).pos[1])
        else:
            button_load_text = self.Font.render(self.button_load.text, True, (0, 0, 0))
        if self.button_save.is_pressed:
            button_save_text = self.Font.render(self.button_save.text, True, (0, 250, 250))
            self.save_to_json("soe.json")  # todo change this to user input
        else:
            button_save_text = self.Font.render(self.button_save.text, True, (0, 0, 0))
        if self.button_nadd.is_pressed:
            button_nadd_text = self.Font.render(self.button_nadd.text, True, (0, 250, 250))
            # alg.graph.add_node(100, (32, 34, 0))  # todo change this to user input
            # button_nadd.func()
        else:
            button_nadd_text = self.Font.render(self.button_nadd.text, True, (0, 0, 0))
        if self.button_eadd.is_pressed:
            button_eadd_text = self.Font.render(self.button_eadd.text, True, (0, 250, 250))
            self.graph.add_edge(5, 0, 2)  # todo change this to user input
        else:
            button_eadd_text = self.Font.render(self.button_eadd.text, True, (0, 0, 0))
        if self.button_nremove.is_pressed:
            button_nremove_text = self.Font.render(self.button_nremove.text, True, (0, 250, 250))
            self.graph.remove_node(0)  # todo change this to user input
        else:
            button_nremove_text = self.Font.render(self.button_nremove.text, True, (0, 0, 0))
        if self.button_eremove.is_pressed:
            button_eremove_text = self.Font.render(self.button_eremove.text, True, (0, 250, 250))
            self.graph.remove_edge(0, 1)  # todo change this to user input
            # if remove[0] != -1 and remove[1] != -1:
            #     alg.graph.remove_edge(remove[0], remove[1])
        else:
            button_eremove_text = self.Font.render(self.button_eremove.text, True, (0, 0, 0))
        for edge in self.graph.edges.values():
            src = self.graph.nodes.get(edge.src).pos
            dest = self.graph.nodes.get(edge.dest).pos
            src_x = self.scale(src[0], self.margin, self.screen.get_width() - self.margin, self.min_x, self.max_x)
            src_y = self.scale(src[1], self.margin, self.screen.get_height() - self.margin, self.min_y, self.max_y)
            dest_x = self.scale(dest[0], self.margin, self.screen.get_width() - self.margin, self.min_x, self.max_x)
            dest_y = self.scale(dest[1], self.margin, self.screen.get_height() - self.margin, self.min_y, self.max_y)
            if edge.src and edge.dest in self.result:
                self.draw_arrow((src_x, src_y), (dest_x, dest_y), 15, 5, (0, 0, 150))
            else:
                self.draw_arrow((src_x, src_y), (dest_x, dest_y), 15, 5, (0, 0, 0))
        for node in self.graph.nodes.values():
            x = self.scale(node.pos[0], self.margin, self.screen.get_width() - self.margin, self.min_x, self.max_x)
            y = self.scale(node.pos[1], self.margin, self.screen.get_height() - self.margin, self.min_y, self.max_y)
            pygame.draw.circle(self.screen, pygame.Color(255, 128, 0), (x, y), self.r)
            node_text = self.Font.render(str(node.id), True, pygame.Color((0, 0, 244)))
            self.screen.blit(node_text, (x - 8, y - 8))
            # self.nodes_screen.append(NodeScreen(pygame.Rect((x, y), (24, 24)), node.id))
            # node_screens.append(NodeScreen(pygame.Rect((x, y), (20, 20)), node.id))
        if self.button_center.is_pressed:
            button_center_text = self.Font.render(self.button_center.text, True, (0, 250, 250))
            node = self.centerPoint()
            xn = self.scale(self.graph.nodes.get(node[0]).pos[0], self.margin, self.screen.get_width() - self.margin,
                            self.min_x,
                            self.max_x)
            yn = self.scale(self.graph.nodes.get(node[0]).pos[1], self.margin, self.screen.get_height() - self.margin,
                            self.min_y,
                            self.max_y)
            pygame.draw.circle(self.screen, pygame.Color(128, 0, 64), (xn, yn), self.r)
        else:
            button_center_text = self.Font.render(self.button_center.text, True, (0, 0, 0))
        if self.button_tsp.is_pressed:
            button_tsp_text = self.Font.render(self.button_tsp.text, True, (0, 250, 250))
        else:
            button_tsp_text = self.Font.render(self.button_tsp.text, True, (0, 0, 0))
        if self.button_short.is_pressed:
            button_short_text = self.Font.render(self.button_short.text, True, (0, 250, 250))
            print(self.shortest_path(0, 5))  # todo change this to user input
        else:
            button_short_text = self.Font.render(self.button_short.text, True, (0, 0, 0))
        self.screen.blit(button_center_text, (self.button_center.rect.x + 10, self.button_center.rect.y))
        self.screen.blit(button_tsp_text, (self.button_tsp.rect.x + 10, self.button_tsp.rect.y))
        self.screen.blit(button_load_text, (self.button_load.rect.x + 10, self.button_load.rect.y))
        self.screen.blit(button_save_text, (self.button_save.rect.x + 10, self.button_save.rect.y))
        self.screen.blit(button_short_text, (self.button_short.rect.x + 10, self.button_short.rect.y))
        self.screen.blit(button_nadd_text, (self.button_nadd.rect.x + 10, self.button_nadd.rect.y))
        self.screen.blit(button_nremove_text, (self.button_nremove.rect.x + 10, self.button_nremove.rect.y))
        self.screen.blit(button_eadd_text, (self.button_eadd.rect.x + 10, self.button_eadd.rect.y))
        self.screen.blit(button_eremove_text, (self.button_eremove.rect.x + 10, self.button_eremove.rect.y))
