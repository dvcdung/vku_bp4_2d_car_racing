import pygame

class ImageHandler:


    def scale(self, img, factor):
        size = round(img.get_width() * factor), round(img.get_height() * factor)
        return pygame.transform.scale(img, size)

    def blit_rotate_center(self, screen, image, top_left, angle):
        rotated_image = pygame.transform.rotate(image, angle)
        new_rect = rotated_image.get_rect(center=image.get_rect(topleft=top_left).center)
        screen.blit(rotated_image, new_rect.topleft)

    def crop_image(input_path, output_path, crop_box):
        try:
            # Open the image
            img = Image.open(input_path)

            # Crop the image
            cropped_img = img.crop(crop_box)

            # Save the cropped image
            cropped_img.save(output_path)

            print(f"Image cropped and saved to {output_path}")

        except Exception as e:
            print(f"Error: {e}")