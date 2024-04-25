import numpy as np
import pygame 

n = 100 # Rows of the matrix
m = 100 # Columns of the matrix
square_size = 8 # Number of pixel for a cell
width, height = m * square_size, n * square_size # Number of pixels of the game window
#matrix = np.random.randint(0, 3, size=(n, m))  # Initial matrix
matrix = np.zeros((n, m)) # Initial matrix

# Colors in RGB
BLACK = (0, 0, 0)
SAND = (194, 178, 128)
RED = (255, 0, 0)
WATER = (0, 0, 255)
ROCK = (128, 128, 128)
WHITE = (255, 255, 255)

# Parameters for the menu
material_item_menu_width = 100
material_item_menu_height = 50
brush_size_item_menu_width = 30
brush_size_item_menu_width = 30

# Initial parameters
selected_material = 1
brush_size = 1

# Pygame parameters
screen = pygame.display.set_mode((width, height))
