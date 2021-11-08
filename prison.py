import math

import pygame, sys
from config import *


class Prison:
    def __init__(self, game, window):
        self.game = game
        self.window = window
        self.clock = pygame.time.Clock()
        self.game.new()

    def prison_background(self, background, image, x, y):
        image = pygame.image.load(image)
        rect = image.get_rect(topleft=(x, y))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        self.window.fill(background)
        self.window.blit(image, rect)
        pygame.display.update()
        self.clock.tick(FPS)


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = 1
        self.groups = self.game.player_group
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.frames = []
        for i in range(6):
            frame = pygame.image.load(f'images/Player/{i}.png').convert_alpha()
            frame = pygame.transform.scale(frame, (frame.get_width() * 1.5, frame.get_height() * 1.5))
            self.frames.append(frame)

        self.image = self.frames[0]
        self.rect = self.image.get_rect(center=(x, y))

        self.alive = True
        self.frame_index = 0

    def update(self):
        print(math.floor(self.frame_index))
        self.animation()

    def animation(self):
        self.image = self.frames[math.floor(self.frame_index)]
        self.frame_index += 0.1
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
