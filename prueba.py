import pygame
import numpy as np
import sys

# Inicializar Pygame
pygame.init()

# Configurar la ventana y la matriz
n = 5  # Número de filas
m = 5  # Número de columnas
square_size = 50  # Tamaño del cuadrado en píxeles
width, height = m * square_size, n * square_size
matrix = np.random.randint(0, 2, size=(n, m))  # Matriz aleatoria de 0s y 1s

# Definir colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Crear la ventana
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Representación de pantalla con matriz")

# Función para dibujar la pantalla
def draw_screen(matrix):
    for row in range(n):
        for col in range(m):
            color = WHITE if matrix[row][col] == 1 else BLACK
            pygame.draw.rect(screen, color, (col * square_size, row * square_size, square_size, square_size))

# Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Limpiar la pantalla
    screen.fill(BLACK)

    # Dibujar la pantalla basada en la matriz
    draw_screen(matrix)

    # Actualizar la pantalla
    pygame.display.flip()