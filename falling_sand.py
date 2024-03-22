import numpy as np
import pygame


n = 100 # Rows of the matrix
m = 100 # Columns of the matrix
square_size = 8 # Number of pixel of the cells
width, height = m * square_size, n * square_size # Number of pixels of the game window
#matrix = np.random.randint(0, 3, size=(n, m))  # 
matrix = np.zeros((n, m)) 

BLACK = (0, 0, 0)
SAND = (194, 178, 128)
RED = (255, 0, 0)
WATER = (0, 0, 255)
WHITE = (255, 255, 255)



def draw_mouse_position():
    '''
    Function that gets and draws the position of the mouse at all time.
    '''
    mouse_x, mouse_y = pygame.mouse.get_pos()
    pygame.draw.circle(screen, RED, (mouse_x, mouse_y), 5) 


def draw_screen(matrix):
    '''
    Function that draw the screen from the matrix of integers.
    '''
    for row in range(n):

        for col in range(m):
            color = SAND if matrix[row][col] == 1 else WATER if matrix[row][col] == 2 else BLACK
            pygame.draw.rect(screen, color, (col * square_size, row * square_size, square_size, square_size))


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


menu_items = [
    MenuItem(1, SAND, 'Sand', pygame.Rect(550, 100, 200, 50)),
    MenuItem(2, WATER, 'Water', pygame.Rect(550, 200, 200, 50)),
    MenuItem(0, WHITE, 'Delete', pygame.Rect(550, 300, 200, 50))
]

selected_material = 1


pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock() # For controlling the fps

generators = []
frame_count = 0

run = True

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
            for item in menu_items:
                if item.position.collidepoint(event.pos):
                    selected_material = item.value

        if is_left_mouse_button_pressed(): # Left mouse button
            '''
            Left mouse button to create a block.
            ''' 
            mouse_x, mouse_y = event.pos 
            # print("Posición del ratón (x, y):", mouse_x, ",", mouse_y)
            cell_j = int(np.floor(mouse_x/square_size))
            cell_i = int(np.floor(mouse_y/square_size))
            print(f"Se ha pulsado la celda ({cell_i}, {cell_j})")
            
            matrix[cell_i, cell_j] = selected_material

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
        
    if frame_count % 5 == 0:
        ''''
        Velocity of the generators
        '''
        for coords in generators:
            matrix[coords[0], coords[1]] = coords[2]
    
    if frame_count > 1000:
        frame_count = 0
    frame_count += 1

    
    for i in range(n-1, -1, -1):
        for j in range(m):
            if matrix[i, j] == 1: # Sand
                if i < n-1: # The cell is not at the bottom border
                    if matrix[i+1, j] == 0: # Down free
                        matrix[i, j] = 0
                        matrix[i+1, j] = 1

                    elif j > 0 and matrix[i+1, j-1] == 0: # Down left free
                        matrix[i, j] = 0
                        matrix[i+1, j-1] = 1

                    elif j < m-1 and matrix[i+1, j+1] == 0: # Down right free
                        matrix[i, j] = 0
                        matrix[i+1, j+1] = 1

            if matrix[i, j] == 2: # Water
                if i < n-1: # The cell is not at the bottom border
                    if matrix[i+1, j] == 0: # Abajo libre 
                        matrix[i, j] = 0
                        matrix[i+1, j] = 2

                    elif j > 0 and matrix[i+1, j-1] == 0: # Down left free
                        matrix[i, j] = 0
                        matrix[i+1, j-1] = 1

                    elif j < m-1 and matrix[i+1, j+1] == 0: # Down right free
                        matrix[i, j] = 0
                        matrix[i+1, j+1] = 1

                    """ elif j > 0 and matrix[i, j-1] == 0: # Left free
                        matrix[i, j] = 0
                        matrix[i, j-1] = 2

                    elif j < m-1 and matrix[i, j+1] == 0: # Right free
                        matrix[i, j] = 0
                        matrix[i+1, j+1] = 2 """

                    """ elif j < m - 1: 
                        rand = np.random.uniform(0, 1)
                        matrix[i, j] = 0
                        if rand > 0.5:
                            matrix[i, j-1] = 2
                        else:
                            matrix[i, j+1] = 2 """


                """ else:
                    if j > 0 and j < m - 1 and matrix[i, j-1] == 0 and matrix[i, j+1] == 0:
                        rand = np.random.uniform(0, 1)
                        if rand < 0.5:
                            matrix[i, j] = 0
                            matrix[i, j-1] = 2
                        else:
                            matrix[i, j] = 0
                            matrix[i, j+1] = 2 

                    if j > 0 and matrix[i, j-1] == 0: 
                        matrix[i, j] = 0
                        matrix[i, j-1] = 2

                    if j < m-1 and matrix[i, j+1] == 0: 
                        matrix[i, j] = 0
                        matrix[i, j+1] = 2  """

                """ elif j > 0 and j < m-1 and matrix[i+1, j-1] != 0 and matrix[i+1, j+1] != 0 and matrix[i, j-1] == 0:
                        rand = np.random.uniform(0, 1)
                        matrix[i, j] = 0
                        if rand > 0.5:
                            matrix[i, j-1] = 2
                        else:
                            matrix[i, j+1] = 2 """

    # Clean screen
    screen.fill(BLACK)

    # Draw screen with the info of the matrix
    draw_screen(matrix)

    # Draw th mouse position
    draw_mouse_position()

    # Draw the right menu
    for item in menu_items:
        item.draw_menu(screen)

    # Update screen
    pygame.display.flip()

pygame.quit()