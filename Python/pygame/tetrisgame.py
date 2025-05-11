import pygame
import random

# Initialize Pygame
pygame.init()

# --- Game Constants ---
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30  # Size of each Tetris block
BOARD_WIDTH = 10  # Number of blocks wide
BOARD_HEIGHT = 20 # Number of blocks tall

# Calculate board pixel dimensions
BOARD_PIXEL_WIDTH = BOARD_WIDTH * BLOCK_SIZE
BOARD_PIXEL_HEIGHT = BOARD_HEIGHT * BLOCK_SIZE

# Board position (centered horizontally)
BOARD_POS_X = (SCREEN_WIDTH - BOARD_PIXEL_WIDTH) // 2
BOARD_POS_Y = SCREEN_HEIGHT - BOARD_PIXEL_HEIGHT - 20 # Add some space at the bottom

# Colors (RGB)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
COLORS = [
    (0, 255, 255),  # I (Cyan)
    (0, 0, 255),    # J (Blue)
    (255, 165, 0),  # L (Orange)
    (255, 255, 0),  # O (Yellow)
    (0, 255, 0),    # S (Green)
    (128, 0, 128),  # T (Purple)
    (255, 0, 0)     # Z (Red)
]

# Tetromino shapes (relative coordinates) and their rotations
# Each shape is a list of rotations, and each rotation is a list of block positions
SHAPES = [
    # I shape
    [[[0, 0], [1, 0], [2, 0], [3, 0]],
     [[1, 0], [1, 1], [1, 2], [1, 3]]],

    # J shape
    [[[0, 0], [0, 1], [1, 1], [2, 1]],
     [[1, 0], [2, 0], [1, 1], [1, 2]],
     [[0, 1], [1, 1], [2, 1], [2, 2]],
     [[1, 0], [1, 1], [0, 2], [1, 2]]],

    # L shape
    [[[0, 1], [1, 1], [2, 1], [2, 0]],
     [[1, 0], [1, 1], [1, 2], [2, 2]],
     [[0, 2], [0, 1], [1, 1], [2, 1]],
     [[0, 0], [1, 0], [1, 1], [1, 2]]],

    # O shape
    [[[0, 0], [1, 0], [0, 1], [1, 1]]], # Only one rotation

    # S shape
    [[[1, 0], [2, 0], [0, 1], [1, 1]],
     [[1, 0], [1, 1], [2, 1], [2, 2]]],

    # T shape
    [[[1, 0], [0, 1], [1, 1], [2, 1]],
     [[1, 0], [1, 1], [2, 1], [1, 2]],
     [[0, 1], [1, 1], [2, 1], [1, 2]],
     [[1, 0], [0, 1], [1, 1], [1, 2]]],

    # Z shape
    [[[0, 0], [1, 0], [1, 1], [2, 1]],
     [[2, 0], [1, 1], [2, 1], [1, 2]]]
]

# --- Game Classes ---

class Tetromino:
    def __init__(self, shape_index):
        self.shape_index = shape_index
        self.shape = SHAPES[shape_index]
        self.color = COLORS[shape_index]
        self.rotation_index = 0
        self.blocks = self.shape[self.rotation_index]
        self.x = BOARD_WIDTH // 2 - 2 # Starting position (adjust for shape width)
        self.y = 0 # Starting position at the top

    def rotate(self, direction):
        """Rotates the tetromino clockwise (1) or counter-clockwise (-1)."""
        next_rotation_index = (self.rotation_index + direction) % len(self.shape)
        original_rotation_index = self.rotation_index # Store original for rollback
        self.rotation_index = next_rotation_index
        self.blocks = self.shape[self.rotation_index]

        # Simple wall kick check (can be improved with SRS - Super Rotation System)
        # If rotation causes collision, try shifting horizontally
        if self.collides(board):
            # Try shifting right
            self.x += 1
            if not self.collides(board):
                return
            # Try shifting left
            self.x -= 2
            if not self.collides(board):
                return
            # If still collides, rollback rotation and position
            self.x += 1 # Reset x position
            self.rotation_index = original_rotation_index
            self.blocks = self.shape[self.rotation_index]


    def move(self, dx, dy):
        """Moves the tetromino by dx horizontally and dy vertically."""
        self.x += dx
        self.y += dy

    def collides(self, board):
        """Checks if the current tetromino position collides with the board or boundaries."""
        for block_x, block_y in self.blocks:
            board_x = self.x + block_x
            board_y = self.y + block_y

            # Check boundary collisions
            if board_x < 0 or board_x >= BOARD_WIDTH or board_y >= BOARD_HEIGHT:
                return True

            # Check collision with existing blocks on the board (only if y is within bounds)
            if board_y >= 0 and board.grid[board_y][board_x] != BLACK:
                return True
        return False

    def draw(self, surface):
        """Draws the tetromino on the given surface."""
        for block_x, block_y in self.blocks:
            # Calculate pixel position
            pixel_x = BOARD_POS_X + (self.x + block_x) * BLOCK_SIZE
            pixel_y = BOARD_POS_Y + (self.y + block_y) * BLOCK_SIZE

            # Draw the block
            pygame.draw.rect(surface, self.color, (pixel_x, pixel_y, BLOCK_SIZE, BLOCK_SIZE))
            # Add a border for better visibility
            pygame.draw.rect(surface, BLACK, (pixel_x, pixel_y, BLOCK_SIZE, BLOCK_SIZE), 2)


class Board:
    def __init__(self):
        # Initialize the board grid with black (empty) blocks
        self.grid = [[BLACK for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]

    def add_tetromino(self, tetromino):
        """Adds a settled tetromino's blocks to the board grid."""
        for block_x, block_y in tetromino.blocks:
            board_x = tetromino.x + block_x
            board_y = tetromino.y + block_y
            # Ensure the block is within the board boundaries before adding
            if 0 <= board_x < BOARD_WIDTH and 0 <= board_y < BOARD_HEIGHT:
                 self.grid[board_y][board_x] = tetromino.color

    def clear_lines(self):
        """Checks for and clears full lines, returning the number of lines cleared."""
        lines_cleared = 0
        new_grid = []
        for row in self.grid:
            # If the row is not full (contains a BLACK block)
            if BLACK in row:
                new_grid.append(row)
            else:
                # If the row is full, increment cleared lines count
                lines_cleared += 1

        # Add empty rows at the top for each line cleared
        for _ in range(lines_cleared):
            new_grid.insert(0, [BLACK for _ in range(BOARD_WIDTH)])

        self.grid = new_grid
        return lines_cleared

    def draw(self, surface):
        """Draws the board grid on the given surface."""
        for y in range(BOARD_HEIGHT):
            for x in range(BOARD_WIDTH):
                color = self.grid[y][x]
                pixel_x = BOARD_POS_X + x * BLOCK_SIZE
                pixel_y = BOARD_POS_Y + y * BLOCK_SIZE
                pygame.draw.rect(surface, color, (pixel_x, pixel_y, BLOCK_SIZE, BLOCK_SIZE))
                pygame.draw.rect(surface, GRAY, (pixel_x, pixel_y, BLOCK_SIZE, BLOCK_SIZE), 1) # Draw grid lines

# --- Game Logic ---

def create_new_tetromino():
    """Creates a new random tetromino."""
    shape_index = random.randint(0, len(SHAPES) - 1)
    return Tetromino(shape_index)

def draw_score(surface, score):
    """Draws the current score on the surface."""
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, WHITE)
    surface.blit(text, (10, 10)) # Position the score

def draw_game_over(surface):
    """Draws the Game Over message."""
    font = pygame.font.Font(None, 72)
    text = font.render("Game Over", True, WHITE)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    surface.blit(text, text_rect)

# --- Main Game Loop ---

def run_game():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Simple Tetris")

    clock = pygame.time.Clock()

    board = Board()
    current_tetromino = create_new_tetromino()
    score = 0
    game_over = False

    # Game loop variables
    fall_time = 0
    fall_speed = 10000 # Milliseconds per block fall

    running = True
    while running:
        dt = clock.tick(60) # Delta time in milliseconds
        fall_time += dt

        # --- Event Handling ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if game_over:
                    # Restart game on key press if game over
                    board = Board()
                    current_tetromino = create_new_tetromino()
                    score = 0
                    game_over = False
                    fall_time = 0 # Reset fall time
                    continue # Skip remaining event processing

                if event.key == pygame.K_LEFT:
                    current_tetromino.move(-1, 0)
                    if current_tetromino.collides(board):
                        current_tetromino.move(1, 0) # Move back if collision
                elif event.key == pygame.K_RIGHT:
                    current_tetromino.move(1, 0)
                    if current_tetromino.collides(board):
                        current_tetromino.move(-1, 0) # Move back if collision
                elif event.key == pygame.K_DOWN:
                    current_tetromino.move(0, 1)
                    if current_tetromino.collides(board):
                         current_tetromino.move(0, -1) # Move back if collision
                         # If cannot move down, it's time to settle
                         board.add_tetromino(current_tetromino)
                         lines_cleared = board.clear_lines()
                         score += lines_cleared * 100 # Simple scoring
                         current_tetromino = create_new_tetromino() # Get a new tetromino
                         if current_tetromino.collides(board):
                             game_over = True # Game over if new piece collides immediately
                         fall_time = 0 # Reset fall time after settling
                elif event.key == pygame.K_UP or event.key == pygame.K_x: # Rotate clockwise
                    current_tetromino.rotate(1)
                elif event.key == pygame.K_z: # Rotate counter-clockwise
                     current_tetromino.rotate(-1)
                elif event.key == pygame.K_SPACE: # Hard drop
                    while not current_tetromino.collides(board):
                        current_tetromino.move(0, 1)
                    current_tetromino.move(0, -1) # Move back one step after collision
                    board.add_tetromino(current_tetromino)
                    lines_cleared = board.clear_lines()
                    score += lines_cleared * 100 * 2 # Hard drop gives more points
                    current_tetromino = create_new_tetromino()
                    if current_tetromino.collides(board):
                        game_over = True
                    fall_time = 0 # Reset fall time after hard drop


        # --- Game Logic Updates ---
        if not game_over:
            if fall_time >= fall_speed:
                current_tetromino.move(0, 1) # Move down automatically
                if current_tetromino.collides(board):
                    current_tetromino.move(0, -1) # Move back if collision
                    # If cannot move down, it's time to settle
                    board.add_tetromino(current_tetromino)
                    lines_cleared = board.clear_lines()
                    score += lines_cleared * 100 # Simple scoring
                    current_tetromino = create_new_tetromino() # Get a new tetromino
                    if current_tetromino.collides(board):
                         game_over = True # Game over if new piece collides immediately
                    fall_time = 0 # Reset fall time after settling


        # --- Drawing ---
        screen.fill(BLACK) # Fill background

        # Draw the board outline
        pygame.draw.rect(screen, WHITE, (BOARD_POS_X - 2, BOARD_POS_Y - 2, BOARD_PIXEL_WIDTH + 4, BOARD_PIXEL_HEIGHT + 4), 2)

        board.draw(screen) # Draw the board
        if not game_over:
            current_tetromino.draw(screen) # Draw the current falling tetromino
        else:
            draw_game_over(screen) # Draw game over message

        draw_score(screen, score) # Draw the score

        pygame.display.flip() # Update the display

    pygame.quit() # Quit pygame

# Run the game
if __name__ == "__main__":
    run_game()
