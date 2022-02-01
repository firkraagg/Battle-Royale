import pygame

import engine
from config import *
import globals
import utilities
import menu
import random
import scene
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
        # if inputStream.keyboard.isKeyDown(entity.input.up):
        #     entity.intention.jump = True
        # else:
        #     entity.intention.jump = False
        if inputStream.keyboard.isKeyDown(entity.input.left):
            entity.intention.moveLeft = True
        else:
            entity.intention.moveLeft = False

        if inputStream.keyboard.isKeyDown(entity.input.right):
            entity.intention.moveRight = True
        else:
            entity.intention.moveRight = False

        if inputStream.keyboard.isKeyDown(entity.input.e):
            entity.intention.ePressed = True
        else:
            entity.intention.ePressed = False

class CollectionSystem(System):
    def check(self, entity):
        return entity.type == 'player' and entity.score is not None
    def updateEntity(self, window, inputStream, entity):
        for otherEntity in globals.world.entities:
            if otherEntity is not entity and otherEntity.type == 'collectable':
                if entity.position.rect.colliderect(otherEntity.position.rect):
                    globals.soundManager.playSound("coins")
                    globals.world.entities.remove(otherEntity)
                    entity.score.score += 15

class ShopSystem(System):
    def check(self, entity):
        return entity.type == 'player'
    def updateEntity(self, window, inputStream, entity):
        for otherEntity in globals.world.entities:
            if otherEntity is not entity and otherEntity.type == 'buyable':
                if entity.position.rect.colliderect(otherEntity.position.rect):
                    for event in pygame.event.get():
                        if event.type == pygame.KEYUP:
                            if event.key == pygame.K_e:
                                if otherEntity.type1 == 'sword':
                                    if entity.score.score >= 20:
                                        globals.soundManager.playSound("buying")
                                        entity.score.score -= 20
                                        entity.damage.damage += 3
                                        globals.world.entities.remove(otherEntity)
                                if otherEntity.type1 == 'sword1':
                                    if entity.score.score >= 20:
                                        globals.soundManager.playSound("buying")
                                        entity.score.score -= 20
                                        entity.damage.damage += 3
                                        entity.swordLvl.swordLvl += 1
                                        globals.world.entities.remove(otherEntity)
                                if otherEntity.type1 == 'armor':
                                    if entity.score.score >= 20:
                                        globals.soundManager.playSound("buying")
                                        entity.score.score -= 20
                                        entity.maxHealth.maxHealth += 7
                                        entity.health.health += 7
                                        globals.world.entities.remove(otherEntity)
                                if otherEntity.type1 == 'shield':
                                    if entity.score.score >= 20:
                                        globals.soundManager.playSound("buying")
                                        entity.score.score -= 20
                                        globals.world.entities.remove(otherEntity)
                                if otherEntity.type1 == 'potion':
                                    if entity.score.score >= 10:
                                        globals.soundManager.playSound("buying")
                                        entity.score.score -= 10
                                        entity.potions.potions += 1
                                        globals.world.entities.remove(otherEntity)

class PhysicsSystem(System):
    def check(self, entity):
        return entity.position is not None
    def updateEntity(self, window, inputStream, entity):
        new_x = entity.position.rect.x
        # new_y = entity.position.rect.y
        if entity.intention is not None:
            if entity.intention.moveLeft:
                new_x -= 3
                entity.direction = 'left'
                entity.state = 'walking'
            if entity.intention.moveRight:
                new_x += 3
                entity.direction = 'right'
                entity.state = 'walking'
            if not entity.intention.moveLeft and not entity.intention.moveRight:
                entity.state = 'standing'
            if entity.combat == True:
                if not entity.intention.moveLeft and not entity.intention.moveRight:
                    entity.state = "standing1"
                if entity.intention is not None:
                    if entity.intention.moveLeft:
                        new_x -= 2
                        entity.direction = 'left'
                        entity.state = 'walking1'
                    if entity.intention.moveRight:
                        new_x += 2
                        entity.direction = 'right'
                        entity.state = 'walking1'
                    if entity.intention.ePressed:
                        entity.state = 'fighting'
                    if entity.health.health == 0:
                        entity.state = "death"
                        if entity.intention.moveLeft:
                            new_x += 5
                        if entity.intention.moveRight:
                            new_x -= 5
                            entity.direction = 'left'




            # if entity.intention.jump and entity.on_ground:
            #     entity.speed -= 5

            entity.movement = True
            for otherEntity in globals.world.entities:
                enemy_x_change = random.randint(1, 5)
                enemy_x_change1 = random.randint(1, 5)
                rand_pos = random.randint(200, 400)
                rand_pos1 = random.randint(50, 100)
                if otherEntity is not entity and otherEntity.type == 'enemy':
                    if otherEntity.name == "Enemy0" or otherEntity.name == "Enemy1":
                        if otherEntity.enemyHealth.enemyHealth >= 1:
                            if otherEntity.position.rect.x <= rand_pos:
                                otherEntity.position.rect.x += enemy_x_change1
                                otherEntity.state = "walking"
                            else:
                                otherEntity.state = "walking"
                                otherEntity.position.rect.x -= enemy_x_change
                    if otherEntity.name == "Enemy2":
                        if otherEntity.enemyHealth.enemyHealth >= 1:
                            if otherEntity.position.rect.x >= rand_pos1:
                                otherEntity.position.rect.x -= enemy_x_change1
                                otherEntity.state = "walking"
                            else:
                                otherEntity.state = "walking"
                                otherEntity.position.rect.x += enemy_x_change
                    arrows = []
                    enemy_rand_attack = random.randint(10, 35)
                    enemy_rand_dmg = random.randint(10, 12)
                    if otherEntity.position.rect.colliderect(entity.position.rect):
                    #     for arrow in arrows:
                    #         window.blit(utilities.arrow_image, pygame.Rect(arrow[0], arrow[1], 200, 250))

                        # for b in range(len(arrows)):
                        #     arrows[b][0] -= 10
                        # for arrow in arrows[:]:
                        #     if arrow[0] > 720:
                        #         arrows.remove(arrow)



                        # for arrow in arrows:
                        #     if arrow.x < 720 and arrow.x > 0:
                        #         arrow.x += arrow.velocity
                        #     else:
                        #         arrows.pop(arrows.index(arrow))
                        # if len(arrows) < 1:
                        #     arrows.append(utilities.projectile(round(otherEntity.position.rect.x), 300, 6, BLACK))
                        # for arrow in arrows:
                        #     arrow.draw(window)
                        if otherEntity.name == "Enemy0":
                            if otherEntity.enemyHealth.enemyHealth >= 1 and entity.health.health >= 1:
                                otherEntity.state = "attack"
                            else:
                                otherEntity.state = "death"
                            if otherEntity.enemyHealth.enemyHealth >= 1:
                                if otherEntity.position.rect.colliderect(entity.position.rect):
                                    if entity.health.health >= 1:
                                        if enemy_rand_attack == 10:
                                            entity.health.health -= enemy_rand_dmg
                                            globals.soundManager.playSound("smash")

                        if otherEntity.position.rect.colliderect(entity.position.rect):
                            if otherEntity.name == "Enemy1":
                                if otherEntity.enemyHealth.enemyHealth >= 1 and entity.health.health >= 1:
                                    otherEntity.state = "attack"
                                    if otherEntity.enemyHealth.enemyHealth >= 1:
                                        if otherEntity.position.rect.colliderect(entity.position.rect):
                                            if entity.health.health >= 1:
                                                if enemy_rand_attack == 10:
                                                    entity.health.health -= enemy_rand_dmg
                                                    globals.soundManager.playSound("smash")

                                if entity.state == "fighting":
                                    otherEntity.state = "block"

                        if otherEntity.name == "Enemy2":
                            if otherEntity.enemyHealth.enemyHealth >= 1 and entity.health.health >= 1:
                                otherEntity.state = "walking"
                                if otherEntity.enemyHealth.enemyHealth >= 1:
                                        if entity.health.health >= 1:
                                            if enemy_rand_attack == 10:
                                                pass

                    if otherEntity.enemyHealth.enemyHealth == 0:
                        otherEntity.state = "death"

                    if entity.health.health < 1:
                        entity.health.health = 0
                    if entity.health.health == 0:
                        otherEntity.state = "walking"



        new_x_rect = pygame.Rect(int(new_x), 400, 72, 72)
        x_collision = False

        for platform in globals.world.platforms:
            if platform.colliderect(new_x_rect):
                x_collision = True
                break

        if x_collision == False:
            entity.position.rect.x = new_x


        # entity.speed += entity.acceleration
        # new_y += entity.speed
        #
        # new_y_rect = pygame.Rect(int(entity.position.rect.x), int (new_y), entity.position.rect.width, entity.position.rect.height)
        #
        # y_collision = False
        # entity.on_ground = False
        #
        # for platform in globals.world.platforms:
        #     if platform.colliderect(new_y_rect):
        #         y_collision = True
        #         entity.speed = 0
        #         if platform[1] > new_y:
        #             entity.position.rect.y = platform[1] - entity.position.rect.height
        #             entity.on_ground = True
        #         break
        # if y_collision == False:
        #     entity.position.rect.y = int(new_y)
        #
        if entity.intention is not None:
            entity.intention.moveLeft = False
            entity.intention.moveRight = False
            entity.intention.ePressed = False
        #     entity.intension.jump = False



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

        entity.combat = True

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
            utilities.draw_coinText(window, str(entity.damage.damage), 405, 52)

        if entity.maxHealth is not None:
            heart_image = pygame.image.load('images/ShopItems/heart.png')
            heart_image = pygame.transform.scale(heart_image, (80, 80))
            window.blit(heart_image, (500, 40))
            utilities.draw_coinText(window, str(entity.maxHealth.maxHealth), 550, 52)

        if entity.health is not None:
            utilities.draw_coinText(window, str(entity.health.health), 600, 400)

        if entity.enemyHealth is not None:
            utilities.draw_coinText(window, str(entity.enemyHealth.enemyHealth), 190, 400)

        utilities.npcName(window, "COINS", WHITE, 40, 20)
        utilities.npcName(window, "POTIONS", WHITE, 180, 20)
        utilities.npcName(window, "DAMAGE", WHITE, 350, 20)
        utilities.npcName(window, "HEALTH", WHITE, 510, 20)

        utilities.npcName(window, "Health:", RED, 110, 400)
        utilities.npcName(window, "Health:", RED, 520, 400)

        window.set_clip(None)
        font = pygame.font.SysFont('franklingothicmedium', 15)

        potion_image = pygame.image.load('images/ShopItems/potion.png')
        potion_button = menu.Button1(window, 530, 430, potion_image, 40, 40)
        sword_image = pygame.image.load("images/ShopItems/sword.png")
        sword_image = pygame.transform.scale(sword_image, (60, 60))
        potion = False
        potion_effect = random.randint(4, 8)
        fullhp_effect = 0
        # action_cooldown = 0
        # action_wait_time = 90
        # last = pygame.time.get_ticks()
        # wait = 2000
        # click = pygame.mouse.get_pressed()[0]
        rand = random.randint(2, 5)
        enemy_rand = random.randint(10, 12)
        p_damage = entity.damage.damage + rand
        pos = pygame.mouse.get_pos()
        hit = False
        attack = False
        damage_taken = False
        hit1 = False

        # arrows = []
        # # arrow = pygame.image.load("images/Enemy2/enemy_attack/arrow.png")
        # for otherEntity in globals.world.entities:
        #     if otherEntity is not entity and otherEntity.type == 'enemy':
        #         for arrow in arrows:
        #             if arrow.x < 720 and arrow.x > 0:
        #                 arrow.x += 10
        #                 # entity.health.health -= enemy_rand_dmg
        #                 # globals.soundManager.playSound("smash")
        #             else:
        #                 arrows.pop(arrows.index(arrow))
        #         if otherEntity.enemyHealth.enemyHealth > 0:
        #             if len(arrows) < 2:
        #                 arrows.append(utilities.projectile(otherEntity.position.rect.x + 100, 6, (BLACK), ))
        #         for arrow in arrows:
        #             arrow.draw(window)
        for otherEntity in globals.world.entities:
            if otherEntity is not entity and otherEntity.type == 'enemy':
                if entity.position.rect.colliderect(otherEntity.position.rect):
                    for event in pygame.event.get():
                        if event.type == pygame.KEYUP:
                            if event.key == pygame.K_e:
                                if otherEntity.enemyHealth.enemyHealth >= 1:
                                    if entity.health.health >= 1:
                                        if otherEntity.state == "block":
                                            if entity.swordLvl.swordLvl == 0:
                                                otherEntity.enemyHealth.enemyHealth -= 0
                                            if entity.swordLvl.swordLvl == 1:
                                                otherEntity.enemyHealth.enemyHealth -= 15
                                        if otherEntity.state == "attack":
                                            pass
                                        # otherEntity.enemyHealth.enemyHealth -= p_damage
                                        player_rand_attack = random.randint(10, 11)
                                        if otherEntity.enemyHealth.enemyHealth >= 1:
                                            if otherEntity.position.rect.colliderect(entity.position.rect):
                                                if entity.health.health >= 1:
                                                    if player_rand_attack == 10:
                                                        globals.soundManager.playSound("player_sword")
                                                        otherEntity.enemyHealth.enemyHealth -= p_damage
                                                            # otherEntity.enemyHealth.enemyHealth -= 20

                                    if otherEntity.enemyHealth.enemyHealth < 1:
                                        otherEntity.enemyHealth.enemyHealth = 0
                                        entity.score.score += 30
                                    # if otherEntity.enemyHealth.enemyHealth >= 1:
                                    #     entity.health.health -= enemy_rand
                                    #     globals.soundManager.playSound("smash")
                                        # entity.health.health -= 20
                                    # if entity.health.health < 1:
                                    #     entity.health.health = 0
                                    # if otherEntity.state == "attack":
                                    #     otherEntity.enemyHealth.enemyHealth -= 0

        if potion_button.draw():
            potion = True
        utilities.draw_text1(window, str(entity.potions.potions), font, RED, 565, 456)
        if potion == True:
            heal_amount = potion_effect
            heal_amount1 = fullhp_effect
            for entity in globals.world.entities:
                if entity.type == "player":
                    if entity.potions.potions > 0:
                        if entity.health.health < entity.maxHealth.maxHealth:
                            globals.soundManager.playSound("elixir")
                            globals.soundManager.playSound("elixir_drink")
                            entity.health.health += heal_amount
                            entity.potions.potions -= 1
                            break
                    if entity.potions.potions > 0:
                        if entity.health.health == entity.maxHealth.maxHealth:
                            globals.soundManager.playSound("elixir")
                            globals.soundManager.playSound("elixir_drink")
                            entity.health.health += heal_amount1
                            entity.potions.potions -= 1

        if entity.type == "player":
            if entity.health.health == 0:
                window.blit(utilities.lost_surface, (150, 150))

        if entity.type == "enemy":
            if entity.enemyHealth.enemyHealth == 0:
                window.blit(utilities.won_surface, (190, 150))
                for entity in globals.world.entities:
                    if entity.type == "player":
                        entity.health.health = entity.maxHealth.maxHealth


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
        window.blit(pygame.transform.flip(self.image_list[self.image_index], flip_x, flip_y), (x, y))

class deathAnimation:
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
                self.image_index -= 1

    def draw(self, window, x, y, flip_x, flip_y):
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
        self.health = 200

class EnemyHealth:
    def __init__(self):
        self.enemyHealth = 20

class Enemy1Health:
    def __init__(self):
        self.enemyHealth = 25

class Enemy2Health:
    def __init__(self):
        self.enemyHealth = 40

class MaxHealth:
    def __init__(self):
        self.maxHealth = 20

class SwordLvl:
    def __init__(self):
        self.swordLvl = 0

class Input:
    def __init__(self, left, right, e):
        # self.up = up
        self.left = left
        self.right = right
        self.e = e

class Intention:
    def __init__(self):
        self.moveLeft = False
        self.moveRight = False
        self.ePressed = False
        # self.jump = False

class Entity:
    def __init__(self):
        self.state = 'standing'
        self.type = 'normal'
        self.position = None
        self.animations = Animations()
        self.direction = 'left'
        # self.speed = 0
        # self.acceleration = 0
        self.intention = None
        # self.on_ground = False
        self.camera = None
        self.score = None
        self.potions = None
        self.damage = None
        self.health = None
        self.maxHealth = None
        self.enemyHealth = None
        self.input = None
        self.combat = False
        self.movement = False
        self.alive = True
        self.swordLvl = None
        # self.alive = True