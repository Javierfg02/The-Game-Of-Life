import pygame
from grid import *
from cell import *

pygame.init()

APP_WIDTH, APP_HEIGHT = 900, 900

WIN = pygame.display.set_mode((APP_WIDTH, APP_HEIGHT))
pygame.display.set_caption('Conway\'s Game Of Life')
FPS = 30

def draw_window(grid:Grid) -> None:
    grid.Conway()
    
    pygame.display.update() # updates the display after having drawn the window.
    
def main() -> None:
    run = True
    clock = pygame.time.Clock()
    
    grid = Grid(WIN, 100, 100)
    grid.starting_grid() 

    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get(): # returns a list of all pygame events
            
            if event.type == pygame.QUIT:
                run = False
            
        draw_window(grid)
        
    pygame.quit()
    
if __name__ == '__main__':
    main() 