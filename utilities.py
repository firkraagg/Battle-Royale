import pygame
import engine
from config import *

pygame.init()
coin_im = pygame.image.load('images/Coins/coin.png')

def makeCoin(x, y):
    entity = engine.Entity()
    entity.position = engine.Position(x,y,18,20)
    entityAnimation = engine.Animation([coin_im])
    entity.animations.add('standing', entityAnimation)
    entity.type = 'collectable'
    return entity

npc1 = pygame.image.load('images/Npc/npc0.png')
npc1 = pygame.transform.scale(npc1, (135, 135))
npc1 = pygame.Rect(200, 250, 50, 60)

npc1_image1 = pygame.image.load('images/Npc/npc0.png')
npc1_image1 = pygame.transform.scale(npc1_image1, (135, 135))
npc1_image2 = pygame.image.load('images/Npc/npc1.png')
npc1_image2 = pygame.transform.scale(npc1_image2, (135, 135))
npc1_image3 = pygame.image.load('images/Npc/npc2.png')
npc1_image3 = pygame.transform.scale(npc1_image3, (135, 135))
npc1_image4 = pygame.image.load('images/Npc/npc3.png')
npc1_image4 = pygame.transform.scale(npc1_image4, (135, 135))
npc1_image5 = pygame.image.load('images/Npc/npc4.png')
npc1_image5 = pygame.transform.scale(npc1_image5, (135, 135))

def makeNpc(x, y):
    entity = engine.Entity()
    entity.position = engine.Position(x,y,80,250)
    entityAnimation = engine.Animation([npc1_image1, npc1_image2, npc1_image3, npc1_image4, npc1_image5])
    entity.animations.add('standing', entityAnimation)
    entity.type = 'friendly'
    return entity

shopkeeper_image = pygame.image.load("images/Npc/shopkeeper.png")
shopkeeper_image = pygame.transform.scale(shopkeeper_image, (135, 135))
shopkeeper_image1 = pygame.image.load("images/Npc/shopkeeper1.png")
shopkeeper_image1 = pygame.transform.scale(shopkeeper_image1, (135, 135))
shopkeeper_image2 = pygame.image.load("images/Npc/shopkeeper3.png")
shopkeeper_image2 = pygame.transform.scale(shopkeeper_image2, (135, 135))
shopkeeper_image3 = pygame.image.load("images/Npc/shopkeeper4.png")
shopkeeper_image3 = pygame.transform.scale(shopkeeper_image3, (135, 135))
def makeShopKeeper(x, y):
    entity = engine.Entity()
    entity.position = engine.Position(x, y, 80, 250)
    entityAnimation = engine.Animation([shopkeeper_image, shopkeeper_image1, shopkeeper_image3, shopkeeper_image1])
    entity.animations.add('standing', entityAnimation)
    entity.type = 'friendly'
    return entity

sword_image = pygame.image.load("images/ShopItems/sword.png")
sword_image = pygame.transform.scale(sword_image, (60, 60))
def makeSword(x, y):
    entity = engine.Entity()
    entity.position = engine.Position(x, y, 40, 40)
    entityAnimation = engine.Animation([sword_image])
    entity.animations.add('standing', entityAnimation)
    entity.type = 'buyable'
    entity.type1 = 'sword'
    return entity

potion_image = pygame.image.load("images/ShopItems/potion.png")
potion_image = pygame.transform.scale(potion_image, (30, 30))
potion_image1 = pygame.image.load("images/ShopItems/potion1.png")
potion_image1 = pygame.transform.scale(potion_image1, (30, 30))
potion_image2 = pygame.image.load("images/ShopItems/potion2.png")
potion_image2 = pygame.transform.scale(potion_image2, (30, 30))
def makePotion(x, y):
    entity = engine.Entity()
    entity.rect = pygame.rect.Rect(10, 10, 60, 40)
    entity.position = engine.Position(x, y, 60, 40)
    entityAnimation = engine.Animation([potion_image, potion_image1, potion_image2])
    entity.animations.add('standing', entityAnimation)
    entity.type = 'buyable'
    entity.type1 = 'potion'
    return entity

armor_image = pygame.image.load("images/ShopItems/armor.png")
armor_image = pygame.transform.scale(armor_image, (70, 70))
def makeArmor(x, y):
    entity = engine.Entity()
    entity.position = engine.Position(x,y,40,40)
    entityAnimation = engine.Animation([armor_image])
    entity.animations.add('standing', entityAnimation)
    entity.type = 'buyable'
    entity.type1 = 'armor'
    return entity

# class HealthBar:
#     def __init__(self, x, y, hp, max_hp):
#         self.x = x
#         self.y = y
#         self.hp = hp
#         self.max_hp = max_hp
#     def draw(self, window, hp):
#         self.hp = hp
#         ratio = self.hp / self.max_hp
#         pygame.draw.rect(window, RED, (self.x, self.y, 150, 20))
#         pygame.draw.rect(window, GREEN, (self.x, self.y, 150 * ratio, 20))
#
# class Hp:
#     def __init__(self, hp):
#         self.hp = hp
#
# class MaxHp:
#     def __init__(self, max_hp):
#         self.max_hp = max_hp


player_stand0 = pygame.image.load('images/Player/player_standing/img0.png')
player_stand0 = pygame.transform.scale(player_stand0, (102, 102))
player_stand1 = pygame.image.load('images/Player/player_standing/img1.png')
player_stand1 = pygame.transform.scale(player_stand1, (102, 102))
player_stand2 = pygame.image.load('images/Player/player_standing/img2.png')
player_stand2 = pygame.transform.scale(player_stand2, (102, 102))
player_stand3 = pygame.image.load('images/Player/player_standing/img3.png')
player_stand3 = pygame.transform.scale(player_stand3, (102, 102))
player_stand4 = pygame.image.load('images/Player/player_standing/img2.png')
player_stand4 = pygame.transform.scale(player_stand2, (102, 102))
player_stand5 = pygame.image.load('images/Player/player_standing/img5.png')
player_stand5 = pygame.transform.scale(player_stand5, (102, 102))

player_walk0 = pygame.image.load('images/Player/player_walking/p00.png')
player_walk0 = pygame.transform.scale(player_walk0, (102, 102))
player_walk1 = pygame.image.load('images/Player/player_walking/p01.png')
player_walk1 = pygame.transform.scale(player_walk1, (102, 102))
player_walk2 = pygame.image.load('images/Player/player_walking/p02.png')
player_walk2 = pygame.transform.scale(player_walk2, (102, 102))
player_walk3 = pygame.image.load('images/Player/player_walking/p03.png')
player_walk3 = pygame.transform.scale(player_walk3, (102, 102))
player_walk4 = pygame.image.load('images/Player/player_walking/p04.png')
player_walk4 = pygame.transform.scale(player_walk4, (102, 102))

def makePlayer(x, y):
    entity = engine.Entity()
    entity.position = engine.Position(x,y, 60, 300)
    entityStandingAnimation = engine.Animation([player_stand0, player_stand1, player_stand2, player_stand3, player_stand4, player_stand5])
    entityWalkingAnimation = engine.Animation([player_walk0, player_walk1, player_walk2, player_walk3, player_walk4])
    entity.animations.add('standing', entityStandingAnimation)
    entity.animations.add('walking', entityWalkingAnimation)
    # entity.score = engine.Score()
    entity.type = 'player'
    return entity

player1_stand0 = pygame.image.load("images/Player1/Standing/img0.png")
player1_stand0 = pygame.transform.scale(player1_stand0, (102, 102))
player1_stand1 = pygame.image.load("images/Player1/Standing/img1.png")
player1_stand1 = pygame.transform.scale(player1_stand1, (102, 102))
player1_stand2 = pygame.image.load("images/Player1/Standing/img2.png")
player1_stand2 = pygame.transform.scale(player1_stand2, (102, 102))
player1_stand3 = pygame.image.load("images/Player1/Standing/img3.png")
player1_stand3 = pygame.transform.scale(player1_stand3, (102, 102))
player1_stand2 = pygame.image.load("images/Player1/Standing/img2.png")
player1_stand2 = pygame.transform.scale(player1_stand2, (102, 102))
player1_stand1 = pygame.image.load("images/Player1/Standing/img1.png")
player1_stand1 = pygame.transform.scale(player1_stand1, (102, 102))
def makePlayer1(x, y):
    entity = engine.Entity()
    entity.position = engine.Position(x,y, 60, 300)
    entityStandingAnimation = engine.Animation([player1_stand0, player1_stand1, player1_stand2, player1_stand3, player1_stand2, player1_stand1])
    # entityWalkingAnimation = engine.Animation([player_walk0, player_walk1, player_walk2, player_walk3, player_walk4])
    entity.animations.add('standing', entityStandingAnimation)
    # entity.animations.add('walking', entityWalkingAnimation)
    # entity.score = engine.Score()
    # entity.alive = True
    entity.damage = 5
    entity.current_fighter = 1
    entity.type = 'player'
    return entity


enemy_stand0 = pygame.image.load('images/Enemy/Idle/0.png')
enemy_stand0 = pygame.transform.scale(enemy_stand0, (200, 110))
enemy_stand1 = pygame.image.load('images/Enemy/Idle/1.png')
enemy_stand1 = pygame.transform.scale(enemy_stand1, (200, 110))
enemy_stand2 = pygame.image.load('images/Enemy/Idle/2.png')
enemy_stand2 = pygame.transform.scale(enemy_stand2, (200, 110))
enemy_stand3 = pygame.image.load('images/Enemy/Idle/3.png')
enemy_stand3 = pygame.transform.scale(enemy_stand3, (200, 110))
enemy_stand4 = pygame.image.load('images/Enemy/Idle/4.png')
enemy_stand4 = pygame.transform.scale(enemy_stand2, (200, 110))
enemy_stand5 = pygame.image.load('images/Enemy/Idle/5.png')
enemy_stand5 = pygame.transform.scale(enemy_stand5, (200, 110))
enemy_stand6 = pygame.image.load('images/Enemy/Idle/6.png')
enemy_stand6 = pygame.transform.scale(enemy_stand0, (200, 110))
enemy_stand7 = pygame.image.load('images/Enemy/Idle/7.png')
enemy_stand7 = pygame.transform.scale(enemy_stand0, (200, 110))

def makeEnemy(x, y, damage, potions):
    entity = engine.Entity()
    entity.position = engine.Position(x,y, 60, 300)
    entity.rect = pygame.rect.Rect(480, 340, 150, 150)
    entityStandingAnimation = engine.Animation([enemy_stand0, enemy_stand1, enemy_stand2, enemy_stand3, enemy_stand4, enemy_stand5, enemy_stand6, enemy_stand7])
    entity.animations.add('standing', entityStandingAnimation)
    entity.damage = damage
    entity.potions = potions
    # entity.alive = True
    entity.current_fighter = 2
    entity.type = 'enemy'
    return entity
def makeBackground(name):
    window = pygame.display.set_mode((720, 480))
    window.blit(name, (0, 0))


def makeDoor(window):
    p1 = pygame.Rect(656, 250, 10, 100)
    pygame.draw.rect(window, BLACK, p1)


def draw_text(window, text, size, x, y):
    font = pygame.font.SysFont('franklingothicmedium', size)
    text = font.render(text, True, WHITE)
    text_rectangle = text.get_rect()
    text_rectangle.center = (x, y)
    window.blit(text, text_rectangle)

def draw_coinText(window,text, x, y):
    font = pygame.font.SysFont('franklingothicmedium', 25)
    text = font.render(text, True, WHITE)
    text_rectangle = text.get_rect()
    text_rectangle.topleft = (x, y)
    # window = pygame.display.set_mode((720, 480))
    window.blit(text, text_rectangle)


def draw_text1(window, text, font, color, x, y):
    img = font.render(text, True, color)
    window.blit(img, (x, y))


#
def intro_text(window, text, size, x, y):
    font = pygame.font.SysFont('franklingothicmedium', size)
    text = font.render(text, True, RED)
    text_rectangle = text.get_rect()
    text_rectangle.center = (x, y)
    window.blit(text, text_rectangle)
    # rect = text.get_rect(topleft=(x, y))
    # while rect.y > -GAME_HEIGHT:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             pygame.quit()
    #             sys.exit()
            # window.fill(background)
            # window.blit(image, rect)
            # pygame.time.wait(25)
            # rect.y -= 1
            # pygame.display.update()

    text1 = "It is year 264 before Christ, Rome"
    text2 = "You are an ordinary craftsman, but your hobby has always"
    text3 = "been sword fighting. And you are pretty good at it."
    text4 = "Late in the evening you and your friends went to the pub"
    text5 = "to have some beer, but you got drunk and you fainted. You"
    text6 = "You woke up in the cell in the morning and you see a "
    text7 = "mysterious guy. "


    dialogue_surface1 = font.render(text1, False, '#FFFFFF')
    dialogue_surface2 = font.render(text2, False, '#FFFFFF')
    dialogue_surface3 = font.render(text3, False, '#FFFFFF')
    dialogue_surface4 = font.render(text4, False, '#FFFFFF')
    dialogue_surface5 = font.render(text5, False, '#FFFFFF')
    dialogue_surface6 = font.render(text6, False, '#FFFFFF')
    dialogue_surface7 = font.render(text7, False, '#FFFFFF')


    window.blit(dialogue_surface1, (200, 10))
    window.blit(dialogue_surface2, (100, 120))
    window.blit(dialogue_surface3, (140, 150))
    window.blit(dialogue_surface4, (100, 230))
    window.blit(dialogue_surface5, (90, 260))
    window.blit(dialogue_surface6, (115, 290))
    window.blit(dialogue_surface7, (270, 320))




def npcName(window, text, color, x, y):
    # p_background = pygame.image.load('images/Prison/prison.png')
    # p_background = pygame.transform.scale(p_background, (GAME_WIDTH, GAME_HEIGHT))
    # window.blit(p_background, (0, 0))
    # coin_count_image = pygame.image.load('images/Coins/coin.png')
    # coin_count_image = pygame.transform.scale(coin_count_image, (25, 30))
    gui_font = pygame.font.SysFont('franklingothicmedium', 24)
    text = text
    # color = color
    name_surface = gui_font.render(text, False, color)
    window.blit(name_surface, (x, y))
    # window.blit(coin_count_image, (50, 50))
    # coin_number = 0
    # draw_coinText(window, str(coin_number), 80, 52)


gui_font = pygame.font.SysFont('franklingothicmedium', 24)
font = pygame.font.SysFont('franklingothicmedium', 15)

second_surface = pygame.Surface([720, 400])
second_surface.fill((BLACK))
door_text = "press 1 to go to hall"
text0 = "press E to talk"
text1 = "Hello, I am Spiculus. They brought you here last night. I don't know "
text2 = "what crime you committed, but you got into the gladiatorial arena."
text3 = "You have to defeat three chosen gladiators and then you will be free. "


dialogue_surface0 = font.render(text0, False, '#FFFFFF')
door_surface = font.render(door_text, False, '#FFFFFF')
dialogue_surface1 = gui_font.render(text1, False, '#FFFFFF')
dialogue_surface2 = gui_font.render(text2, False, '#FFFFFF')
dialogue_surface3 = gui_font.render(text3, False, '#FFFFFF')

turn1_text = "Your Turn"
turn2_text = "Enemy's Turn"
turn_surface1 = gui_font.render(turn1_text, False, '#FFFFFF')
turn_surface2 = gui_font.render(turn2_text, False, '#FFFFFF')

hall_text = "Press B to go back to the Hall"

sword_text = "+ 3 DMG"
sword_surface = font.render(sword_text, False, '#FFFFFF')
armor_text = "+ 7 HP"
armor_surface = font.render(armor_text, False, '#FFFFFF')
potion_text = "HEALS"
potion_surface = font.render(potion_text, False, '#FFFFFF')
pcost_text = "COST: 10"
pcost_surface = font.render(pcost_text, False, '#FFFFFF')
acost_text = "COST: 20"
acost_surface = font.render(acost_text, False, '#FFFFFF')
scost_text = "COST: 20"
scost_surface = font.render(scost_text, False, '#FFFFFF')

cursor_image = pygame.image.load("images/ShopItems/sword.png")

won_text = "You Won!"
won_surface = gui_font.render(won_text, False, '#FFFFFF')
lost_text = "You Lost!"
lost_surface = gui_font.render(lost_text, False, '#FFFFFF')