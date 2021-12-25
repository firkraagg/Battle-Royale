import pygame
import config
import globals
import utilities

class System():
    def __init__(self):
        pass
    def check(self, entity):
        return True
    def update(self, window):
        for entity in globals.world.entities:
            if self.check(entity):
                self.updateEntity(window, entity)
    def updateEntity(self, window, entity):
        pass
class CameraSystem(System):
    def __init__(self):
        super().__init__()
    def check(self, entity):
        return entity.camera is not None
    def updateEntity(self, window, entity):

        cameraRect = entity.camera.rect
        clipRect = pygame.Rect(cameraRect.x, cameraRect.y, cameraRect.w, cameraRect.h)
        window.set_clip(clipRect)
        #
        # if entity.camera.entityToTrack is not None:
        #     trackedEntity = entity.camera.entityToTrack
        #     entity.camera.worldX = trackedEntity.position.rect.x
        #     entity.camera.worldY = trackedEntity.position.rect.y
        #
        # offsetX = cameraRect.x + cameraRect.w/2 - entity.camera.worldX
        # offsetY = cameraRect.y + cameraRect.h/2 - entity.camera.worldY

        for e in globals.world.entities:
            s = e.state
            a = e.animations.animationList[s]
            a.draw(window, e.position.rect.x, e.position.rect.y, e.direction == 'right', False)

        if entity.score is not None:
            coin_count_image = pygame.image.load('images/Coins/coin.png')
            coin_count_image = pygame.transform.scale(coin_count_image, (25, 30))
            window.blit(coin_count_image, (50, 50))
            utilities.draw_coinText(window, str(entity.score.score), 80, 52)


        window.set_clip(None)



class Camera():
    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)
        # self.worldX = 0
        # self.worldY = 0
        # self.entityToTrack = None
    #
    # def setWorldPosition(self, x, y):
    #     self.worldX = x
    #     self.worldY = y
    # def trackEntity(self, e):
    #     self.entityToTrack = e

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

class Score():
    def __init__(self):
        self.score = 0

class Entity():
    def __init__(self):
        self.state = 'standing'
        self.type = 'normal'
        self.position = None
        self.animations = Animations()
        self.direction = 'left'
        self.camera = None
        self.score = None


