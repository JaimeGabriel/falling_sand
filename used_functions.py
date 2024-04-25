import pygame
from globals import *

def draw_mouse_position():
    '''
    Function that gets and draws the position of the mouse at all time.
    '''
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if mouse_x > 0 and mouse_x < width - 1 and mouse_y > 0 and mouse_y < height - 1:
        pygame.draw.circle(screen, RED, (mouse_x, mouse_y), brush_size * square_size) 


def draw_screen(matrix):
    '''
    Function that draw the screen from the matrix of integers.
    '''
    for row in range(n):

        for col in range(m):
            color = SAND if matrix[row][col] == 1 else WATER if matrix[row][col] == 2 else ROCK if matrix[row][col] == 3 else BLACK
            pygame.draw.rect(screen, color, (col * square_size, row * square_size, square_size, square_size))

def random_index(m):
    '''
    Returns a random ordered list of numbers from 0 to m
    '''

    # Generar índices de columnas
    column_indices = list(range(m))
    np.random.shuffle(column_indices)  # Barajar los índices

    return column_indices


def is_left_mouse_button_pressed():
    mouse_buttons = pygame.mouse.get_pressed()
    return mouse_buttons[0]
