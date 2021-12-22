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
min_x = alg.graph.nodes.get(min(alg.graph.nodes, key=lambda n: alg.graph.nodes.get(n).pos.x)).pos.x
max_x = alg.graph.nodes.get(max(alg.graph.nodes, key=lambda n: alg.graph.nodes.get(n).pos.x)).pos.x
min_y = alg.graph.nodes.get(min(alg.graph.nodes, key=lambda n: alg.graph.nodes.get(n).pos.y)).pos.y
max_y = alg.graph.nodes.get(max(alg.graph.nodes, key=lambda n: alg.graph.nodes.get(n).pos.y)).pos.y


with open('A0.json', 'r') as file:
    while True:
        for eve in pygame.event.get():
            if eve.type == pygame.QUIT:
                pygame.quit()
                exit(0)
        screen.fill(pygame.Color(100, 22, 100))
        pygame.display.set_caption("Graph")
        for edge in alg.graph.edges:
            src = alg.graph.nodes.get(alg.graph.edges.get(edge).src).pos
            dest = alg.graph.nodes.get(alg.graph.edges.get(edge).dest).pos
            src_x = scale(src.x, margin, screen.get_width() - margin, min_x, max_x)
            src_y = scale(src.y, margin, screen.get_height() - margin, min_y, max_y)
            dest_x = scale(dest.x, margin, screen.get_width() - margin, min_x, max_x)
            dest_y = scale(dest.y, margin, screen.get_height() - margin, min_y, max_y)
            pygame.draw.line(screen, pygame.Color(255,250,250), (src_x, src_y), (dest_x, dest_y), width=2)

        for node in alg.graph.nodes:
            x = scale(alg.graph.nodes.get(node).pos.x, margin, screen.get_width() - margin, min_x, max_x)
            y = scale(alg.graph.nodes.get(node).pos.y, margin, screen.get_height() - margin, min_y, max_y)
            pygame.draw.circle(screen, pygame.Color(221, 209, 60), (x, y), r)
        pygame.display.update()
        clock.tick(60)
