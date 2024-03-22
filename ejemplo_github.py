import numpy as np
import pygame

# Inicializar Pygame
pygame.init()

# Definir colores
BLACK = (0, 0, 0)
SAND = (194, 178, 128)

# Configurar la ventana y la matriz
n = 100  # Número de filas
m = 100  # Número de columnas
square_size = 8  # Tamaño del cuadrado en píxeles
width, height = m * square_size, n * square_size
matrix = np.random.randint(0, 2, size=(n, m))  # Matriz aleatoria de 0s y 1s

screen = pygame.display.set_mode((width, height))

# Función para dibujar la pantalla
def draw_screen(matrix):
    for row in range(n):
        for col in range(m):
            color = SAND if matrix[row][col] == 1 else BLACK
            pygame.draw.rect(screen, color, (col * square_size, row * square_size, square_size, square_size))

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for i in range(n-1, -1, -1):  # Iterar desde la fila más baja hasta la más alta
        for j in range(m):
            if matrix[i, j] != 0:    
                if i < n-1:  # Comprueba si la celda no está en el borde inferior de la matriz
                    if matrix[i+1, j] == 0:  # Abajo está libre
                        matrix[i, j] = 0
                        matrix[i+1, j] = 1
                    elif j > 0 and matrix[i+1, j-1] == 0:  # Abajo izquierda está libre
                        matrix[i, j] = 0
                        matrix[i+1, j-1] = 1
                    elif j < m-1 and matrix[i+1, j+1] == 0:  # Abajo derecha está libre
                        matrix[i, j] = 0
                        matrix[i+1, j+1] = 1

    # Limpiar la pantalla
    screen.fill(BLACK)

    # Dibujar la pantalla basada en la matriz
    draw_screen(matrix)

    # Actualizar la pantalla
    pygame.display.flip()

pygame.quit()
