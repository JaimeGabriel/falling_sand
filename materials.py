import numpy as np
import pygame

class Material:
    def __init__(self, color, state, value, width):
        self.color = color
        self.state = state
        self.value = value
        self.width = width

    def metodo_prueba(self):
        print('prueba')



class Grid:
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        self.grid=np.zeros((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.screen_width = SCREEN_WIDTH
        self.screen_height = SCREEN_HEIGHT
        self.position=[]


    def add_sand(self, x, y, material_width):
        if x >= 0 and x <= self.screen_width + material_width:
            if self.grid[x, y] == 0:
                self.grid[x, y] = 1

    def draw(self, screen, color, material_width):
        for points in self.position:
            pygame.draw.rect(screen, color, 8, 0)  


