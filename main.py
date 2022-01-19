import pygame
from grid import *
from cell import *

pygame.init()

APP_WIDTH, APP_HEIGHT = 900, 900

WIN = pygame.display.set_mode((APP_WIDTH, APP_HEIGHT))
pygame.display.set_caption('Conway\'s Game Of Life')
FPS = 30

SIZE = 75

def draw_window(grid:Grid) -> None:
    grid.Conway()
    
    pygame.display.update() # updates the display after having drawn the window.
    
def main() -> None:
    run = True
    clock = pygame.time.Clock()
    
    grid = Grid(WIN, SIZE, SIZE)
    grid.starting_grid() 
    
    paused = False

    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get(): # returns a list of all pygame events
            
            # Quits the game
            if event.type == pygame.QUIT:
                run = False
                
            # Handles the key events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not paused:
                    grid = Grid(WIN, SIZE, SIZE)
                    grid.starting_grid()
                
                if event.key == pygame.K_p and not paused:
                    paused = True
                    
                elif event.key == pygame.K_p and paused:
                    paused = False
            
            # Handles the mouse events
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                grid.animate_cell(position)
        
        if not paused:
            draw_window(grid)
    
    pygame.quit()
        
    
if __name__ == '__main__':
    main() 