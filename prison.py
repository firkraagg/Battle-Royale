<<<<<<< Updated upstream
import math
=======
<<<<<<< HEAD
# import math
=======
import math
>>>>>>> 2
>>>>>>> Stashed changes

import pygame, sys
from config import *

<<<<<<< Updated upstream

class Prison:
=======
<<<<<<< HEAD
class Prison(pygame.sprite.Sprite):
>>>>>>> Stashed changes
    def __init__(self, game, window):
        self.game = game
        self.window = window
        self.clock = pygame.time.Clock()
        # self.game.new()

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

class Player:
    def __init__(self, game, image , x, y):
        self.game = game
        self.alive = True
        self.window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
        img = pygame.image.load(image)
        self.image = pygame.transform.scale(img, (img.get_width() * 1.5, img.get_height() * 1.5))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def draw(self, game):
        self.game = game
        self.window.blit(self.image, self.rect)

<<<<<<< Updated upstream
=======
        self.window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
        self.sprites = []
        for i in range(5):
            self.sprites.append(pygame.transform.scale(pygame.image.load(f'images/Player/img{i}.png'), (145, 145)))
        self.current_sprite = 0
=======

class Prison:
    def __init__(self, game, window):
        self.game = game
        self.window = window
        self.clock = pygame.time.Clock()
        # self.game.new()

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

class Player:
    def __init__(self, game, image , x, y):
        self.game = game
        self.alive = True
        self.window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
        img = pygame.image.load(image)
        self.image = pygame.transform.scale(img, (img.get_width() * 1.5, img.get_height() * 1.5))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def draw(self, game):
        self.game = game
        self.window.blit(self.image, self.rect)
>>>>>>> 2
>>>>>>> Stashed changes



    #     self._layer = 1
    #     self.groups = self.game.player_group
    #     pygame.sprite.Sprite.__init__(self, self.groups)
    #
    #
    #     self.frames = []
    #     for i in range(6):
    #         frame = pygame.image.load(f'images/Player/{i}.png').convert_alpha()
    #         frame = pygame.transform.scale(frame, (frame.get_width() * 1.5, frame.get_height() * 1.5))
    #         self.frames.append(frame)
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

<<<<<<< Updated upstream
class Npc:
    def __init__(self, game, image , x, y):
        self.game = game
=======
<<<<<<< HEAD
>>>>>>> Stashed changes
        self.alive = True
        self.window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
        img = pygame.image.load(image)
        self.image = pygame.transform.scale(img, (img.get_width() * 1.5, img.get_height() * 1.5))
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
<<<<<<< Updated upstream
    #         self.frame_index = 0
=======
    #         self.frame_index = 0

class Dialogue:
    def __init__(self):
        pass
=======
    #     self._layer = 1
    #     self.groups = self.game.player_group
    #     pygame.sprite.Sprite.__init__(self, self.groups)
    #
    #
    #     self.frames = []
    #     for i in range(6):
    #         frame = pygame.image.load(f'images/Player/{i}.png').convert_alpha()
    #         frame = pygame.transform.scale(frame, (frame.get_width() * 1.5, frame.get_height() * 1.5))
    #         self.frames.append(frame)
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

class Npc:
    def __init__(self, game, image , x, y):
        self.game = game
        self.alive = True
        self.window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
        img = pygame.image.load(image)
        self.image = pygame.transform.scale(img, (img.get_width() * 1.5, img.get_height() * 1.5))
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
>>>>>>> 2
>>>>>>> Stashed changes
