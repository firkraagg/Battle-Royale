import pygame
from config import *
import globals
import utilities
import menu
import random
import inputstream

class System():
    def __init__(self):
        pass
    def check(self, entity):
        return True
    def update(self, window=None, inputStream=None):
        for entity in globals.world.entities:
            if self.check(entity):
                self.updateEntity(window, inputStream, entity)
    def updateEntity(self, window, inputStream, entity):
        pass

class InputSystem(System):
    def check(self, entity):
        return entity.input is not None and entity.intention is not None
    def updateEntity(self, window, inputStream, entity):
        if inputStream.keyboard.isKeyDown(entity.input.left):
            entity.intention.moveLeft = True
        else:
            entity.intention.moveLeft = False

        if inputStream.keyboard.isKeyDown(entity.input.right):
            entity.intention.moveRight = True
        else:
            entity.intention.moveRight = False

class CollectionSystem(System):
    def check(self, entity):
        return entity.type == 'player' and entity.score is not None
    def updateEntity(self, window, inputStream, entity):
        for otherEntity in globals.world.entities:
            if otherEntity is not entity and otherEntity.type == 'collectable':
                if entity.position.rect.colliderect(otherEntity.position.rect):
                    globals.world.entities.remove(otherEntity)
                    entity.score.score += 15

# class TalkingSystem(System):
#     def check(self, entity):
#         return entity.type == 'player'
#     def updateEntity(self, window, inputStream, entity):
#         font = pygame.font.SysFont('franklingothicmedium', 15)
#         gui_font = pygame.font.SysFont('franklingothicmedium', 24)
#         text0 = "press E to talk"
#         text1 = "Hello, I am Spiculus. They brought you here last night. I don't know "
#         text2 = "what crime you committed, but you got into the gladiatorial arena."
#         text3 = "You have to defeat three chosen gladiators and then you will be free. "
#         second_surface = pygame.Surface([720, 400])
#         second_surface.fill((config.BLACK))
#         dialogue_surface0 = font.render(text0, False, '#FFFFFF')
#         dialogue_surface1 = gui_font.render(text1, False, '#FFFFFF')
#         dialogue_surface2 = gui_font.render(text2, False, '#FFFFFF')
#         dialogue_surface3 = gui_font.render(text3, False, '#FFFFFF')
#         for otherEntity in globals.world.entities:
#             if otherEntity is not entity and otherEntity.type == 'friendly':
#                 if entity.position.rect.colliderect(otherEntity.position.rect):
#                     # window.blit(dialogue_surface0, (175, 240))
#                     for event in pygame.event.get():
#                         if event.type == pygame.KEYUP:
#                                     if event.key == pygame.K_e:
#                                         window.blit(second_surface, (0, 370)),
#                                         window.blit(dialogue_surface1, (0, 380)),
#                                         window.blit(dialogue_surface2, (0, 410)),
#                                         window.blit(dialogue_surface3, (0, 440))


        # for entity in globals.world.entities:
        #     if entity.type == 'friendly':
        #         if entity.position.rect.colliderect(player_rect):
        #             window.blit(dialogue_surface0, (175, 240))
        #             if event.type == pygame.KEYUP:
        #                 if event.key == pygame.K_e:
        #                     window.blit(second_surface, (0, 370)),
        #                     window.blit(dialogue_surface1, (0, 380)),
        #                     window.blit(dialogue_surface2, (0, 410)),
        #                     # window.blit(dialogue_surface3, (0, 440))

class ShopSystem(System):
    def check(self, entity):
        return entity.type == 'player' and entity.health is not None
    def updateEntity(self, window, inputStream, entity):
        for otherEntity in globals.world.entities:
            if otherEntity is not entity and otherEntity.type == 'buyable':
                if entity.position.rect.colliderect(otherEntity.position.rect):
                    for event in pygame.event.get():
                        if event.type == pygame.KEYUP:
                            if event.key == pygame.K_e:
                                if otherEntity.type1 == 'sword':
                                    if entity.score.score >= 20:
                                        entity.score.score -= 20
                                        entity.damage.damage += 3
                                        globals.world.entities.remove(otherEntity)
                                if otherEntity.type1 == 'armor':
                                    if entity.score.score >= 20:
                                        entity.score.score -= 20
                                        entity.health.health += 7
                                        globals.world.entities.remove(otherEntity)
                                if otherEntity.type1 == 'potion':
                                    if entity.score.score >= 10:
                                        entity.score.score -= 10
                                        entity.potions.potions += 1
                                        globals.world.entities.remove(otherEntity)
# class PhysicsSystem(System):
#     def check(self, entity):
#         return entity.position is not None
#     def updateEntity(self, window, inputStream, entity):
#         new_x = entity.position.rect.x
#
#         if entity.intention is not None:
#             if entity.intention.moveLeft:
#                 new_x -= 2
#                 entity.direction = 'left'
#                 entity.state = 'walking'
#             if entity.intention.moveRight:
#                 new_x += 2
#                 entity.direction = 'right'
#                 entity.state = 'walking'
#             if entity.intention.moveLeft and not entity.intention.moveRight:
#                 entity.state = 'standing'
#
#         new_x_rect = pygame.Rect(int(new_x), 400, 72, 72)
#         x_collision = False
#
#         for platform in globals.world.platforms:
#             if platform.colliderect(new_x_rect):
#                 x_collision = True
#                 break
#
#         for door in globals.world.doors:
#             if door.colliderect(new_x_rect):
#                 # window.blit(door_surface, (530, 225))
#                 pass
#         if x_collision == False:
#             entity.position.rect.x = new_x
#
#         if entity.intention is not None:
#             entity.intention.moveLeft = False
#             entity.intention.moveRight = False

class CameraSystem(System):
    def check(self, entity):
        return entity.camera is not None
    def updateEntity(self, window, inputStream, entity):

        cameraRect = entity.camera.rect
        clipRect = pygame.Rect(cameraRect.x, cameraRect.y, cameraRect.w, cameraRect.h)
        window.set_clip(clipRect)

        for e in globals.world.entities:
            s = e.state
            a = e.animations.animationList[s]
            a.draw(window, e.position.rect.x, e.position.rect.y, e.direction == 'right', False)

        if entity.score is not None:
            coin_count_image = pygame.image.load('images/Coins/coin.png')
            coin_count_image = pygame.transform.scale(coin_count_image, (25, 30))
            window.blit(coin_count_image, (50, 50))
            utilities.draw_coinText(window, str(entity.score.score), 80, 52)

        if entity.potions is not None:
            potions_image = pygame.image.load('images/ShopItems/potion.png')
            potions_image = pygame.transform.scale(potions_image, (40, 50))
            window.blit(potions_image, (200, 33))
            utilities.draw_coinText(window, str(entity.potions.potions), 235, 52)

        if entity.damage is not None:
            damage_image = pygame.image.load('images/ShopItems/sword.png')
            damage_image = pygame.transform.scale(damage_image, (80, 80))
            window.blit(damage_image, (350, 20))
            utilities.draw_coinText(window, str(entity.damage.damage), 410, 52)

        if entity.maxHealth is not None:
            heart_image = pygame.image.load('images/ShopItems/heart.png')
            heart_image = pygame.transform.scale(heart_image, (80, 80))
            window.blit(heart_image, (500, 40))
            utilities.draw_coinText(window, str(entity.maxHealth.maxHealth), 550, 52)

        utilities.npcName(window, "COINS", WHITE, 40, 20)
        utilities.npcName(window, "POTIONS", WHITE, 180, 20)
        utilities.npcName(window, "DAMAGE", WHITE, 350, 20)
        utilities.npcName(window, "HEALTH", WHITE, 510, 20)



        window.set_clip(None)

class CameraSystem1(System):
    def check(self, entity):
        return entity.camera is not None

    def updateEntity(self, window, inputStream, entity):

        cameraRect = entity.camera.rect
        clipRect = pygame.Rect(cameraRect.x, cameraRect.y, cameraRect.w, cameraRect.h)
        window.set_clip(clipRect)


        for e in globals.world.entities:
            s = e.state
            a = e.animations.animationList[s]
            a.draw(window, e.position.rect.x, e.position.rect.y, e.direction == 'left', False)

        if entity.score is not None:
            coin_count_image = pygame.image.load('images/Coins/coin.png')
            coin_count_image = pygame.transform.scale(coin_count_image, (25, 30))
            window.blit(coin_count_image, (50, 50))
            utilities.draw_coinText(window, str(entity.score.score), 80, 52)

        if entity.potions is not None:
            potions_image = pygame.image.load('images/ShopItems/potion.png')
            potions_image = pygame.transform.scale(potions_image, (40, 50))
            window.blit(potions_image, (200, 33))
            utilities.draw_coinText(window, str(entity.potions.potions), 235, 52)

        if entity.damage is not None:
            damage_image = pygame.image.load('images/ShopItems/sword.png')
            damage_image = pygame.transform.scale(damage_image, (80, 80))
            window.blit(damage_image, (350, 20))
            utilities.draw_coinText(window, str(entity.damage.damage), 405, 52)

        if entity.maxHealth is not None:
            heart_image = pygame.image.load('images/ShopItems/heart.png')
            heart_image = pygame.transform.scale(heart_image, (80, 80))
            window.blit(heart_image, (500, 40))
            utilities.draw_coinText(window, str(entity.maxHealth.maxHealth), 550, 52)


        if entity.health is not None:
            utilities.draw_coinText(window, str(entity.health.health), 190, 300)

        if entity.enemyHealth is not None:
            utilities.draw_coinText(window, str(entity.enemyHealth.enemyHealth), 600, 300)

        utilities.npcName(window, "COINS", WHITE, 40, 20)
        utilities.npcName(window, "POTIONS", WHITE, 180, 20)
        utilities.npcName(window, "DAMAGE", WHITE, 350, 20)
        utilities.npcName(window, "HEALTH", WHITE, 510, 20)

        utilities.npcName(window, "Health:", RED, 520, 300)
        utilities.npcName(window, "Health:", RED, 110, 300)

        # entity.playerHealth = entity.health
        # entity.health = utilities.Hp()
        # entity.maxHealth = utilities.MaxHp()
        # entity_healthbar = utilities.HealthBar(100, 340, utilities.Hp, utilities.MaxHp)
        # entity_healthbar.draw(entity.health)
        window.set_clip(None)
        font = pygame.font.SysFont('franklingothicmedium', 15)

        potion_image = pygame.image.load('images/ShopItems/potion.png').convert_alpha()
        potion_button = menu.Button1(window, 100, 250, potion_image, 40, 40)
        sword_image = pygame.image.load("images/ShopItems/sword.png")
        sword_image = pygame.transform.scale(sword_image, (60, 60))
        potion = False
        potion_effect = 5
        fullhp_effect = 0
        # current_fighter = 1
        # total_fighters = 2
        action_cooldown = 0
        action_wait_time = 90
        # last = pygame.time.get_ticks()
        # wait = 2000
        click = pygame.mouse.get_pressed()[0]
        rand = random.randint(0, 5)
        enemy_rand = random.randint(6, 10)
        p_damage = entity.damage.damage + rand

        if potion_button.draw():
            potion = True
        utilities.draw_text1(window, str(entity.potions.potions), font, RED, 132, 272)
        if potion == True:
            heal_amount1 = fullhp_effect
            if entity.potions.potions > 0:
                if entity.health.health == entity.maxHealth.maxHealth:
                    entity.health.health += heal_amount1
                    entity.potions.potions -= 1
            if entity.potions.potions > 0:
                if entity.health.health < entity.maxHealth.maxHealth:
                        heal_amount = potion_effect
                        entity.health.health += heal_amount
                        entity.potions.potions -= 1

        if entity.type == "player":
            if entity.current_fighter == 1:
                window.blit(utilities.turn_surface1, (320, 100))
                for otherEntity in globals.world.entities:
                    if otherEntity is not entity and otherEntity.type == 'enemy':
                        window.blit(utilities.turn_surface2, (300, 100))
                        if click:
                            if otherEntity.enemyHealth.enemyHealth >= 1:
                                if entity.health.health >= 1:
                                    otherEntity.enemyHealth.enemyHealth -= p_damage
                                    entity.current_fighter = 2
                                    if otherEntity.enemyHealth.enemyHealth < 1:
                                        otherEntity.enemyHealth.enemyHealth = 0
                                    if otherEntity.enemyHealth.enemyHealth >= 1:
                                        if entity.current_fighter == 2:
                                            # window.blit(utilities.turn_surface2, (300, 100))
                                            entity.health.health -= enemy_rand
                                            entity.current_fighter = 1
                                        if entity.health.health < 1:
                                            entity.health.health = 0


            # pygame.mouse.set_visible(True)
            # pos = pygame.mouse.get_pos()
            # if entity.type == 'enemy':
            #     if entity.rect.collidepoint(pos):
            #         pygame.mouse.set_visible(False)
            #         window.blit(sword_image, pos)
            #     # if clicked == True and bandit.alive == True:
            #     #     attack = True
            #     #     target = enemy_list[count]



class Camera:
    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)

class Position():
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

class Score:
    def __init__(self):
        self.score = 0

class Potions:
    def __init__(self):
        self.potions = 0

class Damage:
    def __init__(self):
        self.damage = 5

class Health:
    def __init__(self):
        self.health = 20

class EnemyHealth:
    def __init__(self):
        self.enemyHealth = 20

class MaxHealth:
    def __init__(self):
        self.maxHealth = 20

class Input:
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Intention:
    def __init__(self):
        self.moveLeft = False
        self.moveRight = False

class Entity:
    def __init__(self):
        self.state = 'standing'
        self.type = 'normal'
        self.position = None
        self.animations = Animations()
        self.direction = 'left'
        self.camera = None
        self.score = None
        self.potions = None
        self.damage = None
        self.health = None
        self.maxHealth = None
        self.enemyHealth = None
        self.input = None
        self.intention = None
        # self.alive = True