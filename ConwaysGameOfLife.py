import time
import random
import os

def create_grid(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]

def randomize_grid(grid, density=0.3):
    rows = len(grid)
    cols = len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if random.random() < density:
                grid[i][j] = 1

def get_neighbors(grid, row, col):
    rows = len(grid)
    cols = len(grid[0])
    live_neighbors = 0
    for i in range(max(0, row - 1), min(rows, row + 2)):
        for j in range(max(0, col - 1), min(cols, col + 2)):
            if (i, j) != (row, col) and grid[i][j] == 1:
                live_neighbors += 1
    return live_neighbors

def next_generation(grid):
    rows = len(grid)
    cols = len(grid[0])
    new_grid = create_grid(rows, cols)
    for i in range(rows):
        for j in range(cols):
            live_neighbors = get_neighbors(grid, i, j)
            if grid[i][j] == 1: 
                if live_neighbors == 2 or live_neighbors == 3:
                    new_grid[i][j] = 1  
            else: 
                if live_neighbors == 3:
                    new_grid[i][j] = 1  
    return new_grid

def print_grid(grid):
    os.system('cls' if os.name == 'nt' else 'clear')  
    for row in grid:
        print(''.join(['*' if cell == 1 else ' ' for cell in row]))

if __name__ == "__main__":
    print(' Name: Rahul G \n USN: 1AY24AI088 \n Section: O')
    rows = 20
    cols = 40
    generations = 10
    update_interval = 0.2 

    grid = create_grid(rows, cols)
    randomize_grid(grid, density=0.2) 

    for generation in range(generations):
        print(f"Generation: {generation + 1}")
        print_grid(grid)
        grid = next_generation(grid)
        time.sleep(update_interval)

    print("Game of Life simulation ended.")
