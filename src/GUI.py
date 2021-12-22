import json
import pygame

from types import SimpleNamespace

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

Font = pygame.font.SysFont('david', 20)


WIDHT, HIGHT = 800, 600
screen = pygame.display.set_mode((WIDHT, HIGHT), depth=32)

with open('A0.json', 'r') as file:
    while True:
        for eve in pygame.event.get():
            if eve.type == pygame.QUIT:
                pygame.quit()
                exit(0)
        screen.fill(pygame.Color(100, 22, 100))
        pygame.display.update()
        clock.tick(60)




