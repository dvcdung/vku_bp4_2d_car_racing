import pygame
import sys
from src.game_manager import GameManager

SCREEN_SIZE = (1200, 700)

# Create a window
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("2D CAR RACING")

# Create init objects
clock = pygame.time.Clock()
game_manager = GameManager(SCREEN_SIZE)

# Run the game
while (True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    game_manager.update(pygame)

    pygame.display.flip()
    clock.tick(60)

def main():

    # Đường dẫn đến tệp ảnh
    image_path = "assets/maps/map01.jpg"  # Thay đổi thành đường dẫn tới ảnh thực tế

    # Tải ảnh
    image = pygame.image.load(image_path)
    image_rect = image.get_rect()

    # Điểm bắt đầu hiển thị ảnh (điểm góc trái trên)
    display_position = [0, 0]

    # Tốc độ di chuyển ảnh
    speed = [2, 2]

    # Lặp vô hạn
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Di chuyển ảnh
        display_position[0] += speed[0]
        display_position[1] += speed[1]

        # Kiểm tra nếu ảnh đã đi qua cửa sổ, reset vị trí
        if display_position[0] > SCREEN_SIZE[0]:
            display_position[0] = -image_rect.width
        if display_position[1] > SCREEN_SIZE[1]:
            display_position[1] = -image_rect.height

        # Vẽ ảnh lên cửa sổ
        screen.blit(image, display_position)
        pygame.display.flip()

        # Tạm dừng để giảm tốc độ cập nhật
        pygame.time.delay(10)

    # Đóng cửa sổ khi kết thúc
    pygame.quit()
    sys.exit()
