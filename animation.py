import pygame, sys
from config import *


class Animation:
    def __init__(self, window):
        self.window = window
        self.clock = pygame.time.Clock()

    def animate_image(self, background, image, x, y):
        image = pygame.image.load(image)
        rect = image.get_rect(topleft=(x, y))
        while rect.y < GAME_HEIGHT:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.window.fill(background)
            self.window.blit(image, rect)
            rect.y += 2
            pygame.display.update()
            self.clock.tick(FPS)
