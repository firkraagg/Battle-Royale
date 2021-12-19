import pygame
import engine
from config import *

pygame.init()


coin1 = pygame.image.load('images/Coins/coin.png')

def makeCoin(x, y):
    entity = engine.Entity()
    entity.position = engine.Position(x,y,1,1)
    entityAnimation = engine.Animation([coin1])
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
    entity.position = engine.Position(x,y, 60, 60)
    entityStandingAnimation = engine.Animation([player_stand0, player_stand1, player_stand2, player_stand3, player_stand4, player_stand5])
    entityWalkingAnimation = engine.Animation([player_walk0, player_walk1, player_walk2, player_walk3, player_walk4])
    entity.animations.add('standing', entityStandingAnimation)
    entity.animations.add('walking', entityWalkingAnimation)
    entity.type = 'player'
    return entity

def draw_text(window, text, size, x, y):
    font = pygame.font.SysFont('franklingothicmedium', size)
    text = font.render(text, True, WHITE)
    text_rectangle = text.get_rect()
    text_rectangle.center = (x, y)
    window.blit(text, text_rectangle)


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






