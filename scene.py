import pygame
import engine
import menu
import globals
import fight
import button

import utilities
from config import *
clock = pygame.time.Clock()


class Scene:
    def __init__(self):
        pass
    def onEnter(self):
        pass
    def onExit(self):
        pass
    def input(self, sm, inputStream):
        pass
    def update(self, sm, inputStream):
        pass
    def draw(self, sm, window):
        pass


class MainMenuScene(Scene):
    def draw(self, sm, window):
        button1 = menu.Button('Play Game', 160, 50, (270, 170), 6)
        button2 = menu.Button('Quit', 110, 30, (295, 255), 6)
        menu_bg = pygame.image.load("images/Backgrounds/menu_bg.png")
        window.blit(menu_bg, (0, 0))
        button1.draw()
        button2.draw()
        if button1.pressed:
            sm.push(FadeTransitionScene(self, LevelSelectScene()))
        elif button2.pressed:
            pygame.quit()


class LevelSelectScene(Scene):
    def input(self, sm, inputStream):
        if inputStream.keyboard.isKeyPressed(pygame.K_SPACE):
            globals.world = globals.levels[1]
            sm.push(FadeTransitionScene(self, GameScene()))
        if inputStream.keyboard.isKeyPressed(pygame.K_ESCAPE):
            sm.pop()
            sm.push(FadeTransitionScene(self, MainMenuScene()))

    def draw(self, sm, window):
        mid_w, mid_h = GAME_WIDTH / 2, GAME_HEIGHT / 2
        window.fill(GREY)
        utilities.intro_text(window, 'Press space to skip', 20, mid_w, mid_h + 210 )




class GameScene(Scene):
    def __init__(self):
        self.cameraSystem = engine.CameraSystem()
        self.collectionSystem = engine.CollectionSystem()
        # self.talkingSystem = engine.TalkingSystem()
        # self.physicsSystem = engine.PhysicsSystem()
        self.inputSystem = engine.InputSystem()
    def input(self, sm, inputStream):
        if inputStream.keyboard.isKeyPressed(pygame.K_ESCAPE):
            sm.pop()
            sm.push(FadeTransitionScene(self, MainMenuScene()))
        if inputStream.keyboard.isKeyPressed(pygame.K_1):
            globals.world = globals.levels[2]
            sm.push(FadeTransitionScene(self, HallScene()))
    def update(self, sm, inputStream):
        self.inputSystem.update(inputStream=inputStream)
        # self.talkingSystem.update()
        self.collectionSystem.update()
        # self.physicsSystem.update()
    def draw(self, sm, window):
        # p_background = pygame.image.load('images/Prison/prison.png')
        # p_background = pygame.transform.scale(p_background, (GAME_WIDTH, GAME_HEIGHT))
        # # window.blit(p_background, (0, 0))
        # utilities.makeBackground(p_background)
        globals.world = globals.levels[1]
        utilities.npcName(window, "Spiculus", WHITE, 370, 215)
        self.cameraSystem.update(window)




class HallScene(Scene):
    def __init__(self):
        self.cameraSystem = engine.CameraSystem()
        self.collectionSystem = engine.CollectionSystem()
        # self.physicsSystem = engine.PhysicsSystem()
        self.inputSystem = engine.InputSystem()
    def input(self, sm, inputStream):
        if inputStream.keyboard.isKeyPressed(pygame.K_ESCAPE):
            sm.pop()
            sm.push(FadeTransitionScene(self, MainMenuScene()))
        if inputStream.keyboard.isKeyPressed(pygame.K_b):
            globals.world = globals.levels[1]
            sm.pop()
            sm.push(FadeTransitionScene(self, GameScene()))
        if inputStream.keyboard.isKeyPressed(pygame.K_2):
            globals.world = globals.levels[3]
            sm.pop()
            sm.push(FadeTransitionScene(self, ShopScene()))
        if inputStream.keyboard.isKeyPressed(pygame.K_3):
            globals.world = globals.levels[4]
            sm.pop()
            sm.push(FadeTransitionScene(self, ArenaScene()))
    def update(self, sm, inputStream):
        self.inputSystem.update(inputStream=inputStream)
        self.collectionSystem.update()
        # self.physicsSystem = engine.PhysicsSystem()
    def draw(self, sm, window):
        hall_bg = pygame.image.load("images/Backgrounds/hall_bg.png")
        hall_bg = pygame.transform.scale(hall_bg, (GAME_WIDTH, GAME_HEIGHT))
        window.blit(hall_bg, (0, 0))
        globals.world = globals.levels[2]
        self.cameraSystem.update(window)




        font = pygame.font.SysFont('franklingothicmedium', 15)
        shop_text = "Press 2 to go to the shop"
        cell_text = "Press B to go back to the cell"
        arena_text = "Press 3 to go to the Arena"
        shop_surface = font.render(shop_text, False, '#FFFFFF')
        cell_surface = font.render(cell_text, False, '#FFFFFF')
        arena_surface = font.render(arena_text, False, '#FFFFFF')
        # shop = pygame.Rect(646, 405, 5, 50)
        window.blit(shop_surface, (500, 225))
        window.blit(cell_surface, (60, 225))
        window.blit(arena_surface, (285, 200))
        # if shop.colliderect(entity.position.rect.colliderect):
        #     window.blit(shop_surface, (500, 225))

class ShopScene(Scene):
    def __init__(self):
        self.cameraSystem = engine.CameraSystem()
        self.collectionSystem = engine.CollectionSystem()
        # self.physicsSystem = engine.PhysicsSystem()
        self.inputSystem = engine.InputSystem()
        self.shopSystem = engine.ShopSystem()
    def input(self, sm, inputStream):
        if inputStream.keyboard.isKeyPressed(pygame.K_ESCAPE):
            sm.pop()
            sm.push(FadeTransitionScene(self, MainMenuScene()))
        if inputStream.keyboard.isKeyPressed(pygame.K_b):
            globals.world = globals.levels[2]
            sm.pop()
            sm.push(FadeTransitionScene(self, HallScene()))
    def update(self, sm, inputStream):
        self.inputSystem.update(inputStream=inputStream)
        self.collectionSystem.update()
        # self.physicsSystem = engine.PhysicsSystem()
        self.shopSystem.update()
    def draw(self, sm, window):
        shop_bg = pygame.image.load("images/Backgrounds/shop_bg.png")
        shop_bg = pygame.transform.scale(shop_bg, (GAME_WIDTH, GAME_HEIGHT))
        window.blit(shop_bg, (0, 0))
        globals.world = globals.levels[3]
        window.blit(utilities.sword_surface, (240, 325))
        window.blit(utilities.armor_surface, (320, 325))
        window.blit(utilities.potion_surface, (435, 325))
        window.blit(utilities.scost_surface, (240, 340))
        window.blit(utilities.acost_surface, (312, 340))
        window.blit(utilities.pcost_surface, (430, 340))
        self.cameraSystem.update(window)
        font = pygame.font.SysFont('franklingothicmedium', 15)
        hall_surface = font.render(utilities.hall_text, False, '#FFFFFF')
        window.blit(hall_surface, (460, 225))
        utilities.makeShopKeeper(250, 245)


class ArenaScene(Scene):
    def __init__(self):
        self.inputSystem = engine.InputSystem()
        # self.cameraSystem = engine.CameraSystem()
        self.cameraSystem1 = engine.CameraSystem1()
        # self.physicsSystem = engine.PhysicsSystem()
    def input(self, sm, inputStream):
        if inputStream.keyboard.isKeyPressed(pygame.K_ESCAPE):
            sm.pop()
            sm.push(FadeTransitionScene(self, MainMenuScene()))
    def update(self, sm, inputStream):
        self.inputSystem.update(inputStream=inputStream)
        pygame.time.get_ticks()
        # self.physicsSystem = engine.PhysicsSystem()
        # self.cameraSystem1.update()
    def draw(self, sm, window):
        # fight.arena(window)
        arena_bg = pygame.image.load("images/Arena/arena_bg.png")
        arena_bg = pygame.transform.scale(arena_bg, (GAME_WIDTH, GAME_HEIGHT))
        window.blit(arena_bg, (0, 0))
        globals.world = globals.levels[4]
        # self.cameraSystem.update(window)
        self.cameraSystem1.update(window)

class TransitionScene(Scene):
    def __init__(self, fromScene, toScene):
        self.currentPercentage = 0
        self.fromScene = fromScene
        self.toScene = toScene
    def update(self, sm, inputStream):
        self.currentPercentage += 1
        if self.currentPercentage >= 100:
            sm.pop()
            sm.push(self.toScene)

class FadeTransitionScene(TransitionScene):
    def draw(self, sm, window):
        if self.currentPercentage < 50:
            self.fromScene.draw(sm, window)
        else:
            self.toScene.draw(sm, window)

        overlay = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
        alpha = int(abs((255 - ((255/50)*self.currentPercentage))))
        overlay.set_alpha((255 - alpha))
        overlay.fill(BLACK)
        window.blit(overlay, (0, 0))

class SceneManager:
    def __init__(self):
        self.scenes = []

    def enterScene(self):
        if len(self.scenes) > 0:
            self.scenes[-1].onEnter()

    def exitScene(self):
        if len(self.scenes) > 0:
            self.scenes[-1].onExit()

    def input(self, inputStream):
        if len(self.scenes) > 0:
            self.scenes[-1].input(self, inputStream)

    def update(self, inputStream):
        if len(self.scenes) > 0:
            self.scenes[-1].update(self, inputStream)

    def draw(self, window):
        if len(self.scenes) > 0:
            self.scenes[-1].draw(self, window)
        pygame.display.flip()

    def push(self, scene):
        # exit current scene
        if len(self.scenes) > 0:
            self.scenes[-1].onExit()
        self.scenes.append(scene)
        if len(self.scenes) > 0:
            self.scenes[-1].onEnter()
        # enter new scene
    def pop(self):
        self.exitScene()
        self.scenes.pop()
        self.enterScene()

    def set(self, scene):
        while len(self.scenes) > 0:
            self.pop()
        self.push(scene)

