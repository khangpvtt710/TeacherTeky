import pygame
import random

# Khởi tạo Pygame
pygame.init()

# --- Hằng số của Game ---
SCREEN_WIDTH = 400 # Chiều rộng cửa sổ game
SCREEN_HEIGHT = 600 # Chiều cao cửa sổ game
BLOCK_SIZE = 30  # Kích thước của mỗi khối Tetris (pixel)
BOARD_WIDTH = 10  # Số lượng khối theo chiều ngang của bảng
BOARD_HEIGHT = 20 # Số lượng khối theo chiều dọc của bảng

# Tính toán kích thước bảng theo pixel
BOARD_PIXEL_WIDTH = BOARD_WIDTH * BLOCK_SIZE
BOARD_PIXEL_HEIGHT = BOARD_HEIGHT * BLOCK_SIZE

# Vị trí của bảng (căn giữa theo chiều ngang)
BOARD_POS_X = (SCREEN_WIDTH - BOARD_PIXEL_WIDTH) // 2
BOARD_POS_Y = SCREEN_HEIGHT - BOARD_PIXEL_HEIGHT - 20 # Thêm khoảng trống ở dưới

# Màu sắc (RGB)
BLACK = (0, 0, 0)       # Đen
WHITE = (255, 255, 255) # Trắng
GRAY = (128, 128, 128) # Xám
COLORS = [
    (0, 255, 255),  # I (Cyan)
    (0, 0, 255),    # J (Blue)
    (255, 165, 0),  # L (Orange)
    (255, 255, 0),  # O (Yellow)
    (0, 255, 0),    # S (Green)
    (128, 0, 128),  # T (Purple)
    (255, 0, 0)     # Z (Red)
]

# Các hình dạng Tetromino (tọa độ tương đối) và các trạng thái xoay của chúng
# Mỗi hình dạng là một danh sách các trạng thái xoay, và mỗi trạng thái xoay là một danh sách các vị trí khối
SHAPES = [
    # Hình dạng I
    [[[0, 0], [1, 0], [2, 0], [3, 0]], # Ngang
     [[1, 0], [1, 1], [1, 2], [1, 3]]], # Dọc

    # Hình dạng J
    [[[0, 0], [0, 1], [1, 1], [2, 1]],
     [[1, 0], [2, 0], [1, 1], [1, 2]],
     [[0, 1], [1, 1], [2, 1], [2, 2]],
     [[1, 0], [1, 1], [0, 2], [1, 2]]],

    # Hình dạng L
    [[[0, 1], [1, 1], [2, 1], [2, 0]],
     [[1, 0], [1, 1], [1, 2], [2, 2]],
     [[0, 2], [0, 1], [1, 1], [2, 1]],
     [[0, 0], [1, 0], [1, 1], [1, 2]]],

    # Hình dạng O
    [[[0, 0], [1, 0], [0, 1], [1, 1]]], # Chỉ có một trạng thái xoay

    # Hình dạng S
    [[[1, 0], [2, 0], [0, 1], [1, 1]],
     [[1, 0], [1, 1], [2, 1], [2, 2]]],

    # Hình dạng T
    [[[1, 0], [0, 1], [1, 1], [2, 1]],
     [[1, 0], [1, 1], [2, 1], [1, 2]],
     [[0, 1], [1, 1], [2, 1], [1, 2]],
     [[1, 0], [0, 1], [1, 1], [1, 2]]],

    # Hình dạng Z
    [[[0, 0], [1, 0], [1, 1], [2, 1]],
     [[2, 0], [1, 1], [2, 1], [1, 2]]]
]

# --- Lớp của Game ---

class Tetromino:
    def __init__(self, shape_index):
        # Chỉ số của hình dạng
        self.shape_index = shape_index
        # Lấy danh sách các trạng thái xoay của hình dạng
        self.shape = SHAPES[shape_index]
        # Lấy màu tương ứng với hình dạng
        self.color = COLORS[shape_index]
        # Chỉ số trạng thái xoay hiện tại
        self.rotation_index = 0
        # Lấy các khối cho trạng thái xoay hiện tại
        self.blocks = self.shape[self.rotation_index]
        # Vị trí bắt đầu trên bảng (căn giữa và điều chỉnh theo chiều rộng hình dạng)
        self.x = BOARD_WIDTH // 2 - 2
        # Vị trí bắt đầu ở đỉnh bảng
        self.y = 0

    def rotate(self, direction):
        """Xoay tetromino theo chiều kim đồng hồ (1) hoặc ngược chiều kim đồng hồ (-1)."""
        # Tính toán chỉ số trạng thái xoay tiếp theo
        next_rotation_index = (self.rotation_index + direction) % len(self.shape)
        # Lưu chỉ số trạng thái xoay ban đầu để khôi phục nếu cần
        original_rotation_index = self.rotation_index
        # Cập nhật chỉ số trạng thái xoay mới
        self.rotation_index = next_rotation_index
        # Cập nhật các khối cho trạng thái xoay mới
        self.blocks = self.shape[self.rotation_index]

        # Kiểm tra va chạm đơn giản sau khi xoay (có thể cải thiện với SRS - Super Rotation System)
        # Nếu xoay gây ra va chạm, thử dịch chuyển ngang
        if self.collides(board):
            # Thử dịch chuyển sang phải
            self.x += 1
            if not self.collides(board):
                return # Xoay và dịch chuyển thành công
            # Thử dịch chuyển sang trái
            self.x -= 2
            if not self.collides(board):
                return # Xoay và dịch chuyển thành công
            # Nếu vẫn va chạm, khôi phục trạng thái xoay và vị trí ban đầu
            self.x += 1 # Đặt lại vị trí x
            self.rotation_index = original_rotation_index
            self.blocks = self.shape[self.rotation_index]


    def move(self, dx, dy):
        """Di chuyển tetromino theo dx ngang và dy dọc."""
        self.x += dx
        self.y += dy

    def collides(self, board):
        """Kiểm tra xem vị trí hiện tại của tetromino có va chạm với bảng hoặc ranh giới không."""
        for block_x, block_y in self.blocks:
            # Tính toán vị trí khối trên bảng
            board_x = self.x + block_x
            board_y = self.y + block_y

            # Kiểm tra va chạm với ranh giới
            if board_x < 0 or board_x >= BOARD_WIDTH or board_y >= BOARD_HEIGHT:
                return True

            # Kiểm tra va chạm với các khối đã tồn tại trên bảng (chỉ khi y nằm trong ranh giới)
            # board_y >= 0 để tránh kiểm tra các khối nằm phía trên đỉnh bảng (y âm)
            if board_y >= 0 and board.grid[board_y][board_x] != BLACK:
                return True
        return False

    def draw(self, surface):
        """Vẽ tetromino lên bề mặt (surface) được cung cấp."""
        for block_x, block_y in self.blocks:
            # Tính toán vị trí pixel trên màn hình
            pixel_x = BOARD_POS_X + (self.x + block_x) * BLOCK_SIZE
            pixel_y = BOARD_POS_Y + (self.y + block_y) * BLOCK_SIZE

            # Vẽ khối
            pygame.draw.rect(surface, self.color, (pixel_x, pixel_y, BLOCK_SIZE, BLOCK_SIZE))
            # Thêm đường viền để dễ nhìn hơn
            pygame.draw.rect(surface, BLACK, (pixel_x, pixel_y, BLOCK_SIZE, BLOCK_SIZE), 2)


class Board:
    def __init__(self):
        # Khởi tạo lưới bảng với các khối màu đen (trống)
        self.grid = [[BLACK for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]

    def add_tetromino(self, tetromino):
        """Thêm các khối của tetromino đã ổn định vào lưới bảng."""
        for block_x, block_y in tetromino.blocks:
            # Tính toán vị trí khối trên bảng
            board_x = tetromino.x + block_x
            board_y = tetromino.y + block_y
            # Đảm bảo khối nằm trong ranh giới bảng trước khi thêm
            if 0 <= board_x < BOARD_WIDTH and 0 <= board_y < BOARD_HEIGHT:
                 self.grid[board_y][board_x] = tetromino.color

    def clear_lines(self):
        """Kiểm tra và xóa các dòng đầy, trả về số lượng dòng đã xóa."""
        lines_cleared = 0 # Biến đếm số dòng đã xóa
        new_grid = [] # Lưới mới sau khi xóa dòng
        for row in self.grid:
            # Nếu dòng KHÔNG đầy (chứa một khối màu đen)
            if BLACK in row:
                new_grid.append(row) # Giữ lại dòng này
            else:
                # Nếu dòng đầy, tăng biến đếm dòng đã xóa
                lines_cleared += 1

        # Thêm các dòng trống (màu đen) vào đỉnh của lưới mới cho mỗi dòng đã xóa
        for _ in range(lines_cleared):
            new_grid.insert(0, [BLACK for _ in range(BOARD_WIDTH)])

        # Cập nhật lưới bảng bằng lưới mới
        self.grid = new_grid
        return lines_cleared # Trả về số dòng đã xóa

    def draw(self, surface):
        """Vẽ lưới bảng lên bề mặt (surface) được cung cấp."""
        for y in range(BOARD_HEIGHT):
            for x in range(BOARD_WIDTH):
                # Lấy màu của khối tại vị trí (x, y)
                color = self.grid[y][x]
                # Tính toán vị trí pixel trên màn hình
                pixel_x = BOARD_POS_X + x * BLOCK_SIZE
                pixel_y = BOARD_POS_Y + y * BLOCK_SIZE
                # Vẽ khối
                pygame.draw.rect(surface, color, (pixel_x, pixel_y, BLOCK_SIZE, BLOCK_SIZE))
                # Vẽ đường lưới
                pygame.draw.rect(surface, GRAY, (pixel_x, pixel_y, BLOCK_SIZE, BLOCK_SIZE), 1)

# --- Logic Game ---

def create_new_tetromino():
    """Tạo một tetromino mới ngẫu nhiên."""
    # Chọn ngẫu nhiên chỉ số hình dạng
    shape_index = random.randint(0, len(SHAPES) - 1)
    # Trả về một đối tượng Tetromino mới
    return Tetromino(shape_index)

def draw_score(surface, score):
    """Vẽ điểm số hiện tại lên bề mặt (surface)."""
    # Chọn font và kích thước
    font = pygame.font.Font(None, 36)
    # Tạo bề mặt văn bản
    text = font.render(f"Score: {score}", True, WHITE)
    # Vẽ văn bản lên bề mặt
    surface.blit(text, (10, 10)) # Vị trí của điểm số

def draw_game_over(surface):
    """Vẽ thông báo Game Over."""
    # Chọn font và kích thước lớn
    font = pygame.font.Font(None, 72)
    # Tạo bề mặt văn bản
    text = font.render("Game Over", True, WHITE)
    # Lấy hình chữ nhật bao quanh văn bản và căn giữa
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    # Vẽ văn bản lên bề mặt
    surface.blit(text, text_rect)

# --- Vòng lặp Game Chính ---

def run_game():
    # Tạo cửa sổ game
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Đặt tiêu đề cửa sổ
    pygame.display.set_caption("Simple Tetris")

    # Tạo đối tượng Clock để kiểm soát tốc độ khung hình
    clock = pygame.time.Clock()

    # Khởi tạo bảng game
    board = Board()
    # Tạo tetromino đầu tiên
    current_tetromino = create_new_tetromino()
    # Khởi tạo điểm số
    score = 0
    # Biến trạng thái game over
    game_over = False

    # Biến cho logic rơi tự động
    fall_time = 0 # Thời gian đã trôi qua kể từ lần rơi cuối cùng
    fall_speed = 500 # Tốc độ rơi (mili giây cho mỗi khối)

    # Biến điều khiển vòng lặp chính
    running = True
    while running:
        # Lấy thời gian đã trôi qua kể từ khung hình cuối cùng (dt)
        dt = clock.tick(60) # Giới hạn tốc độ khung hình ở 60 FPS, dt tính bằng mili giây
        fall_time += dt # Cộng thời gian đã trôi qua vào biến đếm thời gian rơi

        # --- Xử lý Sự kiện ---
        for event in pygame.event.get():
            # Nếu người dùng đóng cửa sổ
            if event.type == pygame.QUIT:
                running = False # Dừng vòng lặp chính
            # Nếu người dùng nhấn một phím
            if event.type == pygame.KEYDOWN:
                # Nếu game đã kết thúc
                if game_over:
                    # Khởi động lại game khi nhấn phím bất kỳ
                    board = Board() # Tạo lại bảng mới
                    current_tetromino = create_new_tetromino() # Tạo tetromino mới
                    score = 0 # Đặt lại điểm số
                    game_over = False # Đặt lại trạng thái game over
                    fall_time = 0 # Đặt lại thời gian rơi
                    continue # Bỏ qua xử lý sự kiện còn lại cho khung hình này

                # Xử lý các phím di chuyển và xoay
                if event.key == pygame.K_LEFT:
                    current_tetromino.move(-1, 0) # Di chuyển sang trái
                    if current_tetromino.collides(board):
                        current_tetromino.move(1, 0) # Di chuyển trở lại nếu va chạm
                elif event.key == pygame.K_RIGHT:
                    current_tetromino.move(1, 0) # Di chuyển sang phải
                    if current_tetromino.collides(board):
                        current_tetromino.move(-1, 0) # Di chuyển trở lại nếu va chạm
                elif event.key == pygame.K_DOWN:
                    current_tetromino.move(0, 1) # Di chuyển xuống (soft drop)
                    if current_tetromino.collides(board):
                         current_tetromino.move(0, -1) # Di chuyển trở lại nếu va chạm
                         # Nếu không thể di chuyển xuống, đã đến lúc cố định khối
                         board.add_tetromino(current_tetromino) # Thêm khối vào bảng
                         lines_cleared = board.clear_lines() # Kiểm tra và xóa dòng
                         score += lines_cleared * 100 # Tính điểm (đơn giản)
                         current_tetromino = create_new_tetromino() # Tạo tetromino mới
                         if current_tetromino.collides(board):
                             game_over = True # Game over nếu khối mới va chạm ngay lập tức
                         fall_time = 0 # Đặt lại thời gian rơi sau khi cố định
                elif event.key == pygame.K_UP or event.key == pygame.K_x: # Xoay theo chiều kim đồng hồ
                    current_tetromino.rotate(1)
                elif event.key == pygame.K_z: # Xoay ngược chiều kim đồng hồ
                     current_tetromino.rotate(-1)
                elif event.key == pygame.K_SPACE: # Thả nhanh (hard drop)
                    # Di chuyển xuống cho đến khi va chạm
                    while not current_tetromino.collides(board):
                        current_tetromino.move(0, 1)
                    current_tetromino.move(0, -1) # Di chuyển trở lại một bước sau khi va chạm
                    board.add_tetromino(current_tetromino) # Thêm khối vào bảng
                    lines_cleared = board.clear_lines() # Kiểm tra và xóa dòng
                    score += lines_cleared * 100 * 2 # Thả nhanh được nhiều điểm hơn
                    current_tetromino = create_new_tetromino() # Tạo tetromino mới
                    if current_tetromino.collides(board):
                        game_over = True
                    fall_time = 0 # Đặt lại thời gian rơi sau khi thả nhanh


        # --- Cập nhật Logic Game ---
        if not game_over: # Chỉ cập nhật logic game nếu chưa game over
            if fall_time >= fall_speed: # Nếu đã đủ thời gian để khối rơi
                current_tetromino.move(0, 1) # Di chuyển khối xuống tự động
                if current_tetromino.collides(board): # Nếu khối va chạm sau khi rơi
                    current_tetromino.move(0, -1) # Di chuyển trở lại một bước
                    # Nếu không thể di chuyển xuống, đã đến lúc cố định khối
                    board.add_tetromino(current_tetromino) # Thêm khối vào bảng
                    lines_cleared = board.clear_lines() # Kiểm tra và xóa dòng
                    score += lines_cleared * 100 # Tính điểm
                    current_tetromino = create_new_tetromino() # Tạo tetromino mới
                    if current_tetromino.collides(board):
                         game_over = True # Game over nếu khối mới va chạm ngay lập tức
                    fall_time = 0 # Đặt lại thời gian rơi sau khi cố định


        # --- Vẽ ---
        screen.fill(BLACK) # Tô đen toàn bộ màn hình (xóa khung hình trước)

        # Vẽ đường viền của bảng
        pygame.draw.rect(screen, WHITE, (BOARD_POS_X - 2, BOARD_POS_Y - 2, BOARD_PIXEL_WIDTH + 4, BOARD_PIXEL_HEIGHT + 4), 2)

        board.draw(screen) # Vẽ bảng game
        if not game_over: # Chỉ vẽ khối đang rơi nếu chưa game over
            current_tetromino.draw(screen) # Vẽ khối tetromino hiện tại
        else:
            draw_game_over(screen) # Vẽ thông báo game over

        draw_score(screen, score) # Vẽ điểm số

        pygame.display.flip() # Cập nhật toàn bộ màn hình

    pygame.quit() # Thoát Pygame

# Chạy game nếu script được thực thi trực tiếp
if __name__ == "__main__":
    run_game()
