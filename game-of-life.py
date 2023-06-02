#TODO
# FIX THIS SHIT. make sure this shit prints correctly, fix copypasta on nvim to make debugging easier on gbt
# add the fancy options
# cry, alot 

import time
import numpy as np

# constants for grid size
rows = 10
columns = 10

# create an empty grid
grid = np.zeros((rows, columns), dtype=int)

# simulation state
simulation_running = False

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

def toggle_cell(row, col):
    # toggle the cell at specified coordinates
    grid[row, col] = 1 - grid[row, col] # toggles between 0 and 1

def handle_user_input():
    while True:
        user_input = input("Enter the cell coordinates (row columns) to toggle (e.g.,2 3). 'exit' to quit: ")
        if user_input == "exit":
            break
        try:
            row, col = map(int, user_input.split())
            if 0 <= row < rows and 0 <= col < columns:
                toggle_cell(row, col)
            else:
                print("Invalid input! Please enter valid coordinates withinthe grid range")
        except ValueError:
            print("Invalid input! Please enter valid numbers for row and columns.")

        user_command= input("Enter a command ('start, 'pause', 'reset'): ")
        if user_command == "start":
            global simulation_running
            simulation_running = True
        elif user_command == "pause":
            simulation_running = False
        elif user_command == "reset":
            global grid
            grid = np.zeros((rows, columns), dtype=int)
        else:
            print("Invalid command!")

        if simulation_running:
            update_grid()
        
        print_grid()

        time.sleep(1)

# print the initial grid
print_grid()

# start the simulation
handle_user_input()
