import pygame
import engine
import utilities
import level
import menu
import config
import globals

import utilities
from config import *



class Scene:
    def __init__(self):
        pass
    def onEnter(self):
        pass
    def onExit(self):
        pass
    def input(self, sm):
        pass
    def update(self, sm):
        pass
    def draw(self, sm, window):
        pass


class MainMenuScene(Scene):
    def draw(self, sm, window):
        button1 = menu.Button(self, 'Play Game', 160, 50, (270, 170), 6)
        button2 = menu.Button(self, 'Quit', 110, 30, (295, 255), 6)
        menu_bg = pygame.image.load("images/Background/menu_bg.png")
        window.blit(menu_bg, (0, 0))
        button1.draw()
        button2.draw()
        # button1.check_click()
        if button1.pressed:
            sm.push(FadeTransitionScene(self, LevelSelectScene()))
        elif button2.pressed:
            pygame.quit()


class LevelSelectScene(Scene):
    def input(self, sm):
        pass
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            globals.world = globals.levels[1]
            sm.push(FadeTransitionScene(self, GameScene()))
        if keys[pygame.K_ESCAPE]:
            sm.pop()
            sm.push(FadeTransitionScene(self, MainMenuScene()))

    def draw(self, sm, window):
        mid_w, mid_h = GAME_WIDTH / 2, GAME_HEIGHT / 2
        window.fill(GREY)
        utilities.intro_text(window, 'Press space to skip', 20, mid_w, mid_h + 210 )



class GameScene(Scene):
    def __init__(self):
        self.cameraSystem = engine.CameraSystem()
    def input(self, sm):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            sm.pop()
            sm.push(FadeTransitionScene(self, MainMenuScene()))
        if keys[pygame.K_1]:
            globals.world = globals.levels[2]
            sm.push(FadeTransitionScene(self, HallScene()))
    def draw(self, sm, window):
        # p_background = pygame.image.load('images/Prison/prison.png')
        # p_background = pygame.transform.scale(p_background, (GAME_WIDTH, GAME_HEIGHT))
        # window.blit(p_background, (0, 0))
        # utilities.makeBackground(p_background)
        globals.world = globals.levels[1]
        utilities.npcName(window)
        self.cameraSystem.update(window)




class HallScene(Scene):
    def __init__(self):
        self.cameraSystem = engine.CameraSystem()
    def input(self, sm):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            sm.pop()
            sm.push(FadeTransitionScene(self, MainMenuScene()))
        if keys[pygame.K_b]:
            globals.world = globals.levels[1]
            sm.pop()
            sm.push(FadeTransitionScene(self, GameScene()))
        if keys[pygame.K_3]:
            globals.world = globals.levels[3]
            sm.pop()
            sm.push(FadeTransitionScene(self, ShopScene()))
        if keys[pygame.K_4]:
            globals.world = globals.levels[4]
            sm.pop()
            sm.push(FadeTransitionScene(self, ArenaScene()))

    def draw(self, sm, window):
        hall_bg = pygame.image.load("images/Hall/hall_bg.png")
        hall_bg = pygame.transform.scale(hall_bg, (GAME_WIDTH, GAME_HEIGHT))
        window.blit(hall_bg, (0, 0))
        globals.world = globals.levels[2]
        self.cameraSystem.update(window)



        font = pygame.font.SysFont('franklingothicmedium', 15)
        shop_text = "Press 3 to go to the shop"
        cell_text = "Press B to go back to the cell"
        arena_text = "Press 4 to go to the Arena"
        shop_surface = font.render(shop_text, False, '#FFFFFF')
        cell_surface = font.render(cell_text, False, '#FFFFFF')
        arena_surface = font.render(arena_text, False, '#FFFFFF')
        # shop = pygame.Rect(646, 405, 5, 50)
        window.blit(shop_surface, (500, 225))
        window.blit(cell_surface, (60, 225))
        window.blit(arena_surface, (285, 200))
        # if shop.colliderect(new_player_rect):
        #     window.blit(shop_surface, (500, 225))

class ShopScene(Scene):
    def __init__(self):
        self.cameraSystem = engine.CameraSystem()
    def input(self, sm):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            sm.pop()
            sm.push(FadeTransitionScene(self, MainMenuScene()))
        if keys[pygame.K_b]:
            globals.world = globals.levels[2]
            sm.pop()
            sm.push(FadeTransitionScene(self, HallScene()))
    def draw(self, sm, window):
        shop_bg = pygame.image.load("images/Shop/shop_bg.png")
        shop_bg = pygame.transform.scale(shop_bg, (GAME_WIDTH, GAME_HEIGHT))
        window.blit(shop_bg, (0, 0))
        globals.world = globals.levels[3]
        self.cameraSystem.update(window)
        font = pygame.font.SysFont('franklingothicmedium', 15)
        hall_text = "Press B to go back to the Hall"
        hall_surface = font.render(hall_text, False, '#FFFFFF')
        window.blit(hall_surface, (70, 225))

class ArenaScene(Scene):
    def __init__(self):
        self.cameraSystem = engine.CameraSystem()
    def input(self, sm):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            sm.pop()
            sm.push(FadeTransitionScene(self, MainMenuScene()))

    def draw(self, sm, window):
        hall_bg = pygame.image.load("images/Hall/hall_bg.png")
        hall_bg = pygame.transform.scale(hall_bg, (GAME_WIDTH, GAME_HEIGHT))
        window.blit(hall_bg, (0, 0))
        globals.world = globals.levels[4]
        self.cameraSystem.update(window)


class TransitionScene(Scene):
    def __init__(self, fromScene, toScene):
        self.currentPercentage = 0
        self.fromScene = fromScene
        self.toScene = toScene
    def update(self, sm):
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

    def input(self):
        if len(self.scenes) > 0:
            self.scenes[-1].input(self)

    def update(self):
        if len(self.scenes) > 0:
            self.scenes[-1].update(self)

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