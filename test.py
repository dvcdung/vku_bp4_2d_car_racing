import pygame
import sys

# Khởi tạo Pygame
pygame.init()

# Kích thước màn hình
screen_width, screen_height = 400, 300

# Màu sắc
white = (255, 255, 255)
black = (0, 0, 0)

# Khởi tạo màn hình
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Tam giác nút')

def draw_triangle(direction):
    # Xóa màn hình
    screen.fill(white)

    # Tọa độ tam giác
    if direction == 'left':
        points = [(200, 100), (250, 200), (200, 300)]
    elif direction == 'right':
        points = [(200, 100), (150, 200), (200, 300)]

    # Vẽ tam giác
    pygame.draw.polygon(screen, black, points)

    # Cập nhật màn hình
    pygame.display.flip()

# Vòng lặp chính
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                draw_triangle('left')
            elif event.key == pygame.K_RIGHT:
                draw_triangle('right')

    # Thêm delay để giảm tải CPU
    pygame.time.delay(10)

# Đóng cửa sổ Pygame khi thoát
pygame.quit()
sys.exit()
