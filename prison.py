# import math

import pygame, sys
from config import *

class Prison(pygame.sprite.Sprite):
    def __init__(self, game, window):
        self.game = game
        self.groups = self.game.sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.window = window
        self.clock = pygame.time.Clock()

        self.image = pygame.image.load('images/Prison/prison.png')
        self.image = pygame.transform.scale(self.image, (self.window.get_width(), self.window.get_height()))
        self.rect = self.image.get_rect()

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self.groups = self.game.sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
        self.sprites = []
        for i in range(5):
            self.sprites.append(pygame.transform.scale(pygame.image.load(f'images/Player/img{i}.png'), (145, 145)))
        self.current_sprite = 0

        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]
        # self.animation_list = []
        # self.frame_index = 0
        # self.update_time = pygame.time.get_ticks()
        # for i in range(6):
        #     img = pygame.image.load(f'images/Player/{i}.png')
        #     img = pygame.transform.scale(img, (img.get_width() * 3.5, img.get_height() * 3.5))
        #     self.animation_list.append(img)
        # self.image = self.animation_list[self.frame_index]
        # self.rect = self.image.get_rect()
        # self.rect.center = (x, y)

    def update(self):
        self.current_sprite += 0.1
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        self.image = self.sprites[int(self.current_sprite)]

class Npc(pygame.sprite.Sprite):
    def __init__(self, game, image, x, y):
        self.game = game
        self.groups = self.game.sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.alive = True
        self.window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
        img = pygame.image.load(image)
        self.image = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        pass
# class Npc(pygame.sprite.Sprite):
#     def __init__(self, game, x, y):
#         self.game = game
    #     self._layer = 1
    #     self.groups = self.game.npc_group
    #     pygame.sprite.Sprite.__init__(self, self.groups)
    #
    #     self.frames = []
    #     frame = pygame.image.load(f'images/Npc/0.png').convert_alpha()
    #     frame = pygame.transform.scale(frame, (frame.get_width() * 1.5, frame.get_height() * 1.5))
    #     self.frames.append(frame)
    #
    #     self.image = self.frames[0]
    #     self.rect = self.image.get_rect(center=(x, y))
    #
    #     self.alive = True
    #     self.frame_index = 0
    #
    # def update(self):
    #     self.animation()
    #
    # def animation(self):
    #     self.image = self.frames[math.floor(self.frame_index)]
    #     self.frame_index += 0.1
    #     if self.frame_index >= len(self.frames):
    #         self.frame_index = 0

class Dialogue:
    def __init__(self):
        pass