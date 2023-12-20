import pygame

class ImageHandler:

    def load(image_path="", target_size=None):
        original_image  = pygame.image.load(image_path)
        if target_size:
            return pygame.transform.scale(original_image, target_size)
        else:
            return original_image
        
    def rotate(image, angle, center_pos):
        image_rotated = pygame.transform.rotate(image, angle)
        return image_rotated, image_rotated.get_rect(center=center_pos)
    
    def scale(img, factor):
        size = round(img.get_width() * factor), round(img.get_height() * factor)
        return pygame.transform.scale(img, size)

    def blit_rotate_center(screen, image, top_left, angle):
        rotated_image = pygame.transform.rotate(image, angle)
        new_rect = rotated_image.get_rect(center=image.get_rect(topleft=top_left).center)
        screen.blit(rotated_image, new_rect.topleft)