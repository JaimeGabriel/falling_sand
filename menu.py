import pygame
from globals import *

class MenuItem:
    def __init__(self, value, color, text, position):
        self.value = value
        self.color = color
        self.original_color = color
        self.text = text
        self.position = position

    def draw_menu(self, surface, is_pressed = False):
        '''
        Draw the menu. The color of the buttons changes when they are pressed
        '''
        if is_pressed: 
            pressed_color = tuple(max(0, c - 50) for c in self.color)  
            pygame.draw.rect(surface, pressed_color, self.position)
        else: 
            pygame.draw.rect(surface, self.color, self.position)
        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.position.center)
        surface.blit(text_surface, text_rect)

    def set_pressed_color(self):  
        '''
        Set how the color of a button changes when pressed
        '''
        self.color = tuple(max(0, c - 50) for c in self.original_color)

    def reset_color(self):  
        '''
        Change the color of a button back to normal when is no longer pressed
        '''
        self.color = self.original_color