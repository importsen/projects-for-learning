import pygame
import numpy as np

# pygame initilaization
pygame.init()

# screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

# Colors

WHITE = (255, 255, 255)
BLACK = (0, 0,  0)

# Cell dimensions
CELL_SIZE = 10

# create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Cell:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
        self.alive = False

    def draw(self):
        color = WHITE if self.alive else BLACK
        pygame.draw.rect(screen, color, self.rect)

class GameOfLife:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.grid = [[Cell(x*CELL_SIZE, y*CELL_SIZE) for x in range(columns)] for y in range(rows)]
        self.simulation_running = False

    def update_grid(self):
        new_grid = self.grid.copy()
        for i in range(self.rows):
            for j in range(self.columns):
                #calculate the number of neighbors
                neighbors = np.sum([self.grid[x][y].alive for x in range(max(0, i-1), min(i+2, self.rows)) for y in range(max(0, j-1), min(j+2, self.columns))]) - self.grid[i][j].alive
                # apply the rules of the game
                if self.grid[i][j].alive:
                    if neighbors < 2 or neighbors > 3:
                        new_grid[i][j].alive = False
                else:
                    if neighbors == 3:
                        new_grid[i][j].alive = True

        self.grid = new_grid

    def draw(self):
        for row in self.grid:
            for cell in row:
                cell.draw()

# main loop

game = GameOfLife(SCREEN_HEIGHT // CELL_SIZE, SCREEN_HEIGHT // CELL_SIZE)
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            game.grid[y // CELL_SIZE][x // CELL_SIZE].alive = not game.grid[y // CELL_SIZE][x // CELL_SIZE].alive
        elif event.type== pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game.simulation_running = not game.simulation_running
            elif event.key == pygame.K_r:
                game.grid = [[Cell(x*CELL_SIZE, y*CELL_SIZE) for x in range(game.columns)] for y in range(game.rows)]

    if game.simulation_running:
        game.update_grid()

    screen.fill(BLACK)
    game.draw()
    pygame.display.flip()
    clock.tick(10)
