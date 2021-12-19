import pygame

class Position:
    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)

class Animations:
    def __init__(self):
        self.animationList = {}
    def add(self, state, animation):
        self.animationList[state] = animation


class Animation:
    def __init__(self, image_list):
        self.image_list = image_list
        self.image_index = 0
        self.animation_timer = 0
        self.animation_speed = 8

    def update(self):
        self.animation_timer += 1
        if self.animation_timer > self.animation_speed:
            self.animation_timer = 0
            self.image_index += 1
            if self.image_index > len(self.image_list) - 1:
                self. image_index = 0

    def draw(self, window, x, y, flip_x, flip_y):
        # window.blit(self.image_list[self.image_index], (x, y))
        # self.image_list = pygame.transform.scale(self.player_image, (102, 102))
        window.blit(pygame.transform.flip(self.image_list[self.image_index], flip_x, flip_y), (x, y))

class Entity():
    def __init__(self):
        self.state = 'standing'
        self.type = 'normal'
        self.position = None
        self.animations = Animations()
        self.direction = 'left'


