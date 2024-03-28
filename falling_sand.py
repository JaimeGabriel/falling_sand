import numpy as np
import pygame


n = 100 # Rows of the matrix
m = 100 # Columns of the matrix
square_size = 8 # Number of pixel for a cell
width, height = m * square_size, n * square_size # Number of pixels of the game window
#matrix = np.random.randint(0, 3, size=(n, m))  # 
matrix = np.zeros((n, m)) 

BLACK = (0, 0, 0)
SAND = (194, 178, 128)
RED = (255, 0, 0)
WATER = (0, 0, 255)
ROCK = (128, 128, 128)
WHITE = (255, 255, 255)



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


class MenuItem:
    def __init__(self, value, color, text, position):
        self.value = value
        self.color = color
        self.text = text
        self.position = position

    def draw_menu(self, surface):
        pygame.draw.rect(surface, self.color, self.position)  
        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.position.center)
        surface.blit(text_surface, text_rect)


material_item_menu_width = 100
material_item_menu_height = 50
brush_size_item_menu_width = 30
brush_size_item_menu_width = 30

material_menu_items = [
    MenuItem(1, SAND, 'Sand', pygame.Rect(width - material_item_menu_width*1.5, material_item_menu_height*1.5, material_item_menu_width, material_item_menu_height)),
    MenuItem(2, WATER, 'Water', pygame.Rect(width - material_item_menu_width*1.5, material_item_menu_height*3, material_item_menu_width, material_item_menu_height)),
    MenuItem(3, ROCK, 'Rock', pygame.Rect(width - material_item_menu_width*1.5, material_item_menu_height*4.5, material_item_menu_width, material_item_menu_height)),
    MenuItem(0, WHITE, 'Delete', pygame.Rect(width - material_item_menu_width*1.5, material_item_menu_height*6, material_item_menu_width, material_item_menu_height)),  
]

brush_size_menu_items = [
    MenuItem(1, WHITE, '1', pygame.Rect(width - brush_size_item_menu_width*1.5, material_item_menu_height*1.5, brush_size_item_menu_width, brush_size_item_menu_width)),
    MenuItem(2, WHITE, '2', pygame.Rect(width - brush_size_item_menu_width*1.5, material_item_menu_height*2.5, brush_size_item_menu_width, brush_size_item_menu_width)),
    MenuItem(5, WHITE, '5', pygame.Rect(width - brush_size_item_menu_width*1.5, material_item_menu_height*3.5, brush_size_item_menu_width, brush_size_item_menu_width)),
    MenuItem(10, WHITE, '10', pygame.Rect(width - brush_size_item_menu_width*1.5, material_item_menu_height*4.5, brush_size_item_menu_width, brush_size_item_menu_width)),
    MenuItem(50, WHITE, '50', pygame.Rect(width - brush_size_item_menu_width*1.5, material_item_menu_height*5.5, brush_size_item_menu_width, brush_size_item_menu_width)),
    MenuItem(100, WHITE, '100', pygame.Rect(width - brush_size_item_menu_width*1.5, material_item_menu_height*6.5, brush_size_item_menu_width, brush_size_item_menu_width))
]

selected_material = 1
brush_size = 1

pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock() # For controlling the fps

generators = []
frame_count = 0

run = True
paused = False
draw_mouse = False

while run:

    clock.tick(60)
    pygame.display.set_caption("Falling Sand - FPS: {}".format(int(clock.get_fps())))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            '''
            Quit the game.
            '''
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            for item in material_menu_items:
                if item.position.collidepoint(event.pos):
                    selected_material = item.value

        if event.type == pygame.MOUSEBUTTONDOWN:
            for item in brush_size_menu_items:
                if item.position.collidepoint(event.pos):
                    brush_size = item.value

        if is_left_mouse_button_pressed(): # Left mouse button
            '''
            Left mouse button to create a block.
            ''' 
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # print("Posición del ratón (x, y):", mouse_x, ",", mouse_y)
            cell_j = int(np.floor(mouse_x/square_size))
            cell_i = int(np.floor(mouse_y/square_size))
            # print(f"Se ha pulsado la celda ({cell_i}, {cell_j})")

            if brush_size == 1:
                matrix[cell_i, cell_j] = selected_material
            else:
                for i in range(cell_i - brush_size, cell_i + brush_size):
                    for j in range(cell_j - brush_size, cell_j + brush_size):
                        if i > 0 and i < n and j > 0 and j < m and np.random.uniform(0, 1) > 0.80:
                            matrix[i, j] = selected_material


        if event.type == pygame.MOUSEBUTTONDOWN:
            '''
            Right mouse button to create a generator block.
            ''' 
            if event.button == 3:  
                #print("Se ha pulsado el botón der del ratón")
                mouse_x, mouse_y = event.pos  
                cell_j = int(np.floor(mouse_x/square_size))
                cell_i = int(np.floor(mouse_y/square_size))
                generators.append([cell_i, cell_j, selected_material])   

        if event.type == pygame.KEYDOWN:
            '''
            D key to eliminate the last generator created.
            ''' 
            if event.key == pygame.K_d and len(generators) != 0:
                print("Se ha pulsado la tecla D")
                generators.pop()

            if event.key == pygame.K_SPACE:
                paused = not paused

            if event.key == pygame.K_v:
                matrix = np.flip(np.flip(matrix, axis=1), axis=0)

            if event.key == pygame.K_m:
                draw_mouse = not draw_mouse
        
    if frame_count % 5 == 0:
        ''''
        Velocity of the generators
        '''
        for coords in generators:
            matrix[coords[0], coords[1]] = coords[2]
    
    if frame_count > 1000:
        frame_count = 0
    frame_count += 1


    
    
    if not paused:
        for i in range(n-1, -1, -1): # from n - 1 to 0
            for j in random_index(m): # from 0 to m - 1, but unordered, to avoid the deviation of the water
                if matrix[i, j] == 1: # Sand
                    if i < n-1: # The cell is not at the bottom border
                        if matrix[i+1, j] == 0: # Bottom free
                            matrix[i, j] = 0
                            matrix[i+1, j] = 1

                        elif j > 0 and matrix[i+1, j-1] == 0: # Botton left free
                            matrix[i, j] = 0
                            matrix[i+1, j-1] = 1

                        elif j < m-1 and matrix[i+1, j+1] == 0: # Bottom right free
                            matrix[i, j] = 0
                            matrix[i+1, j+1] = 1

                        # Interaction with water
                        elif matrix[i+1, j] == 2 and frame_count%3 == 0: # Bottom has water
                            matrix[i, j] = 2
                            matrix[i+1, j] = 1


                if matrix[i, j] == 2: # Water
                    if i < n-1: # The cell is not at the bottom border
                        if matrix[i+1, j] == 0: # Bottom free 
                            matrix[i, j] = 0
                            matrix[i+1, j] = 2

                        elif j > 0 and matrix[i+1, j-1] == 0: # Bottom left free
                            matrix[i, j] = 0
                            matrix[i+1, j-1] = 2

                        elif j < m-1 and matrix[i+1, j+1] == 0: # Botton right free
                            matrix[i, j] = 0
                            matrix[i+1, j+1] = 2

                        elif j > 0 and j < m-1 and matrix[i, j-1] == 0 and matrix[i, j+1] == 0: # Bottom occupied and both sides free
                            matrix[i, j] = 0
                            rand = np.random.choice([1, -1])
                            matrix[i, j+rand] = 2

                        elif j > 0 and j < m-1 and matrix[i, j+1] == 0: # Bottom occupied and right free
                            matrix[i, j] = 0
                            matrix[i, j+1] = 2

                        elif j > 0 and j < m-1 and matrix[i, j-1] == 0: # Bottom occupied and left free
                            matrix[i, j] = 0
                            matrix[i, j-1] = 2
                    

                    
    # Clean screen
    screen.fill(BLACK)

    # Draw screen with the info of the matrix
    draw_screen(matrix)

    if paused:
        # Mostrar un mensaje de pausa en la pantalla si está pausado
        font = pygame.font.Font(None, 36)
        text = font.render("JUEGO EN PAUSA", True, WHITE)
        text_rect = text.get_rect(center=(width // 2, height * 0.1))
        screen.blit(text, text_rect)

    # Draw th mouse position
    if draw_mouse == True:
        draw_mouse_position()

    # Draw the right menu
    for item in material_menu_items:
        item.draw_menu(screen)

    for item in brush_size_menu_items:
        item.draw_menu(screen)


    # Update screen
    pygame.display.flip()

pygame.quit()