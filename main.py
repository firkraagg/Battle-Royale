import pygame
import engine
import utilities
import level
import scene
import globals
import inputstream
import soundmanager
from globals import *
import pickle
import button

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

globals.soundManager = soundmanager.SoundManager()

coin_image = pygame.image.load('images/Coins/coin.png')
coin = utilities.makeCoin(90, 342)
coin1 = utilities.makeCoin(615, 342)
coin2 = utilities.makeCoin(200, 342)

npc1 = utilities.makeNpc(350, 226)
shopkeeper = utilities.makeShopKeeper(250,242)

sword = utilities.makeSword(255, 280)
sword1 = utilities.makeSword1(255, 277)
shield = utilities.makeShield(255, 265)
armor = utilities.makeArmor(310, 274)
potion = utilities.makePotion(445, 293)
poisonPotion = utilities.makePoisonPotion(584, 293)

background = utilities.makeBackground(p_background)

player = utilities.makePlayer(450, 212)
player.camera = engine.Camera(0, 0, 920, 525)
player.score = engine.Score()
player.potions = engine.Potions()
player.poisonPotions = engine.PoisonPotions()
player.damage = engine.Damage()
player.health = engine.Health()
player.maxHealth = engine.MaxHealth()
player.swordLvl = engine.SwordLvl()
player.shieldLvl = engine.ShieldLvl()
player.input = engine.Input(pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_e, pygame.K_SPACE)
player.intention = engine.Intention()
score = 0

player1 = utilities.makePlayer1(500, 265)
player1.camera = engine.Camera(0, 0, 920, 525)
player1.score = player.score
player1.potions = player.potions
player1.poisonPotions = player.poisonPotions
player1.damage = player.damage
player1.health = player.health
player1.maxHealth = player.maxHealth
player1.swordLvl = player.swordLvl
player1.shieldLvl = player.shieldLvl
player1.input = engine.Input(pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_e, pygame.K_SPACE)
player1.intention = engine.Intention()

enemy = utilities.makeEnemy(190, 245, 5, 1)
enemy.camera = engine.Camera(0, 0, 920, 525)
enemy.score = player.score
enemy.potions = player.potions
enemy.poisonPotions = player.poisonPotions
enemy.damage = player.damage
enemy.enemyHealth = engine.EnemyHealth()

enemy1 = utilities.makeEnemy1(190, 250, 10, 1)
enemy1.camera = engine.Camera(0, 0, 920, 525)
enemy1.score = player.score
enemy1.potions = player.potions
enemy1.poisonPotions = player.poisonPotions
enemy1.damage = player.damage
enemy1.enemyHealth = engine.Enemy1Health()

enemy2 = utilities.makeEnemy2(190, 181, 10, 1)
enemy2.camera = engine.Camera(0, 0, 920, 525)
enemy2.score = player.score
enemy2.potions = player.potions
enemy2.poisonPotions = player.poisonPotions
enemy2.damage = player.damage
enemy2.enemyHealth = engine.Enemy2Health()

enemy3 = utilities.makeEnemy3(190, 181, 10, 1)
enemy3.camera = engine.Camera(0, 0, 920, 525)
enemy3.score = player.score
enemy3.potions = player.potions
enemy3.poisonPotions = player.poisonPotions
enemy3.damage = player.damage
enemy3.enemyHealth = engine.Enemy3Health()

enemy4 = utilities.makeEnemy4(190, 181, 10, 1)
enemy4.camera = engine.Camera(0, 0, 920, 525)
enemy4.score = player.score
enemy4.potions = player.potions
enemy4.poisonPotions = player.poisonPotions
enemy4.damage = player.damage
enemy4.enemyHealth = engine.Enemy4Health()

arrow = utilities.makeArrow(290, 312)
arrow.camera = engine.Camera(0, 0, 920, 525)
arrow.score = player.score
arrow.potions = player.potions
arrow.poisonPotions = player.poisonPotions
arrow.damage = player.damage
arrow.health = player.health

poisonArrow = utilities.makePoisonArrow(290, 300)
poisonArrow.camera = engine.Camera(0, 0, 920, 525)
poisonArrow.score = player.score
poisonArrow.potions = player.potions
poisonArrow.poisonPotions = player.poisonPotions
poisonArrow.damage = player.damage
poisonArrow.health = player.health

ball = utilities.makeBall(290, 290)
ball.camera = engine.Camera(0, 0, 920, 525)
ball.score = player.score
ball.potions = player.potions
ball.poisonPotions = player.poisonPotions
ball.damage = player.damage
ball.health = player.health

door1 = pygame.Rect(46, 405, 5, 50)

def update():
    clock.tick(60)

globals.levels[1] = level.Level(
    platforms=[
        pygame.Rect(52, 286, 610, 5),

        pygame.Rect(50, 405, 5, 50),

        pygame.Rect(680, 405, 5, 50)

    ],
    entities=[
        npc1, player, coin

    ],
)

globals.levels[2] = level.Level(
    platforms=[
        pygame.Rect(52, 283, 610, 5),

        pygame.Rect(50, 405, 5, 50),

        pygame.Rect(680, 405, 5, 50)
    ],
    entities=[
        coin1, player,
    ]
)

globals.levels[3] = level.Level(
    platforms=[
        pygame.Rect(52, 286, 610, 5),

        pygame.Rect(50, 405, 5, 50),

        pygame.Rect(680, 405, 5, 50)
    ],
    entities=[
        coin2, shopkeeper, sword, potion, armor, player
    ]
)

globals.levels[4] = level.Level(
    platforms=[
        pygame.Rect(52, 337, 610, 5),

        pygame.Rect(1, 405, 5, 50),

        pygame.Rect(686, 405, 5, 50)
    ],
    entities=[
        enemy, player1
    ]
)

globals.levels[5] = level.Level(
    platforms=[
        pygame.Rect(52, 283, 610, 5),

        pygame.Rect(50, 405, 5, 50),

        pygame.Rect(680, 405, 5, 50)
    ],
    entities=[
        player
    ]
)

globals.levels[6] = level.Level(
    platforms=[
        pygame.Rect(52, 286, 610, 5),

        pygame.Rect(50, 405, 5, 50),

        pygame.Rect(680, 405, 5, 50)
    ],
    entities=[
        coin2, shopkeeper, sword1, potion, armor, player
    ]
)

globals.levels[7] = level.Level(
    platforms=[
        pygame.Rect(52, 340, 610, 5),

        pygame.Rect(25, 405, 5, 50),

        pygame.Rect(656, 405, 5, 50)
    ],
    entities=[
        enemy1, player1
    ]
)

globals.levels[8] = level.Level(
    platforms=[
        pygame.Rect(52, 283, 610, 5),

        pygame.Rect(50, 405, 5, 50),

        pygame.Rect(680, 405, 5, 50)
    ],
    entities=[
        player
    ]
)

globals.levels[9] = level.Level(
    platforms=[
        pygame.Rect(52, 286, 610, 5),

        pygame.Rect(50, 405, 5, 50),

        pygame.Rect(680, 405, 5, 50)
    ],
    entities=[
        coin2, shopkeeper, shield, potion, armor, player
    ]
)

globals.levels[10] = level.Level(
    platforms=[
        pygame.Rect(52, 340, 610, 5),

        pygame.Rect(25, 405, 5, 50),

        pygame.Rect(656, 405, 5, 50)
    ],
    entities=[
        enemy2, player1, arrow
    ]
)

globals.levels[11] = level.Level(
    platforms=[
        pygame.Rect(52, 283, 610, 5),

        pygame.Rect(50, 405, 5, 50),

        pygame.Rect(680, 405, 5, 50)
    ],
    entities=[
        player
    ]
)

globals.levels[12] = level.Level(
    platforms=[
        pygame.Rect(52, 286, 610, 5),

        pygame.Rect(50, 405, 5, 50),

        pygame.Rect(680, 405, 5, 50)
    ],
    entities=[
        coin2, shopkeeper, shield, potion, armor, poisonPotion, player
    ]
)


globals.levels[13] = level.Level(
    platforms=[
        pygame.Rect(52, 340, 610, 5),

        pygame.Rect(25, 405, 5, 50),

        pygame.Rect(656, 405, 5, 50)
    ],
    entities=[
        enemy3, player1, poisonArrow
    ]
)

globals.levels[14] = level.Level(
    platforms=[
        pygame.Rect(52, 283, 610, 5),

        pygame.Rect(50, 405, 5, 50),

        pygame.Rect(680, 405, 5, 50)
    ],
    entities=[
        player
    ]
)

globals.levels[15] = level.Level(
    platforms=[
        pygame.Rect(52, 286, 610, 5),

        pygame.Rect(50, 405, 5, 50),

        pygame.Rect(680, 405, 5, 50)
    ],
    entities=[
        coin2, shopkeeper, sword, potion, armor, poisonPotion, player
    ]
)

globals.levels[16] = level.Level(
    platforms=[
        pygame.Rect(52, 340, 610, 5),

        pygame.Rect(25, 405, 5, 50),

        pygame.Rect(656, 405, 5, 50)
    ],
    entities=[
        enemy4, player1, ball
    ]
)
globals.world = globals.levels[1]

sceneManager = scene.SceneManager()
mainMenu = scene.MainMenuScene()
sceneManager.push(mainMenu)

inputStream = inputstream.InputStream()
cameraSys = engine.CameraSystem()
cameraSys1 = engine.CameraSystem1()

entity = engine.Entity()

running = True

def save():
    with open("save_game.pkl", "wb") as save_game:
        pickle.dump(player.position, save_game)
        pickle.dump(player.score, save_game)
        pickle.dump(player.potions, save_game)
        pickle.dump(player.poisonPotions, save_game)
        pickle.dump(player.damage, save_game)
        pickle.dump(player.health, save_game)
        pickle.dump(player.maxHealth, save_game)
        pickle.dump(player.swordLvl, save_game)
        pickle.dump(player.shieldLvl, save_game)

        pickle.dump(player1.position, save_game)
        pickle.dump(player1.score, save_game)
        pickle.dump(player1.potions, save_game)
        pickle.dump(player1.poisonPotions, save_game)
        pickle.dump(player1.damage, save_game)
        pickle.dump(player1.health, save_game)
        pickle.dump(player1.maxHealth, save_game)
        pickle.dump(player1.swordLvl, save_game)
        pickle.dump(player1.shieldLvl, save_game)

        pickle.dump(enemy.position, save_game)
        pickle.dump(enemy.score, save_game)
        pickle.dump(enemy.potions, save_game)
        pickle.dump(enemy.poisonPotions, save_game)
        pickle.dump(enemy.damage, save_game)
        pickle.dump(enemy.health, save_game)
        pickle.dump(enemy.maxHealth, save_game)
        pickle.dump(enemy.swordLvl, save_game)
        pickle.dump(enemy.shieldLvl, save_game)

        pickle.dump(enemy1.position, save_game)
        pickle.dump(enemy1.score, save_game)
        pickle.dump(enemy1.potions, save_game)
        pickle.dump(enemy1.poisonPotions, save_game)
        pickle.dump(enemy1.damage, save_game)
        pickle.dump(enemy1.health, save_game)
        pickle.dump(enemy1.maxHealth, save_game)
        pickle.dump(enemy1.swordLvl, save_game)
        pickle.dump(enemy1.shieldLvl, save_game)

        pickle.dump(enemy2.position, save_game)
        pickle.dump(enemy2.score, save_game)
        pickle.dump(enemy2.potions, save_game)
        pickle.dump(enemy2.poisonPotions, save_game)
        pickle.dump(enemy2.damage, save_game)
        pickle.dump(enemy2.health, save_game)
        pickle.dump(enemy2.maxHealth, save_game)
        pickle.dump(enemy2.swordLvl, save_game)
        pickle.dump(enemy2.shieldLvl, save_game)

        pickle.dump(enemy3.position, save_game)
        pickle.dump(enemy3.score, save_game)
        pickle.dump(enemy3.potions, save_game)
        pickle.dump(enemy3.poisonPotions, save_game)
        pickle.dump(enemy3.damage, save_game)
        pickle.dump(enemy3.health, save_game)
        pickle.dump(enemy3.maxHealth, save_game)
        pickle.dump(enemy3.swordLvl, save_game)
        pickle.dump(enemy3.shieldLvl, save_game)

        pickle.dump(enemy4.position, save_game)
        pickle.dump(enemy4.score, save_game)
        pickle.dump(enemy4.potions, save_game)
        pickle.dump(enemy4.poisonPotions, save_game)
        pickle.dump(enemy4.damage, save_game)
        pickle.dump(enemy4.health, save_game)
        pickle.dump(enemy4.maxHealth, save_game)
        pickle.dump(enemy4.swordLvl, save_game)
        pickle.dump(enemy4.shieldLvl, save_game)

def load():
    with open("save_game.pkl", "rb") as load_game:
        player.position = pickle.load(load_game)
        player.score = pickle.load(load_game)
        player.potions = pickle.load(load_game)
        player.poisonPotions = pickle.load(load_game)
        player.damage = pickle.load(load_game)
        player.health = pickle.load(load_game)
        player.maxHealth = pickle.load(load_game)
        player.swordLvl = pickle.load(load_game)
        player.shieldLvl = pickle.load(load_game)
        print(player)
        player1.position = pickle.load(load_game)
        player.score = pickle.load(load_game)
        player1.score = player.score
        player.potions = pickle.load(load_game)
        player.potions = player1.potions
        player1.poisonPotions = pickle.load(load_game)
        player.poisonPotions = player1.poisonPotions
        player1.damage = pickle.load(load_game)
        player1.health = pickle.load(load_game)
        player1.maxHealth = pickle.load(load_game)
        player1.swordLvl = pickle.load(load_game)
        player1.swordLvl = player.swordLvl
        player1.shieldLvl = pickle.load(load_game)
        player1.shieldLvl = player.shieldLvl
        print(player1)
        enemy.enemyHealth = engine.EnemyHealth()
        enemy1.enemyHealth = engine.Enemy1Health()
        enemy2.enemyHealth = engine.Enemy2Health()
        enemy3.enemyHealth = engine.Enemy3Health()
        enemy4.enemyHealth = engine.Enemy4Health()

while running:

    inputStream.processInput()

    sceneManager.input(inputStream)
    sceneManager.update(inputStream)
    sceneManager.draw(window)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    new_player_x = player.position.rect.x
    new_enemy_x = enemy.position.rect.x


    if game_state == 'playing':

        for entity in globals.world.entities:
            entity.animations.animationList[entity.state].update()

        window.blit(p_background, (0, 0))
        window.blit(utilities.door_surface, (60, 225))

        new_player_rect = pygame.Rect(int(new_player_x), 400, 72, 72)
        x_collision = False

        for platform in globals.world.platforms:
            if platform.colliderect(new_player_rect):
                x_collision = True
                break

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
                                     globals.soundManager.playSound("buying")
                                     player.score.score -= 20
                                     player.damage.damage += 3
                                     globals.world.entities.remove(entity)
                             if entity == sword1:
                                 if player.score.score >= 20:
                                     globals.soundManager.playSound("buying")
                                     player.score.score -= 20
                                     player.damage.damage += 3
                                     player.swordLvl.swordLvl += 1
                                     globals.world.entities.remove(entity)
                             if entity == potion:
                                 if player.score.score >= 10:
                                     globals.soundManager.playSound("buying")
                                     player.score.score -= 10
                                     player.potions.potions += 1
                                     globals.world.entities.remove(entity)
                             if entity == poisonPotion:
                                 if player.score.score >= 10:
                                     globals.soundManager.playSound("buying")
                                     player.score.score -= 10
                                     player.poisonPotions.poisonPotions += 1
                                     globals.world.entities.remove(entity)
                             if entity == armor:
                                 if player.score.score >= 20:
                                     globals.soundManager.playSound("buying")
                                     player.score.score -= 20
                                     player1.maxHealth.maxHealth += 7
                                     player.health.health += 7
                                     globals.world.entities.remove(entity)
                             if entity == shield:
                                 if player.score.score >= 20:
                                     globals.soundManager.playSound("buying")
                                     player.score.score -= 20
                                     player.shieldLvl.shieldLvl += 1
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
        if globals.levels == [2]:
            level.save_button.draw()
        if globals.levels == [4]:
            level.load_button.draw()
        if level.load_button.clicked:
            load()
            print("loaded")
            if entity.health.health == 0:
                level.yes = True
        if level.save_button.clicked:
            save()
            print("saved")

    update()

pygame.quit()