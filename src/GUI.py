import math

import pygame
from src.DiGraph import DiGraph
from src.GeoLocation import GeoLocation
from src.GraphAlgo import GraphAlgo
from types import SimpleNamespace
class button:
    def __init__(self, rect: pygame.Rect, text: str, color: pygame.Color, func= None):
        self.rect = rect
        self.text = text
        self.color = color
        self.func = func
        self.is_pressed = False
    def pressed(self):
        self.is_pressed = not self.is_pressed

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
Font = pygame.font.SysFont('david', 20)
alg = GraphAlgo(DiGraph())
alg.load_from_json('A0.json')


def scale(data, min_screen, max_screen, min_data, max_data):
    return ((float(data) - float(min_data)) / (float(max_data) - float(min_data))) * (max_screen - min_screen) + min_screen

# screen = pygame.display.set_mode()
WIDHT, HIGHT = 800, 600
screen = pygame.display.set_mode((WIDHT, HIGHT), depth=32, flags=pygame.constants.RESIZABLE)
r = 15
margin = 50
min_x = min(alg.graph.nodes.values(), key=lambda n: n.pos.x).pos.x
max_x = max(alg.graph.nodes.values(), key=lambda n: n.pos.x).pos.x
min_y = min(alg.graph.nodes.values(), key=lambda n: n.pos.y).pos.y
max_y = max(alg.graph.nodes.values(), key=lambda n: n.pos.y).pos.y


with open('A0.json', 'r') as file:
    while True:
        for eve in pygame.event.get():
            if eve.type == pygame.QUIT:
                pygame.quit()
                exit(0)
        pygame.display.update()
        screen.fill(pygame.Color(100, 22, 100))
        pygame.display.set_caption("Graph")
        for edge in alg.graph.edges.values():
            src = alg.graph.nodes.get(edge.src).pos
            dest = alg.graph.nodes.get(edge.dest).pos
            src_x = scale(src.x, margin, screen.get_width() - margin, min_x, max_x)
            src_y = scale(src.y, margin, screen.get_height() - margin, min_y, max_y)
            dest_x = scale(dest.x, margin, screen.get_width() - margin, min_x, max_x)
            dest_y = scale(dest.y, margin, screen.get_height() - margin, min_y, max_y)
            pygame.draw.line(screen, pygame.Color(255, 250, 250), (src_x, src_y), (dest_x, dest_y), width=2)
            # pi = math.pi / 6
            # h = 12
            # x2 = dest_x - h * math.cos(math.atan2(dest_y - src_y, dest_x - src_x) + pi)
            # y2 = dest_y - h * math.cos(math.atan2(dest_y - src_y, dest_x - src_x) + pi)
            # x3 = dest_x - h * math.cos(math.atan2(dest_y - src_y, dest_x - src_x) - pi)
            # y3 = dest_y - h * math.cos(math.atan2(dest_y - src_y, dest_x - src_x) - pi)
            # points = [(dest_x-2, dest_y-2), (x2, y2), (x3 , y3)]
            # pygame.draw.polygon(screen, pygame.Color(255, 250, 250), points, width=4)
        for node in alg.graph.nodes.values():
            x = scale(node.pos.x, margin, screen.get_width() - margin, min_x, max_x)
            y = scale(node.pos.y, margin, screen.get_height() - margin, min_y, max_y)
            pygame.draw.circle(screen, pygame.Color(221, 209, 60), (x, y), r)
        clock.tick(60)
# button = Button(pygame.Rect(20, 100), (50, 50)), "algo",(250, 0, 0))