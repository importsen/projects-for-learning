import time
import numpy as np

class GameOfLife:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.grid = np.zeros((rows, columns), dtype=int)
        self.simulation_running = False

    def update_grid(self):
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

    def toggle_cell(self, row, col):
        # toggle the cell at specified coordinates
        self.grid[row, col] = 1 - self.grid[row, col] # toggles between 0 and 1
    
    def print_grid(self):
        for row in self.grid:
            print(' '.join(["*" if cell == 1 else "." for cell in row]))

    def handle_user_input():
        while True:
            user_input = input("Enter the cell coordinates (row columns) to toggle (e.g.,2 3). 'exit' to quit: ")
            if user_input == "exit":
                break

            try:
                row, col = map(int, user_input.split())
                if 0 <= row < rows and 0 <= col < columns:
                    self.toggle_cell(row, col)
                else:
                    print("Invalid input! Please enter valid coordinates withinthe grid range")
            except ValueError:
                print("Invalid input! Please enter valid numbers for row and columns.")

            user_command= input("Enter a command ('start, 'pause', 'reset'): ")
            if user_command == "start":
                simulation_running = True
            elif user_command == "pause":
                simulation_running = False
            elif user_command == "reset":
                self.grid = np.zeros((self.rows, self.columns), dtype=int)
            else:
                print("Invalid command!")

            if self.simulation_running:
                self.update_grid()
        
            self.print_grid()

            time.sleep(1)

# constants for grid size
rows = 10
columns = 10

#create the game of life instance
game = GameOfLife(rows, columns)

# print the initial grid
game.print_grid()

# start the simulation
game.handle_user_input()
