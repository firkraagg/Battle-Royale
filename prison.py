import pygame, sys
from config import *


window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

class Prison:
    def __init__(self, window):
        self.window = window
        self.clock = pygame.time.Clock()

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
    def __init__(self, x, y):
        self.alive = True
        self.animation_list = []
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        for i in range(6):
            img = pygame.image.load(f'images/Player/{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 1.5, img.get_height() * 1.5))
            self.animation_list.append(img)
        self.image = self.animation_list[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


    def update(self):
        animation_cooldown = 100
        self.image = self.animation_list[self.frame_index]
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        if self.frame_index >= len(self.animation_list):
            self.frame_index = 0

    def draw(self):
      window.blit(self.image, self.rect)





