import pygame
import engine
import level
import menu

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
        button1 = menu.Button(self, 'Play Game', 150, 50, (270, 170), 6)
        button2 = menu.Button(self, 'Quit', 100, 30, (295, 255), 6)
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
            sm.push(FadeTransitionScene(self, GameScene()))
        if keys[pygame.K_ESCAPE]:
            sm.pop()
            sm.push(FadeTransitionScene(self, MainMenuScene()))

    def draw(self, sm, window):
        mid_w, mid_h = GAME_WIDTH / 2, GAME_HEIGHT / 2
        window.fill(GREY)
        utilities.intro_text(window, 'Press space to skip', 20, mid_w, mid_h + 210 )



class GameScene(Scene):
    def input(self, sm):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            sm.pop()
            sm.push(FadeTransitionScene(self, MainMenuScene()))
        if keys[pygame.K_2]:
            sm.push(FadeTransitionScene(self, GameScene1()))

    def draw(self, sm, window):
        pass
        level.Level1()

class GameScene1(Scene):
    def input(self, sm):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            sm.pop()
            sm.push(FadeTransitionScene(self, MainMenuScene()))

    def draw(self, sm, window):
        window.fill(GREY)

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