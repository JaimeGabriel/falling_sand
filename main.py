import numpy as np
import pygame
from materials import Material
from materials import Grid

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


sand_color = (194, 178, 128)

sand = Material(sand_color, 'liquid', 1, 8)
run = True
grid_instance = Grid(SCREEN_WIDTH, SCREEN_HEIGHT)  # Crear una instancia de la clase Grid
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif pygame.mouse.get_pressed()[0]:
                pos=pygame.mouse.get_pos()
                grid_instance.add_sand(pos[0]-pos[0]%sand.width, pos[1]-pos[1]%sand.width, sand.width)  
    
    grid_instance.draw(screen, sand_color, sand.width)

pygame.quit()
