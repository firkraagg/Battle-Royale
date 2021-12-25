import pygame
import engine
import utilities
import level
import scene
import globals
import config
from config import *

pygame.init()
window = pygame.display.set_mode((720, 480))
pygame.display.set_caption('Battle Royale')
clock = pygame.time.Clock()
font1 = pygame.font.SysFont('franklingothicmedium', 25)

game_state = 'playing'

entities = []

second_surface = pygame.Surface([720, 400])
second_surface.fill((BLACK))
door_text = "press 1 to go to hall"
text0 = "press E to talk"
text1 = "Hello, I am Spiculus. They brought you here last night. I don't know "
text2 = "what crime you committed, but you got into the gladiatorial arena."
text3 = "You have to defeat three chosen gladiators and then you will be free. "



gui_font = pygame.font.SysFont('franklingothicmedium', 24)
font = pygame.font.SysFont('franklingothicmedium', 15)
dialogue_surface0 = font.render(text0, False, '#FFFFFF')
door_surface = font.render(door_text, False, '#FFFFFF')
dialogue_surface1 = gui_font.render(text1, False, '#FFFFFF')
dialogue_surface2 = gui_font.render(text2, False, '#FFFFFF')
dialogue_surface3 = gui_font.render(text3, False, '#FFFFFF')

p_background = pygame.image.load('images/Prison/prison.png')
p_background = pygame.transform.scale(p_background, (GAME_WIDTH, GAME_HEIGHT))

hall_bg = pygame.image.load("images/Hall/hall_bg.png")
hall_bg = pygame.transform.scale(hall_bg, (GAME_WIDTH, GAME_HEIGHT))

shop_text = "Press 3 to go to the shop"
shop_surface = font.render(shop_text, False, '#FFFFFF')

coin_image = pygame.image.load('images/Coins/coin.png')
coin = utilities.makeCoin(90, 342)
coin1 = utilities.makeCoin(500, 342)
entities.append(coin)

npc = utilities.makeNpc(150, 226)

player = utilities.makePlayer(530, 261)
background = utilities.makeBackground(p_background)
player.camera = engine.Camera(0, 0, 920, 525)
player.score = engine.Score()


door1 = pygame.Rect(646, 405, 5, 50)


globals.levels[1] = level.Level(

    platforms=[
        pygame.Rect(52, 350, 610, 5),

        pygame.Rect(25, 405, 5, 50),

        pygame.Rect(656, 405, 5, 50)

    ],
    entities=[
        npc, player, coin

    ],
    doors=[
        door1
    ]

)
globals.levels[2] = level.Level(

    platforms=[
        pygame.Rect(52, 350, 610, 5),

        pygame.Rect(25, 405, 5, 50),

        pygame.Rect(656, 405, 5, 50),

    ],
    entities=[
        coin1, player
    ],
    doors=[
        door1
    ]

)

globals.levels[3] = level.Level(

    platforms=[
        pygame.Rect(52, 350, 610, 5),

        pygame.Rect(25, 405, 5, 50),

        pygame.Rect(656, 405, 5, 50)
    ],
    entities=[
        coin1, player
    ],
    doors=[
        pygame.Rect(330, 405, 5, 50),
    ]

)

globals.levels[4] = level.Level(

    platforms=[
        pygame.Rect(52, 350, 610, 5),

        pygame.Rect(25, 405, 5, 50),

        pygame.Rect(656, 405, 5, 50)
    ],
    entities=[
        player
    ],
    doors=[
        pygame.Rect(330, 405, 5, 50),
    ]

)


globals.world = globals.levels[1]


sceneManager = scene.SceneManager()
mainMenu = scene.MainMenuScene()
sceneManager.push(mainMenu)

cameraSys = engine.CameraSystem()
running = True
while running:

    sceneManager.input()
    sceneManager.update()
    sceneManager.draw(window)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    new_player_x = player.position.rect.x

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        new_player_x -= 2
        player.direction = 'left'
        player.state = 'walking'
    if keys[pygame.K_d]:
        new_player_x += 2
        player.direction = 'right'
        player.state = 'walking'
    if not keys[pygame.K_a] and not keys[pygame.K_d]:
        player.state = 'standing'


    if game_state == 'playing':


        for entity in globals.world.entities:
            entity.animations.animationList[entity.state].update()

        window.blit(p_background, (0, 0))

        new_player_rect = pygame.Rect(int(new_player_x), 400, 72, 72)
        x_collision = False
        # if config.levels[1]:
        #     utilities.makeBackground(p_background)
        # if config.levels[2]:
        #     utilities.makeBackground(hall_bg)

        for platform in globals.world.platforms:
            if platform.colliderect(new_player_rect):
                x_collision = True
                break

        for door in globals.world.doors:
            if door.colliderect(new_player_rect):
                window.blit(door_surface, (530, 225))




        if x_collision == False:
            player.position.rect.x = new_player_x

        score = 0
        player_rect = pygame.Rect(int(player.position.rect.x), 300, player.position.rect.width, player.position.rect.height)
        for entity in globals.world.entities:
            if entity.type == 'collectable':
                if entity.position.rect.colliderect(player_rect):
                    globals.world.entities.remove(entity)
                    utilities.draw_coinText(window, str(score), 80, 52)
                    player.score.score += 15

        for entity in globals.world.entities:
            if entity.type == 'friendly':
                if entity.position.rect.colliderect(player_rect):
                    window.blit(dialogue_surface0, (175, 240))
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_e:
                            window.blit(second_surface, (0, 370)),
                            window.blit(dialogue_surface1, (0, 380)),
                            window.blit(dialogue_surface2, (0, 410)),
                            window.blit(dialogue_surface3, (0, 440))

        # draw_text(str(coin_number), 80, 52)
        # cameraSys.update(window, world)
        # pygame.display.flip()
        clock.tick(60)

pygame.quit()