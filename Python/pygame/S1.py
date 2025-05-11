# Import thư viện Pygame
import pygame

# Khởi tạo thư viện Pygame
pygame.init()  # Khởi tạo Pygame để sử dụng các tính năng của nó

# Tạo cửa sổ hiển thị (window) với kích thước 800x600
screen = pygame.display.set_mode((800, 600))  # Cửa sổ có chiều rộng 800px và chiều cao 600px

# Đặt tiêu đề cho cửa sổ
pygame.display.set_caption('Game Pygame')  # Đặt tên cho cửa sổ game

# Màu sắc (RGB)
WHITE = (255, 255, 255)  # Màu trắng
BLACK = (0, 0, 0)        # Màu đen
RED = (255, 0, 0)        # Màu đỏ
GREEN = (0, 255, 0)      # Màu xanh lá
BLUE = (0, 0, 255)       # Màu xanh dương

# Vòng lặp chính của game
running = True  # Biến điều khiển vòng lặp game
while running:
    # Kiểm tra các sự kiện (event)
    for event in pygame.event.get():  # Duyệt qua tất cả sự kiện hiện tại
        if event.type == pygame.QUIT:  # Nếu người dùng nhấn nút thoát cửa sổ
            running = False  # Dừng vòng lặp và thoát game

    # Đổ màu nền cho màn hình
    screen.fill(WHITE)  # Đặt nền của cửa sổ là màu trắng

    # Vẽ các hình ảnh và đối tượng lên màn hình
    pygame.draw.rect(screen, RED, (100, 100, 200, 150))  # Vẽ hình chữ nhật màu đỏ tại vị trí (100, 100) với kích thước (200, 150)
    pygame.draw.circle(screen, BLUE, (400, 300), 50)  # Vẽ hình tròn màu xanh dương tại vị trí (400, 300) với bán kính 50px

    # Cập nhật màn hình hiển thị
    pygame.display.update()  # Cập nhật cửa sổ hiển thị

# Tải hình ảnh từ file
image = pygame.image.load('image.png')  # Tải hình ảnh từ file
screen.blit(image, (100, 100))  # Vẽ hình ảnh lên màn hình tại vị trí (100, 100)

# Nhận phím bấm từ người dùng
keys = pygame.key.get_pressed()  # Lấy trạng thái của tất cả các phím
if keys[pygame.K_LEFT]:  # Nếu phím mũi tên trái được nhấn
    print("Left key pressed")

# Thêm nhạc
pygame.mixer.init()  # Khởi tạo bộ trộn âm thanh
pygame.mixer.music.load('background_music.mp3')  # Tải nhạc nền
pygame.mixer.music.play(-1)  # Phát nhạc nền (lặp lại vô hạn)

# Quản lý thời gian FPS
clock = pygame.time.Clock()  # Tạo đối tượng clock để điều khiển thời gian
clock.tick(60)  # Giới hạn số khung hình mỗi giây là 60 FPS

# Sử dụng chuột
mouse_x, mouse_y = pygame.mouse.get_pos()  # Lấy vị trí con chuột
mouse_click = pygame.mouse.get_pressed()  # Lấy trạng thái của nút chuột

# Thoát game
pygame.quit()  # Thoát khỏi Pygame



