import copy
import os
import time
from colorama import Fore, Style, init

init(autoreset=True)

def initialize_grid(rows, cols):
    return [[' ' for _ in range(cols)] for _ in range(rows)]

def print_grid(grid):
    for row in grid:
        for cell in row:
            if cell == '#':
                print(Fore.GREEN + cell, end=' ')
            else:
                print(Fore.WHITE + cell, end=' ')
        print()
    print()

def count_neighbors(grid, x, y):
    neighbors = 0
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == '#':
            neighbors += 1

    return neighbors

def update_grid(grid):
    new_grid = copy.deepcopy(grid)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            neighbors = count_neighbors(grid, i, j)

            if grid[i][j] == ' ' and neighbors == 3:
                new_grid[i][j] = '#'
            elif grid[i][j] == '#' and (neighbors < 2 or neighbors > 3):
                new_grid[i][j] = ' '
    
    return new_grid

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def main(rows, cols, generations):
    grid = initialize_grid(rows, cols)

    
    grid[1][2] = '#'
    grid[2][3] = '#'
    grid[3][1] = '#'
    grid[3][2] = '#'
    grid[3][3] = '#'

    for _ in range(generations):
        clear_console()
        print_grid(grid)
        time.sleep(0.5)  
        grid = update_grid(grid)

if __name__ == "__main__":
    rows = 10
    cols = 10
    generations = 20
    main(rows, cols, generations)

