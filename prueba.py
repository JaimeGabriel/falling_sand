import pygame
import sys

# Inicializar Pygame
pygame.init()

# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Dimensiones de la pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class MenuItem:
    def __init__(self, color, text, position):
        self.color = color
        self.text = text
        self.position = position

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.position)  # Dibujar el cuadrado
        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.text, True, BLACK)  # Renderizar el texto
        text_rect = text_surface.get_rect(center=self.position.center)
        surface.blit(text_surface, text_rect)  # Dibujar el texto

def main():
    # Configurar la pantalla
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Menú Pygame")
    
    # Crear elementos del menú
    menu_items = [
        MenuItem(RED, "Opción 1", pygame.Rect(550, 100, 200, 50)),
        MenuItem(GREEN, "Opción 2", pygame.Rect(550, 200, 200, 50)),
        MenuItem(BLUE, "Opción 3", pygame.Rect(550, 300, 200, 50))
    ]
    
    selected_option = None
    
    # Bucle principal
    while True:
        screen.fill(WHITE)  # Limpiar la pantalla
        
        # Manejar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for item in menu_items:
                    if item.position.collidepoint(event.pos):
                        selected_option = item.text
        
        # Dibujar el menú
        for item in menu_items:
            item.draw(screen)
        
        # Dibujar la variable seleccionada
        if selected_option:
            font = pygame.font.Font(None, 48)
            text_surface = font.render("Seleccionado: " + selected_option, True, BLACK)
            text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, 500))
            screen.blit(text_surface, text_rect)
        
        pygame.display.flip()  # Actualizar la pantalla

if __name__ == "__main__":
    main()
