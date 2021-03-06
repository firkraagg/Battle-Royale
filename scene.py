import pygame
import engine
import button
import globals
import utilities
from globals import *
import level

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
    def __init__(self):
        globals.soundManager.playMusic("menu_music")
    def draw(self, sm, window):
        button1 = button.Button('Start new game', 160, 50, (270, 170), 6)
        button2 = button.Button('Quit', 110, 30, (295, 250), 6)
        menu_bg = pygame.image.load("images/Backgrounds/menu_bg.png")
        window.blit(menu_bg, (0, 0))
        button1.draw()
        button2.draw()
        if button1.pressed:
            sm.push(FadeTransitionScene(self, IntroScene()))
        elif button2.pressed:
            pygame.quit()

class IntroScene(Scene):
    def input(self, sm, inputStream):
        if inputStream.keyboard.isKeyPressed(pygame.K_SPACE):
            globals.world = globals.levels[1]
            sm.push(FadeTransitionScene(self, PrisonScene()))
        if inputStream.keyboard.isKeyPressed(pygame.K_ESCAPE):
            sm.pop()
            sm.push(FadeTransitionScene(self, MainMenuScene()))

    def draw(self, sm, window):
        mid_w, mid_h = GAME_WIDTH / 2, GAME_HEIGHT / 2
        window.fill(GREY)
        utilities.intro_text(window, 'Press space to skip', 20, mid_w, mid_h + 210 )

class PrisonScene(Scene):
    def __init__(self):
        self.cameraSystem = engine.CameraSystem()
        self.collectionSystem = engine.CollectionSystem()
        self.physicsSystem = engine.PhysicsSystem()
        self.inputSystem = engine.InputSystem()
        globals.soundManager.playMusic("prison_music")
    def input(self, sm, inputStream):
        if inputStream.keyboard.isKeyPressed(pygame.K_ESCAPE):
            sm.pop()
            sm.push(FadeTransitionScene(self, MainMenuScene()))
        if inputStream.keyboard.isKeyPressed(pygame.K_1):
            globals.soundManager.playSound("room_doors")
            globals.world = globals.levels[2]
            sm.push(FadeTransitionScene(self, HallScene()))
    def update(self, sm, inputStream):
        self.inputSystem.update(inputStream=inputStream)
        self.collectionSystem.update()
        self.physicsSystem.update()
    def draw(self, sm, window):
        globals.world = globals.levels[1]
        utilities.npcName(window, "Spiculus", WHITE, 370, 215)
        self.cameraSystem.update(window)

class HallScene(Scene):
    def __init__(self):
        self.cameraSystem = engine.CameraSystem()
        self.collectionSystem = engine.CollectionSystem()
        self.physicsSystem = engine.PhysicsSystem()
        self.inputSystem = engine.InputSystem()
        globals.soundManager.playMusic("game_music")
    def input(self, sm, inputStream):
        if inputStream.keyboard.isKeyPressed(pygame.K_ESCAPE):
            sm.pop()
            sm.push(FadeTransitionScene(self, MainMenuScene()))
        if inputStream.keyboard.isKeyPressed(pygame.K_b):
            globals.soundManager.playSound("room_doors")
            globals.world = globals.levels[1]
            sm.pop()
            sm.push(FadeTransitionScene(self, PrisonScene()))
        if inputStream.keyboard.isKeyPressed(pygame.K_2):
            globals.soundManager.playSound("room_doors")
            globals.world = globals.levels[3]
            sm.pop()
            sm.push(FadeTransitionScene(self, ShopScene()))
        if inputStream.keyboard.isKeyPressed(pygame.K_3):
            globals.soundManager.playSound("arena_doors")
            sm.pop()
            sm.push(FadeTransitionScene(self, ArenaIntroScene()))
    def update(self, sm, inputStream):
        self.inputSystem.update(inputStream=inputStream)
        self.collectionSystem.update()
        self.physicsSystem.update()
    def draw(self, sm, window):
        hall_bg = pygame.image.load("images/Backgrounds/hall_bg.png")
        hall_bg = pygame.transform.scale(hall_bg, (GAME_WIDTH, GAME_HEIGHT))
        window.blit(hall_bg, (0, 0))
        level.save_button.draw()
        globals.world = globals.levels[2]
        self.cameraSystem.update(window)
        font = pygame.font.SysFont('franklingothicmedium', 15)
        shop_text = "Press 2 to go to the shop"
        cell_text = "Press B to go back to the cell"
        arena_text = "Press 3 to go to the Arena"
        shop_surface = font.render(shop_text, False, '#FFFFFF')
        cell_surface = font.render(cell_text, False, '#FFFFFF')
        arena_surface = font.render(arena_text, False, '#FFFFFF')
        window.blit(shop_surface, (500, 225))
        window.blit(cell_surface, (60, 225))
        window.blit(arena_surface, (285, 200))
        window.blit(utilities.load_hintSurface1, (10, 420))
        window.blit(utilities.load_hintSurface2, (10, 440))

class ShopScene(Scene):
    def __init__(self):
        self.cameraSystem = engine.CameraSystem()
        self.collectionSystem = engine.CollectionSystem()
        self.physicsSystem = engine.PhysicsSystem()
        self.inputSystem = engine.InputSystem()
        self.shopSystem = engine.ShopSystem()
    def input(self, sm, inputStream):
        if inputStream.keyboard.isKeyPressed(pygame.K_ESCAPE):
            sm.pop()
            sm.push(FadeTransitionScene(self, MainMenuScene()))
        if inputStream.keyboard.isKeyPressed(pygame.K_b):
            globals.soundManager.playSound("room_doors")
            globals.world = globals.levels[2]
            sm.pop()
            sm.push(FadeTransitionScene(self, HallScene()))
    def update(self, sm, inputStream):
        self.inputSystem.update(inputStream=inputStream)
        self.collectionSystem.update()
        self.physicsSystem.update()
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
        window.blit(utilities.shop_hintSurface, (20, 450))
        self.cameraSystem.update(window)
        font = pygame.font.SysFont('franklingothicmedium', 15)
        hall_surface = font.render(utilities.hall_text, False, '#FFFFFF')
        window.blit(hall_surface, (460, 225))
        utilities.makeShopKeeper(250, 245)

class ArenaIntroScene(Scene):
    def input(self, sm, inputStream):
        if inputStream.keyboard.isKeyPressed(pygame.K_SPACE):
            sm.push(FadeTransitionScene(self, ArenaScene()))
            globals.world = globals.levels[4]
        if inputStream.keyboard.isKeyPressed(pygame.K_ESCAPE):
            sm.pop()
            sm.push(FadeTransitionScene(self, MainMenuScene()))

    def draw(self, sm, window):
        arena_intro_bg = pygame.image.load("images/Backgrounds/arena_intro_bg.png")
        arena_intro_bg = pygame.transform.scale(arena_intro_bg, (GAME_WIDTH, GAME_HEIGHT))
        window.blit(arena_intro_bg, (0, 0))
        mid_w, mid_h = GAME_WIDTH / 2, GAME_HEIGHT / 2
        window.blit(utilities.arena_intro_surface1, (mid_w - 180, mid_h - 120))
        window.blit(utilities.arena_intro_surface2, (mid_w - 230, mid_h - 70))
        window.blit(utilities.arena_intro_surface3, (mid_w - 250, mid_h - 45))
        window.blit(utilities.skip_surface, (mid_w - 85, mid_h + 210))

class ArenaScene(Scene):
    def __init__(self):
        self.inputSystem = engine.InputSystem()
        self.cameraSystem1 = engine.CameraSystem1()
        self.physicsSystem = engine.PhysicsSystem()
        self.conditionSystem = engine.ConditionSystem()
        globals.soundManager.playMusic("arena_music")
    def input(self, sm, inputStream):
        if inputStream.keyboard.isKeyPressed(pygame.K_ESCAPE):
            sm.pop()
            sm.push(FadeTransitionScene(self, MainMenuScene()))
        for entity in globals.world.entities:
            if entity.score.score >= 30:
                if inputStream.keyboard.isKeyPressed(pygame.K_4):
                    globals.soundManager.playSound("arena_doors")
                    sm.pop()
                    sm.push(FadeTransitionScene(self, HallScene1()))
        if level.yes == True:
            sm.pop()
            # globals.world = globals.levels[2]
            sm.push(FadeTransitionScene(self, HallScene()))
            globals.world = globals.levels[2]

    def update(self, sm, inputStream):
        self.inputSystem.update(inputStream=inputStream)
        self.physicsSystem.update()
        self.conditionSystem.update()
    def draw(self, sm, window):
        # load_image = pygame.image.load("images/load_image.png")
        # load_image = pygame.transform.scale(load_image, (120, 60))
        window.blit(utilities.arena_bg, (0, 0))
        # load_button = button.Button1(window, 430, 430, load_image, 40, 40)
        for otherEntity in globals.world.entities:
            if otherEntity.type == "enemy":
                if otherEntity.enemyHealth.enemyHealth != 0:
                    level.load_button.draw()
        globals.world = globals.levels[4]
        self.cameraSystem1.update(window)

class HallScene1(Scene):
    def __init__(self):
        self.cameraSystem = engine.CameraSystem()
        self.collectionSystem = engine.CollectionSystem()
        self.physicsSystem = engine.PhysicsSystem()
        self.inputSystem = engine.InputSystem()
        globals.soundManager.playMusic("game_music")
    def input(self, sm, inputStream):
        if inputStream.keyboard.isKeyPressed(pygame.K_ESCAPE):
            sm.pop()
            sm.push(FadeTransitionScene(self, MainMenuScene()))
        if inputStream.keyboard.isKeyPressed(pygame.K_2):
            globals.soundManager.playSound("room_doors")
            sm.pop()
            sm.push(FadeTransitionScene(self, ShopScene1()))
            globals.world = globals.levels[6]
        if inputStream.keyboard.isKeyPressed(pygame.K_3):
            globals.soundManager.playSound("arena_doors")
            globals.world = globals.levels[7]
            sm.pop()
            sm.push(FadeTransitionScene(self, ArenaScene1()))
    def update(self, sm, inputStream):
        self.inputSystem.update(inputStream=inputStream)
        self.collectionSystem.update()
        self.physicsSystem.update()
    def draw(self, sm, window):
        hall_bg = pygame.image.load("images/Backgrounds/hall_bg.png")
        hall_bg = pygame.transform.scale(hall_bg, (GAME_WIDTH, GAME_HEIGHT))
        window.blit(hall_bg, (0, 0))
        level.save_button.draw()
        window.blit(utilities.shield_hintSurface, (20, 450))
        globals.world = globals.levels[5]
        self.cameraSystem.update(window)
        font = pygame.font.SysFont('franklingothicmedium', 15)
        shop_text = "Press 2 to go to the shop"
        arena_text = "Press 3 to go to the Arena"
        shop_surface = font.render(shop_text, False, '#FFFFFF')
        arena_surface = font.render(arena_text, False, '#FFFFFF')
        window.blit(shop_surface, (500, 225))
        window.blit(arena_surface, (285, 200))

class ShopScene1(Scene):
    def __init__(self):
        self.cameraSystem = engine.CameraSystem()
        self.collectionSystem = engine.CollectionSystem()
        self.physicsSystem = engine.PhysicsSystem()
        self.inputSystem = engine.InputSystem()
        self.shopSystem = engine.ShopSystem()
    def input(self, sm, inputStream):
        if inputStream.keyboard.isKeyPressed(pygame.K_ESCAPE):
            sm.pop()
            sm.push(FadeTransitionScene(self, MainMenuScene()))
        if inputStream.keyboard.isKeyPressed(pygame.K_b):
            globals.soundManager.playSound("room_doors")
            globals.world = globals.levels[5]
            sm.pop()
            sm.push(FadeTransitionScene(self, HallScene1()))
    def update(self, sm, inputStream):
        self.inputSystem.update(inputStream=inputStream)
        self.collectionSystem.update()
        self.physicsSystem.update()
        self.shopSystem.update()
    def draw(self, sm, window):
        shop_bg = pygame.image.load("images/Backgrounds/shop_bg.png")
        shop_bg = pygame.transform.scale(shop_bg, (GAME_WIDTH, GAME_HEIGHT))
        window.blit(shop_bg, (0, 0))
        globals.world = globals.levels[6]
        window.blit(utilities.sword1_surface, (240, 322))
        window.blit(utilities.sword1_surface1, (240, 332))
        window.blit(utilities.armor_surface, (320, 325))
        window.blit(utilities.potion_surface, (435, 325))
        window.blit(utilities.scost_surface, (240, 340))
        window.blit(utilities.acost_surface, (312, 340))
        window.blit(utilities.pcost_surface, (430, 340))
        window.blit(utilities.shop_hintSurface, (20, 450))
        self.cameraSystem.update(window)
        font = pygame.font.SysFont('franklingothicmedium', 15)
        hall_surface = font.render(utilities.hall_text, False, '#FFFFFF')
        window.blit(hall_surface, (460, 225))
        utilities.makeShopKeeper(250, 245)

class ArenaScene1(Scene):
    def __init__(self):
        self.inputSystem = engine.InputSystem()
        self.cameraSystem1 = engine.CameraSystem1()
        self.physicsSystem = engine.PhysicsSystem()
        globals.soundManager.playMusic("arena_music")
    def input(self, sm, inputStream):
        if inputStream.keyboard.isKeyPressed(pygame.K_ESCAPE):
            sm.pop()
            sm.push(FadeTransitionScene(self, MainMenuScene()))
        for entity in globals.world.entities:
            if entity.score.score >= 30:
                if inputStream.keyboard.isKeyPressed(pygame.K_4):
                    globals.soundManager.playSound("arena_doors")
                    sm.pop()
                    sm.push(FadeTransitionScene(self, HallScene2()))
                    globals.world = globals.levels[8]

    def update(self, sm, inputStream):
        self.inputSystem.update(inputStream=inputStream)
        self.physicsSystem.update()
    def draw(self, sm, window):
        window.blit(utilities.arena_bg, (0, 0))
        globals.world = globals.levels[7]
        for otherEntity in globals.world.entities:
            if otherEntity.type == "enemy":
                if otherEntity.enemyHealth.enemyHealth != 0:
                    level.load_button.draw()
        self.cameraSystem1.update(window)


class HallScene2(Scene):
    def __init__(self):
        self.cameraSystem = engine.CameraSystem()
        self.collectionSystem = engine.CollectionSystem()
        self.physicsSystem = engine.PhysicsSystem()
        self.inputSystem = engine.InputSystem()
        globals.soundManager.playMusic("game_music")
    def input(self, sm, inputStream):
        if inputStream.keyboard.isKeyPressed(pygame.K_ESCAPE):
            sm.pop()
            sm.push(FadeTransitionScene(self, MainMenuScene()))
        if inputStream.keyboard.isKeyPressed(pygame.K_2):
            globals.soundManager.playSound("room_doors")
            sm.pop()
            sm.push(FadeTransitionScene(self, ShopScene2()))
            globals.world = globals.levels[9]
        if inputStream.keyboard.isKeyPressed(pygame.K_3):
            globals.soundManager.playSound("arena_doors")
            globals.world = globals.levels[10]
            sm.pop()
            sm.push(FadeTransitionScene(self, ArenaScene2()))
    def update(self, sm, inputStream):
        self.inputSystem.update(inputStream=inputStream)
        self.collectionSystem.update()
        self.physicsSystem.update()
    def draw(self, sm, window):
        hall_bg = pygame.image.load("images/Backgrounds/hall_bg.png")
        hall_bg = pygame.transform.scale(hall_bg, (GAME_WIDTH, GAME_HEIGHT))
        window.blit(hall_bg, (0, 0))
        level.save_button.draw()
        window.blit(utilities.bow_hintSurface, (20, 450))
        window.blit(utilities.useShield_hintSurface, (20, 430))
        globals.world = globals.levels[8]
        self.cameraSystem.update(window)
        font = pygame.font.SysFont('franklingothicmedium', 15)
        shop_text = "Press 2 to go to the shop"
        arena_text = "Press 3 to go to the Arena"
        shop_surface = font.render(shop_text, False, '#FFFFFF')
        arena_surface = font.render(arena_text, False, '#FFFFFF')
        window.blit(shop_surface, (500, 225))
        window.blit(arena_surface, (285, 200))

class ShopScene2(Scene):
    def __init__(self):
        self.cameraSystem = engine.CameraSystem()
        self.collectionSystem = engine.CollectionSystem()
        self.physicsSystem = engine.PhysicsSystem()
        self.inputSystem = engine.InputSystem()
        self.shopSystem = engine.ShopSystem()
    def input(self, sm, inputStream):
        if inputStream.keyboard.isKeyPressed(pygame.K_ESCAPE):
            sm.pop()
            sm.push(FadeTransitionScene(self, MainMenuScene()))
        if inputStream.keyboard.isKeyPressed(pygame.K_b):
            globals.soundManager.playSound("room_doors")
            globals.world = globals.levels[8]
            sm.pop()
            sm.push(FadeTransitionScene(self, HallScene2()))
    def update(self, sm, inputStream):
        self.inputSystem.update(inputStream=inputStream)
        self.collectionSystem.update()
        self.physicsSystem.update()
        self.shopSystem.update()
    def draw(self, sm, window):
        shop_bg = pygame.image.load("images/Backgrounds/shop_bg.png")
        shop_bg = pygame.transform.scale(shop_bg, (GAME_WIDTH, GAME_HEIGHT))
        window.blit(shop_bg, (0, 0))
        globals.world = globals.levels[9]
        window.blit(utilities.shield_surface, (250, 325))
        window.blit(utilities.armor_surface, (320, 325))
        window.blit(utilities.potion_surface, (435, 325))
        window.blit(utilities.scost_surface, (240, 340))
        window.blit(utilities.acost_surface, (312, 340))
        window.blit(utilities.pcost_surface, (430, 340))
        window.blit(utilities.shop_hintSurface, (20, 450))
        self.cameraSystem.update(window)
        font = pygame.font.SysFont('franklingothicmedium', 15)
        hall_surface = font.render(utilities.hall_text, False, '#FFFFFF')
        window.blit(hall_surface, (460, 225))
        utilities.makeShopKeeper(250, 245)

class ArenaScene2(Scene):
    def __init__(self):
        self.inputSystem = engine.InputSystem()
        self.cameraSystem1 = engine.CameraSystem1()
        self.physicsSystem = engine.PhysicsSystem()
        globals.soundManager.playMusic("arena_music")
    def input(self, sm, inputStream):
        if inputStream.keyboard.isKeyPressed(pygame.K_ESCAPE):
            sm.pop()
            sm.push(FadeTransitionScene(self, MainMenuScene()))
        for entity in globals.world.entities:
            if entity.score.score >= 30:
                if inputStream.keyboard.isKeyPressed(pygame.K_4):
                    globals.soundManager.playSound("arena_doors")
                    sm.pop()
                    sm.push(FadeTransitionScene(self, HallScene3()))
                    globals.world = globals.levels[11]

    def update(self, sm, inputStream):
        self.inputSystem.update(inputStream=inputStream)
        self.physicsSystem.update()
    def draw(self, sm, window):
        window.blit(utilities.arena_bg, (0, 0))
        globals.world = globals.levels[10]
        for otherEntity in globals.world.entities:
            if otherEntity.type == "enemy":
                if otherEntity.enemyHealth.enemyHealth != 0:
                    level.load_button.draw()
        self.cameraSystem1.update(window)

class HallScene3(Scene):
    def __init__(self):
        self.cameraSystem = engine.CameraSystem()
        self.collectionSystem = engine.CollectionSystem()
        self.physicsSystem = engine.PhysicsSystem()
        self.inputSystem = engine.InputSystem()
        globals.soundManager.playMusic("game_music")
    def input(self, sm, inputStream):
        if inputStream.keyboard.isKeyPressed(pygame.K_ESCAPE):
            sm.pop()
            sm.push(FadeTransitionScene(self, MainMenuScene()))
        if inputStream.keyboard.isKeyPressed(pygame.K_2):
            globals.soundManager.playSound("room_doors")
            sm.pop()
            sm.push(FadeTransitionScene(self, ShopScene3()))
            globals.world = globals.levels[12]
        if inputStream.keyboard.isKeyPressed(pygame.K_3):
            globals.soundManager.playSound("arena_doors")
            globals.world = globals.levels[13]
            sm.pop()
            sm.push(FadeTransitionScene(self, ArenaScene3()))
    def update(self, sm, inputStream):
        self.inputSystem.update(inputStream=inputStream)
        self.collectionSystem.update()
        self.physicsSystem.update()
    def draw(self, sm, window):
        hall_bg = pygame.image.load("images/Backgrounds/hall_bg.png")
        hall_bg = pygame.transform.scale(hall_bg, (GAME_WIDTH, GAME_HEIGHT))
        window.blit(hall_bg, (0, 0))
        level.save_button.draw()
        window.blit(utilities.poisonArrow_hintSurface1, (20, 410))
        window.blit(utilities.poisonArrow_hintSurface2, (20, 430))
        window.blit(utilities.poisonArrow_hintSurface3, (20, 450))
        globals.world = globals.levels[11]
        self.cameraSystem.update(window)
        font = pygame.font.SysFont('franklingothicmedium', 15)
        shop_text = "Press 2 to go to the shop"
        arena_text = "Press 3 to go to the Arena"
        shop_surface = font.render(shop_text, False, '#FFFFFF')
        arena_surface = font.render(arena_text, False, '#FFFFFF')
        window.blit(shop_surface, (500, 225))
        window.blit(arena_surface, (285, 200))

class ShopScene3(Scene):
    def __init__(self):
        self.cameraSystem = engine.CameraSystem()
        self.collectionSystem = engine.CollectionSystem()
        self.physicsSystem = engine.PhysicsSystem()
        self.inputSystem = engine.InputSystem()
        self.shopSystem = engine.ShopSystem()
    def input(self, sm, inputStream):
        if inputStream.keyboard.isKeyPressed(pygame.K_ESCAPE):
            sm.pop()
            sm.push(FadeTransitionScene(self, MainMenuScene()))
        if inputStream.keyboard.isKeyPressed(pygame.K_b):
            globals.soundManager.playSound("room_doors")
            globals.world = globals.levels[11]
            sm.pop()
            sm.push(FadeTransitionScene(self, HallScene3()))
    def update(self, sm, inputStream):
        self.inputSystem.update(inputStream=inputStream)
        self.collectionSystem.update()
        self.physicsSystem.update()
        self.shopSystem.update()
    def draw(self, sm, window):
        shop_bg1 = pygame.image.load("images/Backgrounds/shop_bg1.png")
        shop_bg1 = pygame.transform.scale(shop_bg1, (GAME_WIDTH, GAME_HEIGHT))
        window.blit(shop_bg1, (0, 0))
        globals.world = globals.levels[12]
        window.blit(utilities.shield_surface, (250, 325))
        window.blit(utilities.armor_surface, (320, 325))
        window.blit(utilities.potion_surface, (435, 325))
        window.blit(utilities.scost_surface, (240, 340))
        window.blit(utilities.acost_surface, (312, 340))
        window.blit(utilities.pcost_surface, (430, 340))
        window.blit(utilities.shop_hintSurface, (20, 450))
        window.blit(utilities.poisonPotion_surface, (560, 325))
        window.blit(utilities.pcost_surface, (570, 340))
        self.cameraSystem.update(window)
        font = pygame.font.SysFont('franklingothicmedium', 15)
        hall_surface = font.render(utilities.hall_text, False, '#FFFFFF')
        window.blit(hall_surface, (460, 225))
        utilities.makeShopKeeper(250, 245)

class ArenaScene3(Scene):
    def __init__(self):
        self.inputSystem = engine.InputSystem()
        self.cameraSystem1 = engine.CameraSystem1()
        self.physicsSystem = engine.PhysicsSystem()
        self.conditionSystem = engine.ConditionSystem()
        globals.soundManager.playMusic("arena_music")
    def input(self, sm, inputStream):
        if inputStream.keyboard.isKeyPressed(pygame.K_ESCAPE):
            sm.pop()
            sm.push(FadeTransitionScene(self, MainMenuScene()))
        for entity in globals.world.entities:
            if entity.score.score >= 30:
                if inputStream.keyboard.isKeyPressed(pygame.K_4):
                    globals.soundManager.playSound("arena_doors")
                    sm.pop()
                    sm.push(FadeTransitionScene(self, HallScene4()))
                    globals.world = globals.levels[14]

    def update(self, sm, inputStream):
        self.inputSystem.update(inputStream=inputStream)
        self.physicsSystem.update()
        self.conditionSystem.update()
    def draw(self, sm, window):
        window.blit(utilities.arena_bg, (0, 0))
        globals.world = globals.levels[13]
        for otherEntity in globals.world.entities:
            if otherEntity.type == "enemy":
                if otherEntity.enemyHealth.enemyHealth != 0:
                    level.load_button.draw()
        self.cameraSystem1.update(window)

class HallScene4(Scene):
    def __init__(self):
        self.cameraSystem = engine.CameraSystem()
        self.collectionSystem = engine.CollectionSystem()
        self.physicsSystem = engine.PhysicsSystem()
        self.inputSystem = engine.InputSystem()
        globals.soundManager.playMusic("game_music")
    def input(self, sm, inputStream):
        if inputStream.keyboard.isKeyPressed(pygame.K_ESCAPE):
            sm.pop()
            sm.push(FadeTransitionScene(self, MainMenuScene()))
        if inputStream.keyboard.isKeyPressed(pygame.K_2):
            globals.soundManager.playSound("room_doors")
            sm.pop()
            sm.push(FadeTransitionScene(self, ShopScene4()))
            globals.world = globals.levels[15]
        if inputStream.keyboard.isKeyPressed(pygame.K_3):
            globals.soundManager.playSound("arena_doors")
            globals.world = globals.levels[16]
            sm.pop()
            sm.push(FadeTransitionScene(self, ArenaScene4()))
    def update(self, sm, inputStream):
        self.inputSystem.update(inputStream=inputStream)
        self.collectionSystem.update()
        self.physicsSystem.update()
    def draw(self, sm, window):
        hall_bg = pygame.image.load("images/Backgrounds/hall_bg.png")
        hall_bg = pygame.transform.scale(hall_bg, (GAME_WIDTH, GAME_HEIGHT))
        window.blit(hall_bg, (0, 0))
        level.save_button.draw()
        window.blit(utilities.boss_hintSurface, (20, 430))
        globals.world = globals.levels[14]
        self.cameraSystem.update(window)
        font = pygame.font.SysFont('franklingothicmedium', 15)
        shop_text = "Press 2 to go to the shop"
        arena_text = "Press 3 to go to the Arena"
        shop_surface = font.render(shop_text, False, '#FFFFFF')
        arena_surface = font.render(arena_text, False, '#FFFFFF')
        window.blit(shop_surface, (500, 225))
        window.blit(arena_surface, (285, 200))

class ShopScene4(Scene):
    def __init__(self):
        self.cameraSystem = engine.CameraSystem()
        self.collectionSystem = engine.CollectionSystem()
        self.physicsSystem = engine.PhysicsSystem()
        self.inputSystem = engine.InputSystem()
        self.shopSystem = engine.ShopSystem()
    def input(self, sm, inputStream):
        if inputStream.keyboard.isKeyPressed(pygame.K_ESCAPE):
            sm.pop()
            sm.push(FadeTransitionScene(self, MainMenuScene()))
        if inputStream.keyboard.isKeyPressed(pygame.K_b):
            globals.soundManager.playSound("room_doors")
            globals.world = globals.levels[14]
            sm.pop()
            sm.push(FadeTransitionScene(self, HallScene4()))
    def update(self, sm, inputStream):
        self.inputSystem.update(inputStream=inputStream)
        self.collectionSystem.update()
        self.physicsSystem.update()
        self.shopSystem.update()
    def draw(self, sm, window):
        shop_bg1 = pygame.image.load("images/Backgrounds/shop_bg1.png")
        shop_bg1 = pygame.transform.scale(shop_bg1, (GAME_WIDTH, GAME_HEIGHT))
        window.blit(shop_bg1, (0, 0))
        globals.world = globals.levels[15]
        window.blit(utilities.sword_surface, (250, 325))
        window.blit(utilities.armor_surface, (320, 325))
        window.blit(utilities.potion_surface, (435, 325))
        window.blit(utilities.scost_surface, (240, 340))
        window.blit(utilities.acost_surface, (312, 340))
        window.blit(utilities.pcost_surface, (430, 340))
        window.blit(utilities.shop_hintSurface, (20, 450))
        window.blit(utilities.poisonPotion_surface, (560, 325))
        window.blit(utilities.pcost_surface, (570, 340))
        self.cameraSystem.update(window)
        font = pygame.font.SysFont('franklingothicmedium', 15)
        hall_surface = font.render(utilities.hall_text, False, '#FFFFFF')
        window.blit(hall_surface, (460, 225))
        utilities.makeShopKeeper(250, 245)

class ArenaScene4(Scene):
    def __init__(self):
        self.inputSystem = engine.InputSystem()
        self.cameraSystem1 = engine.CameraSystem1()
        self.physicsSystem = engine.PhysicsSystem()
        self.conditionSystem = engine.ConditionSystem()
        globals.soundManager.playMusic("arena_music")
    def input(self, sm, inputStream):
        if inputStream.keyboard.isKeyPressed(pygame.K_ESCAPE):
            sm.pop()
            sm.push(FadeTransitionScene(self, MainMenuScene()))
        for entity in globals.world.entities:
            if entity.score.score >= 30:
                if inputStream.keyboard.isKeyPressed(pygame.K_4):
                    globals.soundManager.playSound("arena_doors")
                    sm.pop()
                    sm.push(FadeTransitionScene(self, GameWonScene()))

    def update(self, sm, inputStream):
        self.inputSystem.update(inputStream=inputStream)
        self.physicsSystem.update()
        self.conditionSystem.update()
    def draw(self, sm, window):
        window.blit(utilities.arena_bg, (0, 0))
        globals.world = globals.levels[16]
        for otherEntity in globals.world.entities:
            if otherEntity.type == "enemy":
                if otherEntity.enemyHealth.enemyHealth != 0:
                    level.load_button.draw()
        self.cameraSystem1.update(window)

class GameWonScene(Scene):
    def __init__(self):
        globals.soundManager.playMusic("game_won_music")
    def input(self, sm, inputStream):
        if inputStream.keyboard.isKeyPressed(pygame.K_ESCAPE):
            sm.pop()
            sm.push(FadeTransitionScene(self, MainMenuScene()))
        for entity in globals.world.entities:
            if entity.score.score >= 30:
                if inputStream.keyboard.isKeyPressed(pygame.K_4):
                    globals.soundManager.playSound("arena_doors")
                    sm.pop()
                    sm.push(FadeTransitionScene(self, GameWonScene()))

    def update(self, sm, inputStream):
        pass
    def draw(self, sm, window):
        won_bg = pygame.image.load("images/Backgrounds/won_bg.png")
        won_bg = pygame.transform.scale(won_bg, (GAME_WIDTH, GAME_HEIGHT))
        window.blit(won_bg, (0, 0))
        window.blit(utilities.gameWon_surface, (180, 150))
        window.blit(utilities.mainMenu_surface, (370, 450))

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
        if len(self.scenes) > 0:
            self.scenes[-1].onExit()
        self.scenes.append(scene)
        if len(self.scenes) > 0:
            self.scenes[-1].onEnter()

    def pop(self):
        self.exitScene()
        self.scenes.pop()
        self.enterScene()

    def set(self, scene):
        while len(self.scenes) > 0:
            self.pop()
        self.push(scene)

