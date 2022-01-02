import pygame
import engine
import utilities
import level
import scene
import globals
import button
import inputstream
from config import *

pygame.init()
window = pygame.display.set_mode((720, 480))
pygame.display.set_caption('Battle Royale')
clock = pygame.time.Clock()
font1 = pygame.font.SysFont('franklingothicmedium', 25)
gui_font = pygame.font.SysFont('franklingothicmedium', 24)
font = pygame.font.SysFont('franklingothicmedium', 15)

game_state = 'playing'

entities = []

p_background = pygame.image.load('images/Backgrounds/prison_bg.png')
p_background = pygame.transform.scale(p_background, (GAME_WIDTH, GAME_HEIGHT))

coin_image = pygame.image.load('images/Coins/coin.png')
coin = utilities.makeCoin(90, 342)
coin1 = utilities.makeCoin(615, 342)
coin2 = utilities.makeCoin(200, 342)
entities.append(coin)

npc1 = utilities.makeNpc(350, 226)
shopkeeper = utilities.makeShopKeeper(250,242)

sword = utilities.makeSword(255, 280)
armor = utilities.makeArmor(310, 274)
potion = utilities.makePotion(445, 293)


background = utilities.makeBackground(p_background)
player = utilities.makePlayer(450, 261)
player.camera = engine.Camera(0, 0, 920, 525)
player.score = engine.Score()
player.potions = engine.Potions()
player.damage = engine.Damage()
player.health = engine.Health()
player.maxHealth = engine.MaxHealth()
player.input = engine.Input(pygame.K_a, pygame.K_d)
player.intention = engine.Intention()
score = 0

player1 = utilities.makePlayer1(100, 363)
player1.camera = engine.Camera(0, 0, 920, 525)
player1.score = player.score
player1.potions = player.potions
player1.damage = player.damage
player1.health = player.health
player1.maxHealth = engine.MaxHealth()

enemy = utilities.makeEnemy(460, 360, 5, 1)
enemy.camera = engine.Camera(0, 0, 920, 525)
enemy.score = player.score
enemy.potions = player.potions
enemy.damage = player.damage
enemy.enemyHealth = engine.EnemyHealth()

door1 = pygame.Rect(46, 405, 5, 50)

globals.levels[1] = level.Level(
    platforms=[
        pygame.Rect(52, 350, 610, 5),

        pygame.Rect(25, 405, 5, 50),

        pygame.Rect(656, 405, 5, 50)

    ],
    entities=[
        npc1, player, coin
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
        coin2, shopkeeper, sword, potion, armor, player
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
        player1, enemy
    ],
    doors=[
        pygame.Rect(330, 405, 5, 50),
    ]
)


globals.world = globals.levels[1]

sceneManager = scene.SceneManager()
mainMenu = scene.MainMenuScene()
sceneManager.push(mainMenu)

inputStream = inputstream.InputStream()
cameraSys = engine.CameraSystem()
cameraSys1 = engine.CameraSystem1()
running = True
while running:
    inputStream.processInput()

    sceneManager.input(inputStream)
    sceneManager.update(inputStream)
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

        for platform in globals.world.platforms:
            if platform.colliderect(new_player_rect):
                x_collision = True
                break

        for door in globals.world.doors:
            if door.colliderect(new_player_rect):
                window.blit(utilities.door_surface, (70, 225))

        if x_collision == False:
            player.position.rect.x = new_player_x
        sword_text = "Sword"
        sword_surface = font.render(sword_text, False, '#FFFFFF')
        player_rect = pygame.Rect(int(player.position.rect.x), 300, player.position.rect.width, player.position.rect.height)
        for entity in globals.world.entities:
             if entity.type == 'buyable':
                 if entity.position.rect.colliderect(player_rect):
                     if event.type == pygame.KEYUP:
                         if event.key == pygame.K_e:
                             if entity == sword:
                                 if player.score.score >= 20:
                                     player.score.score -= 20
                                     player.damage.damage += 3
                                     globals.world.entities.remove(entity)
                             if entity == potion:
                                 if player.score.score >= 10:
                                     player.score.score -= 10
                                     player.potions.potions += 1
                                     globals.world.entities.remove(entity)
                             if entity == armor:
                                 if player.score.score >= 20:
                                     player.score.score -= 20
                                     player1.maxHealth.maxHealth += 7
                                     player.maxHealth.maxHealth += 7
                                     player1.health.health += 7
                                     globals.world.entities.remove(entity)
        for entity in globals.world.entities:
            if entity.type == 'friendly':
                if entity.position.rect.colliderect(player_rect):
                    window.blit(utilities.dialogue_surface0, (370, 240))
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_e:
                            window.blit(utilities.second_surface, (0, 370)),
                            window.blit(utilities.dialogue_surface1, (0, 380)),
                            window.blit(utilities.dialogue_surface2, (0, 410)),
                            window.blit(utilities.dialogue_surface3, (0, 440))

        clock.tick(60)

pygame.quit()