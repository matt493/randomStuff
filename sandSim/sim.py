import pygame

# Define constants
WINDOW_SIZE = (640, 480)
CELL_SIZE = 5
GRID_WIDTH = WINDOW_SIZE[0] // CELL_SIZE
GRID_HEIGHT = WINDOW_SIZE[1] // CELL_SIZE
SAND_COLOR = (255, 255, 0)

# Set up Pygame window
pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()

# Create 2D grid for sand simulation
grid = [[0 for j in range(GRID_HEIGHT)] for i in range(GRID_WIDTH)]

# Define cellular automata rules
def update_sand(grid):
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            if grid[x][y] == 1:
                if y < GRID_HEIGHT - 1 and grid[x][y+1] == 0:
                    grid[x][y] = 0
                    grid[x][y+1] = 1
                elif y < GRID_HEIGHT - 1 and x > 0 and x < GRID_WIDTH - 1 and grid[x-1][y+1] == 0 and grid[x+1][y+1] == 0:
                    grid[x][y] = 0
                    grid[x-1][y+1] = 1
                elif y < GRID_HEIGHT - 1 and x < GRID_WIDTH - 1 and grid[x+1][y+1] == 0 and grid[x][y+1] == 0:
                    grid[x][y] = 0
                    grid[x+1][y+1] = 1
                elif y < GRID_HEIGHT - 1 and x > 0 and grid[x-1][y+1] == 0 and grid[x][y+1] == 0:
                    grid[x][y] = 0
                    grid[x-1][y+1] = 1


# Define function to spawn sand particle at mouse position
def spawn_sand(x, y):
    grid[x // CELL_SIZE][y // CELL_SIZE] = 1

# Pygame main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left click
                spawn_sand(*event.pos)

    # Update sand simulation
    update_sand(grid)

    # Draw sand particles on screen
    screen.fill((0, 0, 0))
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            if grid[x][y] == 1:
                rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, SAND_COLOR, rect)

    # Update display and wait for next frame
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
