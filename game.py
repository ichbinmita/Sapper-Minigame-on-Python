import pygame
import random

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sapper+")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (144, 238, 144)  # Light green for unrevealed cells
GRAY = (200, 200, 200)   # Gray for revealed cells

# Game grid settings
GRID_SIZE = 40           # Size of each cell in pixels
GRID_WIDTH = 15          # Number of cells horizontally
GRID_HEIGHT = 10         # Number of cells vertically
MINES = 20               # Number of mines to place

# Player and target positions
player_pos = [1 * GRID_SIZE, 1 * GRID_SIZE]  # Start position (top-left corner)
target_pos = [(GRID_WIDTH - 2) * GRID_SIZE, (GRID_HEIGHT - 2) * GRID_SIZE]  # End position (bottom-right corner)

# Initialize game grid and state
grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]  # 2D grid for mine counts
mines_positions = []      # List to store mine positions
revealed = [[False for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]  # Track revealed cells
game_state = "sapper"    # Initial game state ("sapper" or "walking")

# Place mines randomly on the grid
while len(mines_positions) < MINES:
    x = random.randint(1, GRID_WIDTH - 2)
    y = random.randint(1, GRID_HEIGHT - 2)
    # Ensure mines don't spawn on player start, target, or duplicate positions
    if (x, y) not in mines_positions and (x, y) != (1, 1) and (x, y) != (GRID_WIDTH - 2, GRID_HEIGHT - 2):
        mines_positions.append((x, y))
        grid[y][x] = -1  # -1 represents a mine

# Calculate adjacent mine counts for each cell
for y in range(GRID_HEIGHT):
    for x in range(GRID_WIDTH):
        if grid[y][x] == -1:  # Skip mine cells
            continue
        count = 0
        # Check all 8 surrounding cells
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                ny, nx = y + dy, x + dx
                # Only count if within bounds and contains a mine
                if 0 <= ny < GRID_HEIGHT and 0 <= nx < GRID_WIDTH and grid[ny][nx] == -1:
                    count += 1
        grid[y][x] = count  # Store the count of adjacent mines

# Game loop control
running = True
clock = pygame.time.Clock()

def draw_grid():
    """Draw the game grid with revealed/unrevealed cells and mine counts"""
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            
            if revealed[y][x]:  # Cell is revealed
                if grid[y][x] == -1:  # Mine cell
                    pygame.draw.rect(screen, RED, rect)
                else:  # Safe cell
                    pygame.draw.rect(screen, GRAY, rect)
                    # Display mine count if > 0
                    if grid[y][x] > 0:
                        font = pygame.font.SysFont(None, 30)
                        text = font.render(str(grid[y][x]), True, BLACK)
                        screen.blit(text, (x * GRID_SIZE + 15, y * GRID_SIZE + 10))
            else:  # Cell is not revealed
                pygame.draw.rect(screen, GREEN, rect)
            
            # Draw grid lines
            pygame.draw.rect(screen, BLACK, rect, 1)

# Main game loop
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Sapper mode (revealing cells)
        if game_state == "sapper":
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Get clicked cell coordinates
                x, y = event.pos
                grid_x, grid_y = x // GRID_SIZE, y // GRID_SIZE
                
                # Validate coordinates and reveal cell
                if 0 <= grid_x < GRID_WIDTH and 0 <= grid_y < GRID_HEIGHT:
                    revealed[grid_y][grid_x] = True
                    
                    # Check if mine was clicked
                    if grid[grid_y][grid_x] == -1:
                        print("Game Over!")
                        running = False
            
            # Switch to walking mode
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_state = "walking"
        
        # Walking mode (moving player)
        elif game_state == "walking":
            if event.type == pygame.KEYDOWN:
                new_pos = player_pos.copy()  # Calculate new position
                
                # Movement controls
                if event.key == pygame.K_UP:
                    new_pos[1] -= GRID_SIZE
                elif event.key == pygame.K_DOWN:
                    new_pos[1] += GRID_SIZE
                elif event.key == pygame.K_LEFT:
                    new_pos[0] -= GRID_SIZE
                elif event.key == pygame.K_RIGHT:
                    new_pos[0] += GRID_SIZE
                # Switch back to sapper mode
                elif event.key == pygame.K_SPACE:
                    game_state = "sapper"
                
                # Validate movement (only to revealed, safe cells)
                grid_x, grid_y = new_pos[0] // GRID_SIZE, new_pos[1] // GRID_SIZE
                if (0 <= grid_x < GRID_WIDTH and 0 <= grid_y < GRID_HEIGHT and 
                    revealed[grid_y][grid_x] and grid[grid_y][grid_x] != -1):
                    player_pos = new_pos  # Update player position
                
                # Check for win condition (player reached target)
                if player_pos == target_pos:
                    print("You win!")
                    running = False
    
    # Rendering
    screen.fill(BLACK)  # Clear screen
    
    draw_grid()  # Draw the game grid
    
    # Draw target (end position)
    pygame.draw.rect(screen, RED, (target_pos[0], target_pos[1], GRID_SIZE, GRID_SIZE))
    
    # Draw player
    pygame.draw.rect(screen, WHITE, (player_pos[0], player_pos[1], GRID_SIZE, GRID_SIZE))
    
    # Display current game mode
    font = pygame.font.SysFont(None, 24)
    mode_text = "Mode: Sapper (SPACE)" if game_state == "sapper" else "Mode: Walk (SPACE)"
    text = font.render(mode_text, True, WHITE)
    screen.blit(text, (10, HEIGHT - 30))
    
    # Update display
    pygame.display.flip()
    clock.tick(60)  # Cap at 60 FPS

# Clean up
pygame.quit()
