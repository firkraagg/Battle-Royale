import pygame, sys
from config import *


class Story:
    def __init__(self, window):
        self.window = window
        self.clock = pygame.time.Clock()

    def animate_image(self, background, image, x, y):
        image = pygame.image.load(image)
        self.image = pygame.transform.scale(image, (image.get_width() * 1.3, image.get_height() * 1.3))
        rect = image.get_rect(topleft=(x, y))
        while rect.y > -GAME_HEIGHT:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.window.fill(background)
            self.window.blit(image, rect)
            pygame.time.wait(25)
            rect.y -= 1
            pygame.display.update()
            self.clock.tick(200)