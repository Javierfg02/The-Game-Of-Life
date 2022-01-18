import pygame
from cell import *
import numpy as np
import random

pygame.init()

DEAD = 0
ALIVE = 1

# This class handles the functionality of the grid where Life occurs.
class Grid:
    
    def __init__(self, surface:pygame.Surface, rows:int, cols:int):
        self.surface = surface
        self.rows = rows
        self.cols = cols
        
        self.cell_width = self.surface.get_width()/self.cols
        self.cell_height = self.surface.get_height()/self.rows
        
        self.grid = np.ndarray(shape=(self.rows, self.cols), dtype=Cell) # 2D array which represents our grid
        
    def starting_grid(self) -> None:
        for x in range(self.rows):
            for y in range(self.cols):
                self.grid[x][y] = Cell(self.surface, x, y, self.cell_width, self.cell_height, random.randint(0, 1))
    
    def copy_grid(self) -> np.ndarray:
        grid = np.ndarray(shape=(self.rows, self.cols), dtype=Cell)
        for x in range(self.rows):
            for y in range(self.cols):
                grid[x][y] = self.grid[x][y]
        return grid
        
    def count_neighbours(self, grid:np.ndarray, x:int, y:int) -> int:
        total = 0 # this variable is used to sum up the states of the neighbouring cells
        for dx in range(-1, 2, 1):
            for dy in range(-1, 2, 1):
                adj_x = (x + dx + self.rows) % self.rows
                adj_y = (y + dy + self.cols) % self.cols
                total += grid[adj_x][adj_y].state 
        
        total -= grid[x][y].state # We want to substract the state of the cell that we are checking            
        return total

    def Conway(self) -> None:
        # Make a copy of the grid 
        copy_grid = self.copy_grid() # Now this grid is an exact copy of the current grid
        for x in range(self.rows):
            for y in range(self.cols):
                neighbours = self.count_neighbours(copy_grid, x, y)
                state = copy_grid[x][y].state
                # Rule 1: if there are three live neighouring cells, then the cell becomes alive as if by reproduction:
                if neighbours == 3 and state == DEAD:
                    self.grid[x][y].set_state(ALIVE) 
                    # print("self grid state: " + str(self.grid[x][y].state))
                    # print("copy_grid state: "  + str(copy_grid[x][y].state))
                    self.grid[x][y].draw_cell()
                    # print("new live cell at: " + str(x) + ", " + str(y))
                    
                # Rule 2: if there are less than 2 live neighbours then the cell dies as if by underpopulation and 
                # Rule 3: if ther are more than 3 live neighbours then the cell dies as if by overpopulation:
                elif (neighbours < 2 or neighbours > 3) and state == ALIVE:
                    self.grid[x][y].set_state(DEAD)
                    self.grid[x][y].draw_cell()
                    # print("dead by underpopulation")
                
                else:
                    self.grid[x][y].set_state(state)
                    # print("cell dies by overpopulation at: " + str(x) + ", " + str(y))
                
                # Rule §4: any live cell with 2 or 3 neighbours lives on to the next generation (no need to code)       