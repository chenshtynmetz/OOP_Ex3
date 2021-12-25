import math

import pygame
import pygame as pygame

from src.DiGraph import DiGraph, Node
from src.GeoLocation import GeoLocation
from src.GraphAlgo import GraphAlgo
from types import SimpleNamespace
from src.Button import Button

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
Font = pygame.font.SysFont('david', 20)
alg = GraphAlgo(DiGraph())
alg.load_from_json('A1.json')
active = False


# class TextInputBox(pygame.sprite.Sprite):
#     def __init__(self, x, y, w, font):
#         super().__init__()
#         self.color = (255, 255, 255)
#         self.backcolor = None
#         self.pos = (x, y)
#         self.width = w
#         self.font = font
#         self.active = False
#         self.text = ""
#         self.render_text()
#
#     def render_text(self):
#         t_surf = self.font.render(self.text, True, self.color, self.backcolor)
#         self.image = pygame.Surface((max(self.width, t_surf.get_width() + 10), t_surf.get_height() + 10),
#                                     pygame.SRCALPHA)
#         if self.backcolor:
#             self.image.fill(self.backcolor)
#         self.image.blit(t_surf, (5, 5))
#         pygame.draw.rect(self.image, self.color, self.image.get_rect().inflate(-2, -2), 2)
#         self.rect = self.image.get_rect(topleft=self.pos)
#
#     def update(self, event_list):
#         for event in event_list:
#             if event.type == pygame.MOUSEBUTTONDOWN and not self.active:
#                 self.active = self.rect.collidepoint(event.pos)
#             if event.type == pygame.KEYDOWN and self.active:
#                 if event.key == pygame.K_RETURN:
#                     self.active = False
#                 elif event.key == pygame.K_BACKSPACE:
#                     self.text = self.text[:-1]
#                 else:
#                     self.text += event.unicode
#                 self.render_text()


# pygame.init()
# window = pygame.display.set_mode((500, 200))
# clock1 = pygame.time.Clock()
# font = pygame.font.SysFont("Ariel", 100)

# text_input_box = TextInputBox(50, 50, 400, Font)
# group = pygame.sprite.Group(text_input_box)

# run = True
# while run:
#     clock1.tick(60)
#     event_list = pygame.event.get()
#     for event in event_list:
#         if event.type == pygame.QUIT:
#             run = False
#     group.update(event_list)
#
#     window.fill(pygame.Color(0, 0, 0))
#     group.draw(window)
#     pygame.display.flip()
#
# pygame.quit()
# exit()


def scale(data, min_screen, max_screen, min_data, max_data):
    return ((float(data) - float(min_data)) / (float(max_data) - float(min_data))) * (
            max_screen - min_screen) + min_screen


# screen = pygame.display.set_mode()
WIDHT, HIGHT = 800, 600
screen = pygame.display.set_mode((WIDHT, HIGHT), depth=32)
# keyboard = False
# text = ""
r = 12
margin = 50
# result = []
# node_screens = []
min_x = min(alg.graph.nodes.values(), key=lambda n: n.pos.x).pos.x
max_x = max(alg.graph.nodes.values(), key=lambda n: n.pos.x).pos.x
min_y = min(alg.graph.nodes.values(), key=lambda n: n.pos.y).pos.y
max_y = max(alg.graph.nodes.values(), key=lambda n: n.pos.y).pos.y
button_center = Button(pygame.Rect((10, 10), (70, 20)), "center", (255, 255, 0))
button_tsp = Button(pygame.Rect((10, 33), (70, 20)), "tsp", (255, 255, 0))
button_load = Button(pygame.Rect((10, 56), (70, 20)), "load", (255, 255, 0))
button_save = Button(pygame.Rect((10, 79), (70, 20)), "save", (255, 255, 0))
button_short = Button(pygame.Rect((10, 101), (120, 20)), "shortest path", (255, 255, 0))
button_nadd = Button(pygame.Rect((90, 10), (120, 20)), "add node", (255, 255, 0))
button_eadd = Button(pygame.Rect((90, 33), (120, 20)), "add edge", (255, 255, 0))
button_nremove = Button(pygame.Rect((90, 56), (120, 20)), "remove node", (255, 255, 0))
button_eremove = Button(pygame.Rect((90, 79), (120, 20)), "remove edge", (255, 255, 0))


class NodeScreen:
    def __init__(self, rect: pygame.Rect, id):
        self.rect = rect
        self.id = id


def draw_arrow(src, dst, d, hi, color):
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
    pygame.draw.line(screen, color, src, dst, width=2)
    pygame.draw.polygon(screen, color, points)


result = []
nodes_screen = []
tsp = []


def on_click(button: Button, list: []):
    global result
    result = button.func(list)
    print(result)


stop = False


def draw(remove):
    # if src1 != -1:
    #     src_text = Font.render(str(src1), True, (0, 0, 0))
    pygame.draw.rect(screen, button_center.color, button_center.rect)
    pygame.draw.rect(screen, button_tsp.color, button_tsp.rect)
    pygame.draw.rect(screen, button_load.color, button_load.rect)
    pygame.draw.rect(screen, button_save.color, button_save.rect)
    pygame.draw.rect(screen, button_short.color, button_short.rect)
    pygame.draw.rect(screen, button_nadd.color, button_nadd.rect)
    pygame.draw.rect(screen, button_nremove.color, button_nremove.rect)
    pygame.draw.rect(screen, button_eadd.color, button_eadd.rect)
    pygame.draw.rect(screen, button_eremove.color, button_eremove.rect)
    if button_load.is_pressed:
        button_load_text = Font.render(button_load.text, True, (0, 250, 250))
        alg.load_from_json("A2.json")  # todo change this to user input
    else:
        button_load_text = Font.render(button_load.text, True, (0, 0, 0))
    if button_save.is_pressed:
        button_save_text = Font.render(button_save.text, True, (0, 250, 250))
        alg.save_to_json("soe.json")  # todo change this to user input
    else:
        button_save_text = Font.render(button_save.text, True, (0, 0, 0))
    if button_nadd.is_pressed:
        button_nadd_text = Font.render(button_nadd.text, True, (0, 250, 250))
        # alg.graph.add_node(100, (32, 34, 0))  # todo change this to user input
        # button_nadd.func()
    else:
        button_nadd_text = Font.render(button_nadd.text, True, (0, 0, 0))
    if button_eadd.is_pressed:
        button_eadd_text = Font.render(button_eadd.text, True, (0, 250, 250))
        alg.graph.add_edge(5, 0, 2)  # todo change this to user input
    else:
        button_eadd_text = Font.render(button_eadd.text, True, (0, 0, 0))
    if button_nremove.is_pressed:
        button_nremove_text = Font.render(button_nremove.text, True, (0, 250, 250))
        alg.graph.remove_node(0)  # todo change this to user input
    else:
        button_nremove_text = Font.render(button_nremove.text, True, (0, 0, 0))
    if button_eremove.is_pressed:
        button_eremove_text = Font.render(button_eremove.text, True, (0, 250, 250))
        alg.graph.remove_edge(0, 1)
        # if remove[0] != -1 and remove[1] != -1:
        #     alg.graph.remove_edge(remove[0], remove[1])  # todo change this to user input
    else:
        button_eremove_text = Font.render(button_eremove.text, True, (0, 0, 0))
    for edge in alg.graph.edges.values():
        src = alg.graph.nodes.get(edge.src).pos
        dest = alg.graph.nodes.get(edge.dest).pos
        src_x = scale(src.x, margin, screen.get_width() - margin, min_x, max_x)
        src_y = scale(src.y, margin, screen.get_height() - margin, min_y, max_y)
        dest_x = scale(dest.x, margin, screen.get_width() - margin, min_x, max_x)
        dest_y = scale(dest.y, margin, screen.get_height() - margin, min_y, max_y)
        if edge.src and edge.dest in result:
            draw_arrow((src_x, src_y), (dest_x, dest_y), 15, 5, (0, 0, 150))
        else:
            draw_arrow((src_x, src_y), (dest_x, dest_y), 15, 5, (0, 0, 0))
    for node in alg.graph.nodes.values():
        x = scale(node.pos.x, margin, screen.get_width() - margin, min_x, max_x)
        y = scale(node.pos.y, margin, screen.get_height() - margin, min_y, max_y)
        pygame.draw.circle(screen, pygame.Color(255, 128, 0), (x, y), r)
        node_text = Font.render(str(node.id), True, pygame.Color((0, 0, 244)))
        screen.blit(node_text, (x - 8, y - 8))
        nodes_screen.append(NodeScreen(pygame.Rect((x, y), (24, 24)), node.id))
        # node_screens.append(NodeScreen(pygame.Rect((x, y), (20, 20)), node.id))
    if button_center.is_pressed:
        button_center_text = Font.render(button_center.text, True, (0, 250, 250))
        node = alg.centerPoint()
        xn = scale(alg.graph.nodes.get(node[0]).pos.x, margin, screen.get_width() - margin, min_x, max_x)
        yn = scale(alg.graph.nodes.get(node[0]).pos.y, margin, screen.get_height() - margin, min_y, max_y)
        pygame.draw.circle(screen, pygame.Color(128, 0, 64), (xn, yn), r)
    else:
        button_center_text = Font.render(button_center.text, True, (0, 0, 0))
    if button_tsp.is_pressed:
        button_tsp_text = Font.render(button_tsp.text, True, (0, 250, 250))
        # pygame.draw.rect(screen, stop_button.color, stop_button.rect)
        # stop = True
        # if stop_button.rect.collidepoint(eve.pos):
        #     stop_button.pressed()
        # if stop_button.is_pressed:
        #     stop = False
        #     on_click(button_tsp, tsp)
        #     tsp.clear()
        # else:
        #     for event in pygame.event.get():
        #         for n in nodes_screen:
        #             if n.rect.collidepoint(event.pos):
        #                 tsp.append(n.id)
    else:
        button_tsp_text = Font.render(button_tsp.text, True, (0, 0, 0))
        # stop = False
        # result.clear()
    if button_short.is_pressed:
        button_short_text = Font.render(button_short.text, True, (0, 250, 250))
        print(alg.shortest_path(0, 5))  # todo change this to user input
    else:
        button_short_text = Font.render(button_short.text, True, (0, 0, 0))
    screen.blit(button_center_text, (button_center.rect.x + 10, button_center.rect.y))
    screen.blit(button_tsp_text, (button_tsp.rect.x + 10, button_tsp.rect.y))
    screen.blit(button_load_text, (button_load.rect.x + 10, button_load.rect.y))
    screen.blit(button_save_text, (button_save.rect.x + 10, button_save.rect.y))
    screen.blit(button_short_text, (button_short.rect.x + 10, button_short.rect.y))
    screen.blit(button_nadd_text, (button_nadd.rect.x + 10, button_nadd.rect.y))
    screen.blit(button_nremove_text, (button_nremove.rect.x + 10, button_nremove.rect.y))
    screen.blit(button_eadd_text, (button_eadd.rect.x + 10, button_eadd.rect.y))
    screen.blit(button_eremove_text, (button_eremove.rect.x + 10, button_eremove.rect.y))


with open('A1.json', 'r') as file:
    remove = (-1, -1)
    button_center.func = alg.centerPoint
    button_tsp.func = alg.TSP
    button_nadd.func = alg.graph.add_node
    stop_button = Button(pygame.Rect((500, 33), (50, 50)), "", pygame.Color(250, 0, 0))
    while True:
        for eve in pygame.event.get():
            if eve.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            if eve.type == pygame.MOUSEBUTTONDOWN:
                if button_center.rect.collidepoint(eve.pos):
                    button_center.pressed()
                if button_tsp.rect.collidepoint(eve.pos):
                    button_tsp.pressed()
                if button_load.rect.collidepoint(eve.pos):
                    button_load.pressed()
                if button_save.rect.collidepoint(eve.pos):
                    button_save.pressed()
                if button_short.rect.collidepoint(eve.pos):
                    button_short.pressed()
                if button_nadd.rect.collidepoint(eve.pos):
                    button_nadd.pressed()
                    # if button_nadd.is_pressed:
                    #     n1 = Node(alg.graph.v_size() + 1, eve.pos)
                    #     alg.graph.add_node(n1.id)
                if button_nremove.rect.collidepoint(eve.pos):
                    button_nremove.pressed()
                if button_eadd.rect.collidepoint(eve.pos):
                    button_eadd.pressed()
                if button_eremove.rect.collidepoint(eve.pos):
                    button_eremove.pressed()
                    # if button_eremove.is_pressed:
                    #     for n1 in nodes_screen:
                    #         for n2 in nodes_screen:
                    #             if n1 != n2:
                    #                 if n1.rect.collidepoint(eve.pos) and n2.rect.collidepoint(eve.pos):
                    #                     remove = (n1, n2)
                # text_input_box = TextInputBox(50, 50, 400, Font)
                # group = pygame.sprite.Group(text_input_box)
                # run = True
                # while run:
                #     clock.tick(60)
                #     window = pygame.display.set_mode((500, 200))
                #     event_list = pygame.event.get()
                #     for event in event_list:
                #         if event.type == pygame.QUIT:
                #             run = False
                #     group.update(event_list)
                #
                #     window.fill(pygame.Color(0, 0, 0))
                #     group.draw(window)
                #     pygame.display.flip()
                #
                # pygame.quit()
                # screen = pygame.display.set_mode((WIDHT, HIGHT), depth=32)
                #     if eve.type == pygame.KEYDOWN:
                #         keyboard = True
                # if button_center.is_pressed:

        draw(remove)
        pygame.display.update()
        screen.fill(pygame.Color(255, 250, 250))
        pygame.display.set_caption("Graph")
        clock.tick(60)
