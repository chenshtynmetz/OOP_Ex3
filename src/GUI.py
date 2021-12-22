import math

import pygame
from src.DiGraph import DiGraph
from src.GeoLocation import GeoLocation
from src.GraphAlgo import GraphAlgo
from types import SimpleNamespace

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
Font = pygame.font.SysFont('david', 20)
alg = GraphAlgo(DiGraph())
alg.load_from_json('A0.json')


def scale(data, min_screen, max_screen, min_data, max_data):
    return ((float(data) - float(min_data)) / (float(max_data) - float(min_data))) * (max_screen - min_screen) + min_screen


WIDHT, HIGHT = 800, 600
screen = pygame.display.set_mode((WIDHT, HIGHT), depth=32, flags=pygame.constants.RESIZABLE)
r = 15
margin = 50
min_x = float(alg.graph.nodes.get(min(alg.graph.nodes, key=lambda n: alg.graph.nodes.get(n).pos.x)).pos.x)
max_x = float(alg.graph.nodes.get(max(alg.graph.nodes, key=lambda n: alg.graph.nodes.get(n).pos.x)).pos.x)
min_y = float(alg.graph.nodes.get(min(alg.graph.nodes, key=lambda n: alg.graph.nodes.get(n).pos.y)).pos.y)
max_y = float(alg.graph.nodes.get(max(alg.graph.nodes, key=lambda n: alg.graph.nodes.get(n).pos.y)).pos.y)

# min_x = math.inf
# max_x = math.inf * -1
# min_y = math.inf
# max_y = math.inf * -1
# for n in alg.graph.nodes:
#     if float(alg.graph.nodes.get(n).pos.x) < min_x:
#         min_x = float(alg.graph.nodes.get(n).pos.x)
#     if float(alg.graph.nodes.get(n).pos.x) > max_x:
#         max_x = float(alg.graph.nodes.get(n).pos.x)
#     if float(alg.graph.nodes.get(n).pos.y) < min_y:
#         min_y = float(alg.graph.nodes.get(n).pos.y)
#     if float(alg.graph.nodes.get(n).pos.y) > max_y:
#         max_y = float(alg.graph.nodes.get(n).pos.y)

with open('A0.json', 'r') as file:
    while True:
        for eve in pygame.event.get():
            if eve.type == pygame.QUIT:
                pygame.quit()
                exit(0)
        screen.fill(pygame.Color(100, 22, 100))
        for node in alg.graph.nodes:
            x = scale(alg.graph.nodes.get(node).pos.x, margin, screen.get_width() - margin, min_x, max_x)
            y = scale(alg.graph.nodes.get(node).pos.y, margin, screen.get_height() - margin, min_y, max_y)
            pygame.draw.circle(screen, pygame.Color(221, 209, 60), (x, y), r)
        pygame.display.update()
        clock.tick(60)
