# import math

import pygame, sys
from config import *

class Prison:
    def __init__(self, game, window):
        self.game = game
        self.window = window
        self.clock = pygame.time.Clock()
        # self.game.new()

    def prison_background(self, background, image, x, y):
        image = pygame.image.load(image)
        image = pygame.transform.scale(image, (720, 480))
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
    def __init__(self, x, y):
        super().__init__()
        self.window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
        self.sprites = []
        self.sprites.append(pygame.image.load('images/Player/img0.png'))
        self.sprites.append(pygame.image.load('images/Player/img1.png'))
        self.sprites.append(pygame.image.load('images/Player/img2.png'))
        self.sprites.append(pygame.image.load('images/Player/img3.png'))
        self.sprites.append(pygame.image.load('images/Player/img4.png'))
        self.sprites.append(pygame.image.load('images/Player/img5.png'))
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

class Npc:
    def __init__(self, game, image, x, y):
        self.game = game
        self.alive = True
        self.window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
        img = pygame.image.load(image)
        self.image = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def draw(self, game):
        self.game = game
        self.window.blit(self.image, self.rect)
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

class dialogue:
    def __init__(self):