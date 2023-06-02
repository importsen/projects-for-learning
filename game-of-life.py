#TODO
# FIX THIS SHIT. make sure this shit prints correctly, fix copypasta on nvim to make debugging easier on gbt
# add the fancy options
# cry, alot 

import time
import numpy as np

rows = 10
columns = 10

grid = np.zeros((rows, columns), dtype=int)

def update_grid():
    global grid 
    new_grid = grid.copy() 

    for i in range(rows):
        for j in range(columns):
            #calculate the number of neighbors
            neighbors = np.sum(grid[max(0, i-1):min(i+2, rows), max(0, j-1):min(j+2, columns)]) - grid[i, j]

            # apply the rules of the game 
            if grid[i, j] == 1:
                if neighbors < 2 or neighbors > 3:
                    new_grid[i, j] = 0
            else:
                if neighbors == 3:
                    new_grid[i, j] = 1
    
    grid = new_grid

def print_grid():
    for row in grid:
        print(' '.join(["*" if cell == 1 else '.' for cell in row]))

while True:
    user_input = input("Enter the cell coordinates (row column) to toggle (e.g.,2 3). 'exit' to quit: ")
    try:
        row, col = map(int, user_input.split())
        # toggle the cell at the specified coordinates
        grid[row, col] = 1 - grid[row, col] #toggles between 0 and 1 
    except ValueError:
        print("Invalid input! Please enter valid numbers for row and columns.")
    user_input = input("enter commands('/start', '/pause', '/reset'): ")
    if user_input == "/start":
        simulation_running = True
    elif user_input == "/pause":
        simulation_running = False
    elif user_input == "/reset":
        grid = np.zeros((rows, columns), dtype=int)
    else:
        print("Invalid command!")

    if simulation_running:
        update_grid()
        print_grid()

    time.sleep(1)
    # Add an exit condition
    if user_input == "exit":
        break
