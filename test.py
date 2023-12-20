import pygame
import sys

class YourGameClass:
    def __init__(self):
        # Khởi tạo Pygame
        pygame.init()

        # Kích thước màn hình
        self.screen_width, self.screen_height = 800, 600

        # Tạo màn hình
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Xoay Ảnh Quanh Điểm Bất Kỳ")

        # Tải hình ảnh từ file
        self.image = pygame.image.load("assets/cars/car001.png")

    def rotate_image_around_point(self, angle, rotate_point):
        # Tạo một bức tranh (Surface) có kích thước giống với ảnh
        temp_surface = pygame.Surface(self.image.get_size(), pygame.SRCALPHA)

        # Vẽ ảnh lên bức tranh
        temp_surface.blit(self.image, (0, 0))

        # Xoay bức tranh
        rotated_surface = pygame.transform.rotate(temp_surface, angle)

        # Lấy hình chữ nhật bao quanh bức tranh đã xoay
        rotated_rect = rotated_surface.get_rect(center=rotate_point)

        # Xóa toàn bộ màn hình
        self.screen.fill((255, 255, 255))

        # Vẽ bức tranh đã xoay lên màn hình
        self.screen.blit(rotated_surface, rotated_rect.topleft)

        # Vẽ điểm xoay
        pygame.draw.circle(self.screen, (255, 0, 0), rotate_point, 5)

        # Cập nhật màn hình
        pygame.display.flip()

    def run(self):
        # Vòng lặp chính của Pygame
        angle = 0
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
            angle += 1
            # Gọi hàm để xoay ảnh quanh điểm bất kỳ
            self.rotate_image_around_point(angle, (self.screen_width // 2, self.screen_height // 2))
            pygame.time.delay(10)

if __name__ == "__main__":
    game = YourGameClass()
    game.run()
