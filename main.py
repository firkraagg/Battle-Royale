import pygame
import engine
import utilities
import level
import scene
from config import *

# def draw_text(text, x, y):
#     text = font1.render(text, True, WHITE)
#     text_rectangle = text.get_rect()
#     text_rectangle.topleft = (x, y)
#     window.blit(text, text_rectangle)
#
#
pygame.init()
window = pygame.display.set_mode((720, 480))
pygame.display.set_caption('Battle Royale')
clock = pygame.time.Clock()
font1 = pygame.font.SysFont('franklingothicmedium', 25)

game_state = 'playing'

# entities = []
#
# second_surface = pygame.Surface([720, 400])
# second_surface.fill((BLACK))
# text00 = "Spiculus"
# text0 = "press E to talk"
# text1 = "Hello, I am Spiculus. They brought you here last night. I don't know "
# text2 = "what crime you committed, but you got into the gladiatorial arena."
# text3 = "You have to defeat three chosen gladiators and then you will be free. "
#
# gui_font = pygame.font.SysFont('franklingothicmedium', 24)
# font = pygame.font.SysFont('franklingothicmedium', 15)
#
# name_surface0 = gui_font.render(text00, False, '#FFFFFF')
# dialogue_surface0 = font.render(text0, False, '#FFFFFF')
# dialogue_surface1 = gui_font.render(text1, False, '#FFFFFF')
# dialogue_surface2 = gui_font.render(text2, False, '#FFFFFF')
# dialogue_surface3 = gui_font.render(text3, False, '#FFFFFF')
#

#
# platforms = [
#
#     pygame.Rect(52, 350, 610, 5),
#
#     pygame.Rect(25, 405, 5, 50),
#
#     pygame.Rect(656, 405, 5, 50)
# ]
#
# p_background = pygame.image.load('images/Prison/prison.png')
# p_background = pygame.transform.scale(p_background, (GAME_WIDTH, GAME_HEIGHT))
#
# coin_image = pygame.image.load('images/Coins/coin.png')
#
# entities.append(utilities.makeCoin(90, 342))
# entities.append(utilities.makeNpc(150, 226))
# player = utilities.makePlayer(530, 261)
# entities.append(player)
#
# coin_number = 0
# coin_count_image = pygame.image.load('images/Coins/coin.png')
# coin_count_image = pygame.transform.scale(coin_count_image, (25, 30))
#

sceneManager = scene.SceneManager()
mainMenu = scene.MainMenuScene()
sceneManager.push(mainMenu)

# level1 = level.Level1(
#     platforms = [
#         pygame.Rect(52, 350, 610, 5),
#
#         pygame.Rect(25, 405, 5, 50),
#
#         pygame.Rect(656, 405, 5, 50)
#     ],
#
# )
#
#
# world = level1
#
running = True
while running:

    sceneManager.input()
    sceneManager.update()
    sceneManager.draw(window)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#
#     new_player_x = player.position.rect.x
#
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_a]:
#         new_player_x -= 2
#         player.direction = 'left'
#         player.state = 'walking'
#     if keys[pygame.K_d]:
#         new_player_x += 2
#         player.direction = 'right'
#         player.state = 'walking'
#     if not keys[pygame.K_a] and not keys[pygame.K_d]:
#         player.state = 'standing'
#
#
#
#     if game_state == 'playing':
#
#
#         for entity in entities:
#             entity.animations.animationList[entity.state].update()
#
#
#
#         new_player_rect = pygame.Rect(new_player_x, 400, 72, 72)
#         x_collision = False
#
#         window.blit(p_background, (0, 0))
#         for platform in platforms:
#             if platform.colliderect(new_player_rect):
#                 x_collision = True
#                 break
#
#         if x_collision == False:
#             player.position.rect.x = new_player_x
#
#         player_rect = pygame.Rect(player.position.rect.x, 300, player.position.rect.width, player.position.rect.height)
#         for entity in entities:
#             if entity.type == 'collectable':
#                 if entity.position.rect.colliderect(player_rect):
#                     entities.remove(entity)
#                     coin_number += 15
#
#         for entity in entities:
#             if entity.type == 'friendly':
#                 if entity.position.rect.colliderect(player_rect):
#                     window.blit(dialogue_surface0, (175, 240))
#                     if event.type == pygame.KEYUP:
#                         if event.key == pygame.K_e:
#                             window.blit(second_surface, (0, 370)),
#                             window.blit(dialogue_surface1, (0, 380)),
#                             window.blit(dialogue_surface2, (0, 410)),
#                             window.blit(dialogue_surface3, (0, 440))
#
#         for entity in entities:
#             s = entity.state
#             a = entity.animations.animationList[s]
#             if entity.direction == 'right':
#                 a.draw(window, entity.position.rect.x, entity.position.rect.y, True, False)
#             else:
#                 a.draw(window, entity.position.rect.x, entity.position.rect.y, False, False)
#
#         window.blit(name_surface0, (180, 215))
#
#         window.blit(coin_count_image, (50, 50))
#         draw_text(str(coin_number), 80, 52)
#
        # pygame.display.flip()
        # clock.tick(60)

pygame.quit()