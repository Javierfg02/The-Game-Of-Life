from re import S
import pygame

pygame.init() 

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Cell:
    def __init__(self, surface:pygame.Surface, x:int, y:int, width:int, height:int, state:int):
        self.surface = surface
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.state = state
        
        self.draw_cell()
        
    def draw_cell(self) -> None:
        if self.state == 0: # if the cell is dead
            color = BLACK
        else:
            color = WHITE
        
        cell = pygame.Rect(self.x*self.width, self.y*self.height, self.width-1, self.height-1)
            
        pygame.draw.rect(self.surface, color, cell)