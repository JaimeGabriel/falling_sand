import numpy as np
import pygame
from menu import *
from globals import *
from used_functions import *




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
    MenuItem(50, WHITE, '50', pygame.Rect(width - brush_size_item_menu_width*1.5, material_item_menu_height*5.5, brush_size_item_menu_width, brush_size_item_menu_width))
]



pygame.init()
clock = pygame.time.Clock() # For controlling the fps


# Constants that can change when the game is running
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
            '''
            Check is the material menu was clicked
            '''
            for item in material_menu_items:
                if item.position.collidepoint(event.pos):
                    selected_material = item.value
                    item.set_pressed_color()

        if event.type == pygame.MOUSEBUTTONDOWN:
            '''
            Check is the brush size menu was clicked
            '''
            for item in brush_size_menu_items:
                if item.position.collidepoint(event.pos):
                    brush_size = item.value
                    item.set_pressed_color()

        if event.type == pygame.MOUSEBUTTONUP:
            '''
            If the mouse button is no longer pressed, the color of the menu goes back to normal
            '''
            for item in material_menu_items + brush_size_menu_items:
                item.reset_color()

        if is_left_mouse_button_pressed()and not any(item.position.collidepoint(pygame.mouse.get_pos()) for item in material_menu_items + brush_size_menu_items): # Left mouse button pressed outside the menu
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



        keys = pygame.key.get_pressed()

        if event.type == pygame.KEYDOWN:
            '''
            D key to eliminate the last generator created.
            ''' 
            if event.key == pygame.K_d and len(generators) != 0:
                generators.pop()

            if event.key == pygame.K_SPACE:
                paused = not paused

            if event.key == pygame.K_v:
                matrix = np.flip(np.flip(matrix, axis=1), axis=0)

            if event.key == pygame.K_m:
                draw_mouse = not draw_mouse

            if keys[pygame.K_d] and keys[pygame.K_LCTRL]:
                matrix = np.zeros((n, m))
        
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

                        elif j > 0 and i < n - 2 and matrix[i+1, j-1] == 0 and matrix[i+1, j+1] == 0: # Botton left and right free
                            matrix[i, j] = 0
                            if np.random.uniform(0, 1) > 0.5:
                                matrix[i+1, j-1] = 1
                            else: 
                                matrix[i+1, j+1] = 1

                        elif j < m-1 and matrix[i+1, j+1] == 0: # Bottom right free
                            matrix[i, j] = 0
                            matrix[i+1, j+1] = 1

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
                    if i < n-1 and matrix[i+1, j] == 0: # Bottom free 
                        matrix[i, j] = 0
                        matrix[i+1, j] = 2

                    elif i < n-1 and j > 0 and matrix[i+1, j-1] == 0: # Bottom left free
                        matrix[i, j] = 0
                        matrix[i+1, j-1] = 2

                    elif i < n-1 and j < m-1 and matrix[i+1, j+1] == 0: # Botton right free
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
        # Show 'Game is paused' message
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