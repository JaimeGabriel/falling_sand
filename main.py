import numpy as np
import pygame

# Inicializar Pygame
pygame.init()


# Función para pintar la posición del ratón
def draw_mouse_position():
    mouse_x, mouse_y = pygame.mouse.get_pos()  # Obtener la posición del ratón
    pygame.draw.circle(screen, RED, (mouse_x, mouse_y), 5)  # Dibujar un círculo en la posición del ratón



# Definir colores
BLACK = (0, 0, 0)
SAND = (194, 178, 128)
RED = (255, 0, 0)
WATER = (0, 0, 255)

# Configurar la ventana y la matriz
n = 100  # Número de filas
m = 100  # Número de columnas
square_size = 8  # Tamaño del cuadrado en píxeles
width, height = m * square_size, n * square_size
#matrix = np.random.randint(0, 3, size=(n, m))  # Matriz aleatoria de 0s y 1s
matrix = np.zeros((n, m))  # Matriz aleatoria de 0s y 1s


screen = pygame.display.set_mode((width, height))

# Función para dibujar la pantalla
def draw_screen(matrix):
    for row in range(n):
        for col in range(m):
            #color = SAND if matrix[row][col] == 1 else WATER if matrix[row][col] == 1 else BLACK
            color = SAND if matrix[row][col] == 1 else WATER if matrix[row][col] == 2 else BLACK
            pygame.draw.rect(screen, color, (col * square_size, row * square_size, square_size, square_size))


# Crear un objeto Clock para controlar la velocidad de los fotogramas
clock = pygame.time.Clock()


run = True
generadores = []
frame_count = 0

while run:

    # Limitar la velocidad de los fotogramas a 60 por segundo
    clock.tick(60)
    pygame.display.set_caption("Falling Sand - FPS: {}".format(int(clock.get_fps())))


    # Verificar el estado del botón izquierdo del ratón
    mouse_buttons = pygame.mouse.get_pressed()
    left_mouse_button_pressed = mouse_buttons[0]  # Índice 0 para el botón izquierdo del ratón


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if left_mouse_button_pressed:  # Verificar si se ha pulsado el botón izquierdo del ratón
                    mouse_x, mouse_y = event.pos  # Obtener la posición del ratón
                    # print("Posición del ratón (x, y):", mouse_x, ",", mouse_y)
                    celda_j = int(np.floor(mouse_x/square_size))
                    celda_i = int(np.floor(mouse_y/square_size))
                    print(f"Se ha pulsado la celda ({celda_i}, {celda_j})")
                    
                    if matrix[celda_i, celda_j] == 0:
                        matrix[celda_i, celda_j] = 1
        

        # Verificar si se ha pulsado el botón izquierdo del ratón
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:  # El botón izquierdo del ratón tiene el código 1
                print("Se ha pulsado el botón der del ratón")
                mouse_x, mouse_y = event.pos  # Obtener la posición del ratón
                celda_j = int(np.floor(mouse_x/square_size))
                celda_i = int(np.floor(mouse_y/square_size))
                generadores.append([celda_i, celda_j])

        # Verificar si se ha pulsado la tecla D
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d and len(generadores) != 0:
                print("Se ha pulsado la tecla D")
                generadores.pop()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                mouse_x, mouse_y = pygame.mouse.get_pos()  # Obtener la posición del ratón
                # print("Posición del ratón (x, y):", mouse_x, ",", mouse_y)
                celda_j = int(np.floor(mouse_x/square_size))
                celda_i = int(np.floor(mouse_y/square_size))
                print(f"Agua")
                
                if matrix[celda_i, celda_j] == 0:
                    matrix[celda_i, celda_j] = 2

            



    if frame_count % 5 == 0:
        for coords in generadores:
            matrix[coords[0], coords[1]] = 1
    
    if frame_count > 1000:
        frame_count = 0

    frame_count += 1

    if frame_count%2 == 0:
        for i in range(n-1, -1, -1):
            for j in range(m):
                if matrix[i, j] == 1:
                    if i < n-1: # La celda no está en el borde inferior de la pantalla
                        if matrix[i+1, j] == 0: # Abajo libre 
                            matrix[i, j] = 0
                            matrix[i+1, j] = 1

                        elif j > 0 and matrix[i+1, j-1] == 0: # Abajo izquierda libre
                            matrix[i, j] = 0
                            matrix[i+1, j-1] = 1

                        elif j < m-1 and matrix[i+1, j+1] == 0: # Abajo derecha libre
                            matrix[i, j] = 0
                            matrix[i+1, j+1] = 1

                if matrix[i, j] == 2:
                    if i < n-1: # La celda no está en el borde inferior de la pantalla
                        if matrix[i+1, j] == 0: # Abajo libre 
                            matrix[i, j] = 0
                            matrix[i+1, j] = 2

                        elif j > 0 and matrix[i+1, j-1] == 0: # Abajo izquierda libre
                            matrix[i, j] = 0
                            matrix[i+1, j-1] = 2

                        elif j < m-1 and matrix[i+1, j+1] == 0: # Abajo derecha libre
                            matrix[i, j] = 0
                            matrix[i+1, j+1] = 2 

                        elif j > 0 and j < m-1 and matrix[i+1, j-1] != 0 and matrix[i+1, j+1] != 0 and matrix[i, j-1] == 0:
                            rand = np.random.uniform(0, 1)
                            matrix[i, j] = 0
                            if rand > 0.5:
                                matrix[i, j-1] = 2
                            else:
                                matrix[i, j+1] = 2


    """ 
    for i in range(n-1, -1, -1):
        for j in range(m):
            if matrix[i, j] != 2:
                if i < n-1: # La celda no está en el borde inferior de la pantalla
                    if matrix[i+1, j] == 0: # Abajo libre 
                        matrix[i, j] = 0
                        matrix[i+1, j] = 2

                    elif j > 0 and matrix[i+1, j-1] == 0: # Abajo izquierda libre
                        matrix[i, j] = 0
                        matrix[i+1, j-1] = 2

                    elif j < m-1 and matrix[i+1, j+1] == 0: # Abajo derecha libre
                        matrix[i, j] = 0
                        matrix[i+1, j+1] = 2 
    """



    # Limpiar la pantalla
    screen.fill(BLACK)

    # Dibujar la pantalla basada en la matriz
    draw_screen(matrix)

    # Dibujar la posición del ratón
    draw_mouse_position()

    # Actualizar la pantalla
    pygame.display.flip()

pygame.quit()
