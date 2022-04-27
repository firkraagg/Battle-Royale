import pygame
import engine
import globals
from globals import *

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

sword1_image = pygame.image.load("images/ShopItems/sword1.png")
sword1_image = pygame.transform.scale(sword1_image, (60, 60))
def makeSword1(x, y):
    entity = engine.Entity()
    entity.position = engine.Position(x, y, 40, 40)
    entityAnimation = engine.Animation([sword_image])
    entity.animations.add('standing', entityAnimation)
    entity.type = 'buyable'
    entity.type1 = 'sword1'
    return entity

arrow_image = pygame.image.load("images/Enemy2/enemy_attack/arrow.png")
arrow_image = pygame.transform.scale(arrow_image, (34, 10))
def makeArrow(x, y):
    entity = engine.Entity()
    entity.x = x
    entity.y = y
    entity.position = engine.Position(x, y, 10, 40)
    entityAnimation = engine.Animation([arrow_image])
    entity.animations.add('standing', entityAnimation)
    entity.shoot = None
    entity.type = 'shootable'
    entity.type1 = 'arrow'
    return entity

def setPoison(entity):
    if entity.health.health >= 1:
        entity.health.health -= 0.1

poisonArrow_image = pygame.image.load("images/Enemy3/enemy_attack/arrow.png")
poisonArrow_image = pygame.transform.scale(poisonArrow_image, (34, 10))
def makePoisonArrow(x, y):
    entity = engine.Entity()
    entity.x = x
    entity.y = y
    entity.position = engine.Position(x, y, 10, 40)
    entityAnimation = engine.Animation([poisonArrow_image])
    entity.animations.add('standing', entityAnimation)
    entity.shoot = None
    entity.effect = engine.Effect(setPoison, 1000, "poison", None)
    entity.type = 'shootable'
    entity.type1 = 'poisonArrow'
    return entity

ball_image = pygame.image.load("images/Enemy4/enemy_shoot/ball.png")
ball_image = pygame.transform.scale(ball_image, (12, 12))
def makeBall(x, y):
    entity = engine.Entity()
    entity.x = x
    entity.y = y
    entity.position = engine.Position(x, y, 10, 40)
    entityAnimation = engine.Animation([ball_image])
    entity.animations.add('standing', entityAnimation)
    entity.shoot = None
    entity.effect = engine.Effect(setPoison, 1000, "poison", None)
    entity.type = 'shootable'
    entity.type1 = 'ball'
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

poisonPotion_image = pygame.image.load("images/ShopItems/poisonPotion.png")
poisonPotion_image = pygame.transform.scale(poisonPotion_image, (30, 30))
def makePoisonPotion(x, y):
    entity = engine.Entity()
    entity.rect = pygame.rect.Rect(10, 10, 60, 40)
    entity.position = engine.Position(x, y, 60, 40)
    entityAnimation = engine.Animation([poisonPotion_image])
    entity.animations.add('standing', entityAnimation)
    entity.type = 'buyable'
    entity.type1 = 'poisonPotion'
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

shield_image = pygame.image.load("images/ShopItems/shield.png")
shield_image = pygame.transform.scale(shield_image, (60, 60))
def makeShield(x, y):
    entity = engine.Entity()
    entity.position = engine.Position(x, y, 40, 40)
    entityAnimation = engine.Animation([shield_image])
    entity.animations.add('standing', entityAnimation)
    entity.type = 'buyable'
    entity.type1 = 'shield'
    return entity

player_stand0 = pygame.image.load('images/Player/player_standing/0.png')
player_stand0 = pygame.transform.scale(player_stand0, (60, 150))
player_stand1 = pygame.image.load('images/Player/player_standing/1.png')
player_stand1 = pygame.transform.scale(player_stand1, (60, 150))
player_stand2 = pygame.image.load('images/Player/player_standing/2.png')
player_stand2 = pygame.transform.scale(player_stand2, (60, 150))
player_stand3 = pygame.image.load('images/Player/player_standing/3.png')
player_stand3 = pygame.transform.scale(player_stand3, (60, 150))
player_stand4 = pygame.image.load('images/Player/player_standing/2.png')
player_stand4 = pygame.transform.scale(player_stand2, (60, 150))
player_stand5 = pygame.image.load('images/Player/player_standing/5.png')
player_stand5 = pygame.transform.scale(player_stand5, (60, 150))

player_walk0 = pygame.image.load('images/Player/player_walking/0.png')
player_walk0 = pygame.transform.scale(player_walk0, (60, 150))
player_walk1 = pygame.image.load('images/Player/player_walking/1.png')
player_walk1 = pygame.transform.scale(player_walk1, (60, 150))
player_walk2 = pygame.image.load('images/Player/player_walking/2.png')
player_walk2 = pygame.transform.scale(player_walk2, (60, 150))
player_walk3 = pygame.image.load('images/Player/player_walking/3.png')
player_walk3 = pygame.transform.scale(player_walk3, (60, 150))
player_walk4 = pygame.image.load('images/Player/player_walking/4.png')
player_walk4 = pygame.transform.scale(player_walk4, (60, 150))

player_jump0 = pygame.image.load('images/Player/player_jumping/0.png')
player_jump0 = pygame.transform.scale(player_jump0, (60, 150))
player_jump1 = pygame.image.load('images/Player/player_jumping/1.png')
player_jump1 = pygame.transform.scale(player_jump1, (68, 150))
player_jump2 = pygame.image.load('images/Player/player_jumping/2.png')
player_jump2 = pygame.transform.scale(player_jump2, (75, 150))

def makePlayer(x, y):
    entity = engine.Entity()
    entity.position = engine.Position(x,y, 60, 300)
    entityStandingAnimation = engine.Animation([player_stand0, player_stand1, player_stand2,
                                                player_stand3, player_stand4, player_stand5])
    entityWalkingAnimation = engine.Animation([player_walk0, player_walk1, player_walk2,
                                               player_walk3, player_walk4])
    entityJumpingAnimation = engine.deathAnimation([player_jump0, player_jump1,
                                                    player_jump2, player_jump2, player_jump2])
    entity.animations.add('standing', entityStandingAnimation)
    entity.animations.add('walking', entityWalkingAnimation)
    entity.animations.add('jumping', entityJumpingAnimation)
    entity.intention = engine.Intention()
    entity.acceleration = 0.05
    entity.type = 'player'
    entity.name = "Player1"
    return entity

player1_stand0 = pygame.image.load("images/Player1/player_standing/img0.png")
player1_stand0 = pygame.transform.scale(player1_stand0, (102, 102))
player1_stand1 = pygame.image.load("images/Player1/player_standing/img1.png")
player1_stand1 = pygame.transform.scale(player1_stand1, (102, 102))
player1_stand2 = pygame.image.load("images/Player1/player_standing/img2.png")
player1_stand2 = pygame.transform.scale(player1_stand2, (102, 102))
player1_stand3 = pygame.image.load("images/Player1/player_standing/img3.png")
player1_stand3 = pygame.transform.scale(player1_stand3, (102, 102))
player1_stand2 = pygame.image.load("images/Player1/player_standing/img2.png")
player1_stand2 = pygame.transform.scale(player1_stand2, (102, 102))
player1_stand1 = pygame.image.load("images/Player1/player_standing/img1.png")
player1_stand1 = pygame.transform.scale(player1_stand1, (102, 102))

player1_poisonedStand0 = pygame.image.load("images/Player1/player_poisonedStanding/img0.png")
player1_poisonedStand0 = pygame.transform.scale(player1_poisonedStand0, (102, 102))
player1_poisonedStand1 = pygame.image.load("images/Player1/player_poisonedStanding/img1.png")
player1_poisonedStand1 = pygame.transform.scale(player1_poisonedStand1, (102, 102))
player1_poisonedStand2 = pygame.image.load("images/Player1/player_poisonedStanding/img2.png")
player1_poisonedStand2 = pygame.transform.scale(player1_poisonedStand2, (102, 102))
player1_poisonedStand3 = pygame.image.load("images/Player1/player_poisonedStanding/img3.png")
player1_poisonedStand3 = pygame.transform.scale(player1_poisonedStand3, (102, 102))
player1_poisonedStand4 = pygame.image.load("images/Player1/player_poisonedStanding/img2.png")
player1_poisonedStand4 = pygame.transform.scale(player1_poisonedStand4, (102, 102))
player1_poisonedStand5 = pygame.image.load("images/Player1/player_poisonedStanding/img1.png")
player1_poisonedStand5 = pygame.transform.scale(player1_poisonedStand5, (102, 102))

player2_stand0 = pygame.image.load("images/Player2/player_standing/img0.png")
player2_stand0 = pygame.transform.scale(player2_stand0, (102, 102))
player2_stand1 = pygame.image.load("images/Player2/player_standing/img1.png")
player2_stand1 = pygame.transform.scale(player2_stand1, (102, 102))
player2_stand2 = pygame.image.load("images/Player2/player_standing/img2.png")
player2_stand2 = pygame.transform.scale(player2_stand2, (102, 102))
player2_stand3 = pygame.image.load("images/Player2/player_standing/img3.png")
player2_stand3 = pygame.transform.scale(player2_stand3, (102, 102))

player2_poisonedStand0 = pygame.image.load("images/Player2/player_poisoned_standing/img0.png")
player2_poisonedStand0 = pygame.transform.scale(player2_poisonedStand0, (102, 102))
player2_poisonedStand1 = pygame.image.load("images/Player2/player_poisoned_standing/img1.png")
player2_poisonedStand1 = pygame.transform.scale(player2_poisonedStand1, (102, 102))
player2_poisonedStand2 = pygame.image.load("images/Player2/player_poisoned_standing/img2.png")
player2_poisonedStand2 = pygame.transform.scale(player2_poisonedStand2, (102, 102))
player2_poisonedStand3 = pygame.image.load("images/Player2/player_poisoned_standing/img3.png")
player2_poisonedStand3 = pygame.transform.scale(player2_poisonedStand3, (102, 102))

player1_fight0 = pygame.image.load('images/Player1/player_fighting/img0.png')
player1_fight0 = pygame.transform.scale(player1_fight0, (102, 102))
player1_fight1 = pygame.image.load('images/Player1/player_fighting/img1.png')
player1_fight1 = pygame.transform.scale(player1_fight1, (102, 102))
player1_fight2 = pygame.image.load('images/Player1/player_fighting/img2.png')
player1_fight2 = pygame.transform.scale(player1_fight2, (102, 102))

player1_poisonedFight0 = pygame.image.load('images/Player1/player_poisonedFighting/img0.png')
player1_poisonedFight0 = pygame.transform.scale(player1_poisonedFight0, (102, 102))
player1_poisonedFight2 = pygame.image.load('images/Player1/player_poisonedFighting/img2.png')
player1_poisonedFight2 = pygame.transform.scale(player1_poisonedFight2, (102, 102))

player2_fight0 = pygame.image.load('images/Player2/player_fighting/img0.png')
player2_fight0 = pygame.transform.scale(player2_fight0, (102, 102))
player2_fight1 = pygame.image.load('images/Player2/player_fighting/img1.png')
player2_fight1 = pygame.transform.scale(player2_fight1, (102, 102))
player2_fight2 = pygame.image.load('images/Player2/player_fighting/img2.png')
player2_fight2 = pygame.transform.scale(player2_fight2, (102, 102))

player2_poisonedFight0 = pygame.image.load('images/Player2/player_poisoned_fighting/img0.png')
player2_poisonedFight0 = pygame.transform.scale(player2_poisonedFight0, (102, 102))
player2_poisonedFight2 = pygame.image.load('images/Player2/player_poisoned_fighting/img2.png')
player2_poisonedFight2 = pygame.transform.scale(player2_poisonedFight2, (102, 102))

player2_block0 = pygame.image.load('images/Player2/player_block/img0.png')
player2_block0 = pygame.transform.scale(player2_block0, (102, 102))
player2_block1 = pygame.image.load('images/Player2/player_block/img1.png')
player2_block1 = pygame.transform.scale(player2_block1, (102, 102))
player2_block2 = pygame.image.load('images/Player2/player_block/img2.png')
player2_block2 = pygame.transform.scale(player2_block2, (102, 102))
player2_block3 = pygame.image.load('images/Player2/player_block/img3.png')
player2_block3 = pygame.transform.scale(player2_block3, (102, 102))
player2_block4 = pygame.image.load('images/Player2/player_block/img4.png')
player2_block4 = pygame.transform.scale(player2_block4, (102, 102))
player2_block5 = pygame.image.load('images/Player2/player_block/img5.png')
player2_block5 = pygame.transform.scale(player2_block5, (102, 102))

player2_poisonedBlock0 = pygame.image.load('images/Player2/player_poisoned_block/img0.png')
player2_poisonedBlock0 = pygame.transform.scale(player2_poisonedBlock0, (102, 102))
player2_poisonedBlock1 = pygame.image.load('images/Player2/player_poisoned_block/img1.png')
player2_poisonedBlock1 = pygame.transform.scale(player2_poisonedBlock1, (102, 102))
player2_poisonedBlock2 = pygame.image.load('images/Player2/player_poisoned_block/img2.png')
player2_poisonedBlock2 = pygame.transform.scale(player2_poisonedBlock2, (102, 102))
player2_poisonedBlock3 = pygame.image.load('images/Player2/player_poisoned_block/img3.png')
player2_poisonedBlock3 = pygame.transform.scale(player2_poisonedBlock3, (102, 102))
player2_poisonedBlock4 = pygame.image.load('images/Player2/player_poisoned_block/img4.png')
player2_poisonedBlock4 = pygame.transform.scale(player2_poisonedBlock4, (102, 102))
player2_poisonedBlock5 = pygame.image.load('images/Player2/player_poisoned_block/img5.png')
player2_poisonedBlock5 = pygame.transform.scale(player2_poisonedBlock5, (102, 102))

player1_walk0 = pygame.image.load('images/Player1/player_walking/img0.png')
player1_walk0 = pygame.transform.scale(player1_walk0, (102, 102))
player1_walk1 = pygame.image.load('images/Player1/player_walking/img1.png')
player1_walk1 = pygame.transform.scale(player1_walk1, (102, 102))
player1_walk2 = pygame.image.load('images/Player1/player_walking/img2.png')
player1_walk2 = pygame.transform.scale(player1_walk2, (102, 102))
player1_walk3 = pygame.image.load('images/Player1/player_walking/img3.png')
player1_walk3 = pygame.transform.scale(player1_walk3, (102, 102))
player1_walk4 = pygame.image.load('images/Player1/player_walking/img4.png')
player1_walk4 = pygame.transform.scale(player1_walk4, (102, 102))

player1_poisonedWalk0 = pygame.image.load('images/Player1/player_poisonedWalking/img0.png')
player1_poisonedWalk0 = pygame.transform.scale(player1_poisonedWalk0, (102, 102))
player1_poisonedWalk1 = pygame.image.load('images/Player1/player_poisonedWalking/img1.png')
player1_poisonedWalk1 = pygame.transform.scale(player1_poisonedWalk1, (102, 102))
player1_poisonedWalk2 = pygame.image.load('images/Player1/player_poisonedWalking/img2.png')
player1_poisonedWalk2 = pygame.transform.scale(player1_poisonedWalk2, (102, 102))
player1_poisonedWalk3 = pygame.image.load('images/Player1/player_poisonedWalking/img3.png')
player1_poisonedWalk3 = pygame.transform.scale(player1_poisonedWalk3, (102, 102))
player1_poisonedWalk4 = pygame.image.load('images/Player1/player_poisonedWalking/img4.png')
player1_poisonedWalk4 = pygame.transform.scale(player1_poisonedWalk4, (102, 102))

player2_walk0 = pygame.image.load('images/Player2/player_walking/img0.png')
player2_walk0 = pygame.transform.scale(player2_walk0, (102, 102))
player2_walk1 = pygame.image.load('images/Player2/player_walking/img1.png')
player2_walk1 = pygame.transform.scale(player2_walk1, (102, 102))
player2_walk2 = pygame.image.load('images/Player2/player_walking/img2.png')
player2_walk2 = pygame.transform.scale(player2_walk2, (102, 102))
player2_walk3 = pygame.image.load('images/Player2/player_walking/img3.png')
player2_walk3 = pygame.transform.scale(player2_walk3, (102, 102))
player2_walk4 = pygame.image.load('images/Player2/player_walking/img4.png')
player2_walk4 = pygame.transform.scale(player2_walk4, (102, 102))

player2_poisoned_walk0 = pygame.image.load('images/Player2/player_poisoned_walking/img0.png')
player2_poisoned_walk0 = pygame.transform.scale(player2_poisoned_walk0, (102, 102))
player2_poisoned_walk1 = pygame.image.load('images/Player2/player_poisoned_walking/img1.png')
player2_poisoned_walk1 = pygame.transform.scale(player2_poisoned_walk1, (102, 102))
player2_poisoned_walk2 = pygame.image.load('images/Player2/player_poisoned_walking/img2.png')
player2_poisoned_walk2 = pygame.transform.scale(player2_poisoned_walk2, (102, 102))
player2_poisoned_walk3 = pygame.image.load('images/Player2/player_poisoned_walking/img3.png')
player2_poisoned_walk3 = pygame.transform.scale(player2_poisoned_walk3, (102, 102))
player2_poisoned_walk4 = pygame.image.load('images/Player2/player_poisoned_walking/img4.png')
player2_poisoned_walk4 = pygame.transform.scale(player2_poisoned_walk4, (102, 102))

player1_death0 = pygame.image.load("images/Player1/player_death/0.png")
player1_death0 = pygame.transform.scale(player1_death0, (102, 102))
player1_death1 = pygame.image.load("images/Player1/player_death/1.png")
player1_death1 = pygame.transform.scale(player1_death1, (102, 102))
player1_death2 = pygame.image.load("images/Player1/player_death/2.png")
player1_death2 = pygame.transform.scale(player1_death2, (102, 102))
player1_death3 = pygame.image.load("images/Player1/player_death/3.png")
player1_death3 = pygame.transform.scale(player1_death3, (102, 102))
player1_death4 = pygame.image.load("images/Player1/player_death/4.png")
player1_death4 = pygame.transform.scale(player1_death4, (102, 102))
player1_death5 = pygame.image.load("images/Player1/player_death/5.png")
player1_death5 = pygame.transform.scale(player1_death5, (102, 102))

player1_jump0 = pygame.image.load("images/Player1/player_jumping/img0.png")
player1_jump0 = pygame.transform.scale(player1_jump0, (102, 102))
player1_jump1 = pygame.image.load("images/Player1/player_jumping/img1.png")
player1_jump1 = pygame.transform.scale(player1_jump1, (102, 102))
player1_jump2 = pygame.image.load("images/Player1/player_jumping/img2.png")
player1_jump2 = pygame.transform.scale(player1_jump2, (102, 102))

player2_jump0 = pygame.image.load("images/Player2/player_jumping/img0.png")
player2_jump0 = pygame.transform.scale(player2_jump0, (102, 102))
player2_jump1 = pygame.image.load("images/Player2/player_jumping/img1.png")
player2_jump1 = pygame.transform.scale(player2_jump1, (102, 102))
player2_jump2 = pygame.image.load("images/Player2/player_jumping/img2.png")
player2_jump2 = pygame.transform.scale(player2_jump2, (102, 102))

player1_poisonedJump0 = pygame.image.load("images/Player1/player_poisonedJumping/img0.png")
player1_poisonedJump0 = pygame.transform.scale(player1_poisonedJump0, (102, 102))
player1_poisonedJump1 = pygame.image.load("images/Player1/player_poisonedJumping/img1.png")
player1_poisonedJump1 = pygame.transform.scale(player1_poisonedJump1, (102, 102))
player1_poisonedJump2 = pygame.image.load("images/Player1/player_poisonedJumping/img2.png")
player1_poisonedJump2 = pygame.transform.scale(player1_poisonedJump2, (102, 102))

player2_poisonedJump0 = pygame.image.load("images/Player2/player_poisoned_jumping/img0.png")
player2_poisonedJump0 = pygame.transform.scale(player2_poisonedJump0, (102, 102))
player2_poisonedJump1 = pygame.image.load("images/Player2/player_poisoned_jumping/img1.png")
player2_poisonedJump1 = pygame.transform.scale(player2_poisonedJump1, (102, 102))
player2_poisonedJump2 = pygame.image.load("images/Player2/player_poisoned_jumping/img2.png")
player2_poisonedJump2 = pygame.transform.scale(player2_poisonedJump2, (102, 102))
def makePlayer1(x, y):
    entity = engine.Entity()
    entity.position = engine.Position(x,y, 45, 100)
    entityStandingAnimation1 = engine.Animation([player1_stand0, player1_stand1,
                                                 player1_stand2, player1_stand3, player1_stand2, player1_stand1])
    entityPoisonedStandingAnimation1 = engine.Animation(
        [player1_poisonedStand0, player1_poisonedStand1, player1_poisonedStand2,
         player1_poisonedStand3, player1_poisonedStand4, player1_poisonedStand5])
    entityWalkingAnimation1 = engine.Animation([player1_walk0, player1_walk1,
                                                player1_walk2, player1_walk3, player1_walk4])
    entityPoisonedWalkingAnimation1 = engine.Animation(
        [player1_poisonedWalk0, player1_poisonedWalk1, player1_poisonedWalk2, player1_poisonedWalk3, player1_poisonedWalk4])
    entityFightingAnimation = engine.deathAnimation([player1_fight0, player1_fight2])
    entityPoisonedFightingAnimation = engine.deathAnimation([player1_poisonedFight0, player1_poisonedFight2])
    entityJumpingAnimation = engine.deathAnimation([player1_jump0, player1_jump1, player1_jump2, player1_jump2, player1_jump2])
    entityPoisonedJumpingAnimation = engine.deathAnimation([player1_poisonedJump0, player1_poisonedJump1,
                                                            player1_poisonedJump2, player1_poisonedJump2, player1_poisonedJump2])
    entityDeathAnimation = engine.deathAnimation([player1_death0, player1_death1, player1_death2,
                                                  player1_death3, player1_death4, player1_death5])
    entity.animations.add('standing1', entityStandingAnimation1)
    entity.animations.add('standing', entityStandingAnimation1)
    entity.animations.add("poisonedStanding1", entityPoisonedStandingAnimation1)
    entity.animations.add('walking1', entityWalkingAnimation1)
    entity.animations.add('poisonedWalking1', entityPoisonedWalkingAnimation1)
    entity.animations.add('fighting', entityFightingAnimation)
    entity.animations.add('poisonedFighting1', entityPoisonedFightingAnimation)
    entity.animations.add('jumping', entityJumpingAnimation)
    entity.animations.add('poisonedJumping', entityPoisonedJumpingAnimation)
    entity.animations.add('death', entityDeathAnimation)

    entityStandingAnimation2 = engine.Animation([player2_stand0, player2_stand1, player2_stand2, player2_stand3])
    entityPoisonedStandingAnimation2 = engine.Animation([player2_poisonedStand0, player2_poisonedStand1, player2_poisonedStand2, player2_poisonedStand3])
    entityWalkingAnimation2 = engine.Animation([player2_walk0, player2_walk1, player2_walk2, player2_walk3, player2_walk4])
    entityPoisonedWalkingAnimation2 = engine.Animation([player2_poisoned_walk0, player2_poisoned_walk1, player2_poisoned_walk2, player2_poisoned_walk3,
    player2_poisoned_walk4])
    entityFightingAnimation2 = engine.deathAnimation([player2_fight0, player2_fight2])
    entityPoisonedFightingAnimation2 = engine.deathAnimation([player2_poisonedFight0, player2_poisonedFight2])
    entityBlockAnimation = engine.Animation([player2_block0, player2_block1, player2_block2, player2_block3, player2_block4, player2_block5])
    entityJumpingAnimation1 = engine.deathAnimation([player2_jump0, player2_jump1, player2_jump2, player2_jump2, player2_jump2])
    entityPoisonedJumpingAnimation1 = engine.deathAnimation(
        [player2_poisonedJump0, player2_poisonedJump1, player2_poisonedJump2, player2_poisonedJump2, player2_poisonedJump2])
    entityPoisonedBlockAnimation = engine.Animation(
        [player2_poisonedBlock0, player2_poisonedBlock1, player2_poisonedBlock2, player2_poisonedBlock3, player2_poisonedBlock4, player2_poisonedBlock5])

    entity.animations.add('standing2', entityStandingAnimation2)
    entity.animations.add('standing3', entityStandingAnimation2)
    entity.animations.add('poisonedStanding2', entityPoisonedStandingAnimation2)
    entity.animations.add('walking2', entityWalkingAnimation2)
    entity.animations.add('poisonedWalking2', entityPoisonedWalkingAnimation2)
    entity.animations.add('fighting2', entityFightingAnimation2)
    entity.animations.add('poisonedFighting2', entityPoisonedFightingAnimation2)
    entity.animations.add("block1", entityBlockAnimation)
    entity.animations.add("jumping1", entityJumpingAnimation1)
    entity.animations.add("poisonedJumping1", entityPoisonedJumpingAnimation1)
    entity.animations.add("poisonedBlock1", entityPoisonedBlockAnimation)
    entity.damage = 5
    entity.sword_lvl = 0
    entity.intention = engine.Intention()
    entity.acceleration = 0.2
    entity.type = 'player'
    entity.name = "Player2"
    return entity

enemy_stand0 = pygame.image.load('images/Enemy/enemy_standing/0.png')
enemy_stand0 = pygame.transform.scale(enemy_stand0, (60, 120))
enemy_stand1 = pygame.image.load('images/Enemy/enemy_standing/1.png')
enemy_stand1 = pygame.transform.scale(enemy_stand1, (60, 120))
enemy_stand2 = pygame.image.load('images/Enemy/enemy_standing/2.png')
enemy_stand2 = pygame.transform.scale(enemy_stand2, (60, 120))

enemy_attack0 = pygame.image.load("images/Enemy/enemy_attack/0.png")
enemy_attack0 = pygame.transform.scale(enemy_attack0, (60, 120))
enemy_attack1 = pygame.image.load("images/Enemy/enemy_attack/1.png")
enemy_attack1 = pygame.transform.scale(enemy_attack1, (60, 120))
enemy_attack2 = pygame.image.load("images/Enemy/enemy_attack/2.png")
enemy_attack2 = pygame.transform.scale(enemy_attack2, (60, 120))
enemy_attack3 = pygame.image.load("images/Enemy/enemy_attack/3.png")
enemy_attack3 = pygame.transform.scale(enemy_attack3, (84, 120))
enemy_attack4 = pygame.image.load("images/Enemy/enemy_attack/4.png")
enemy_attack4 = pygame.transform.scale(enemy_attack4, (70, 120))
enemy_attack5 = pygame.image.load("images/Enemy/enemy_attack/5.png")
enemy_attack5 = pygame.transform.scale(enemy_attack5, (76, 120))

enemy_walking0 = pygame.image.load("images/Enemy/enemy_walking/0.png")
enemy_walking0 = pygame.transform.scale(enemy_walking0, (70, 120))
enemy_walking1 = pygame.image.load("images/Enemy/enemy_walking/1.png")
enemy_walking1 = pygame.transform.scale(enemy_walking1, (70, 120))
enemy_walking2 = pygame.image.load("images/Enemy/enemy_walking/2.png")
enemy_walking2 = pygame.transform.scale(enemy_walking2, (54, 120))
enemy_walking3 = pygame.image.load("images/Enemy/enemy_walking/3.png")
enemy_walking3 = pygame.transform.scale(enemy_walking3, (54, 120))
enemy_walking4 = pygame.image.load("images/Enemy/enemy_walking/4.png")
enemy_walking4 = pygame.transform.scale(enemy_walking4, (54, 120))
enemy_walking5 = pygame.image.load("images/Enemy/enemy_walking/5.png")
enemy_walking5 = pygame.transform.scale(enemy_walking5, (54, 120))
enemy_walking6 = pygame.image.load("images/Enemy/enemy_walking/6.png")
enemy_walking6 = pygame.transform.scale(enemy_walking6, (54, 120))
enemy_walking7 = pygame.image.load("images/Enemy/enemy_walking/7.png")
enemy_walking7 = pygame.transform.scale(enemy_walking7, (54, 120))

enemy_death0 = pygame.image.load("images/Enemy/enemy_death/0.png")
enemy_death0 = pygame.transform.scale(enemy_death0, (70, 120))
enemy_death1 = pygame.image.load("images/Enemy/enemy_death/1.png")
enemy_death1 = pygame.transform.scale(enemy_death1, (100, 120))
enemy_death2 = pygame.image.load("images/Enemy/enemy_death/2.png")
enemy_death2 = pygame.transform.scale(enemy_death2, (108, 120))
enemy_death3 = pygame.image.load("images/Enemy/enemy_death/3.png")
enemy_death3 = pygame.transform.scale(enemy_death3, (108, 120))
enemy_death4 = pygame.image.load("images/Enemy/enemy_death/4.png")
enemy_death4 = pygame.transform.scale(enemy_death4, (108, 120))
enemy_death5 = pygame.image.load("images/Enemy/enemy_death/5.png")
enemy_death5 = pygame.transform.scale(enemy_death5, (108, 120))
def makeEnemy(x, y, damage, potions):
    entity = engine.Entity()
    entity.x = x
    entity.y = y
    entity.position = engine.Position(entity.x, entity.y, 60, 300)
    entity.rect = pygame.rect.Rect(480, 340, 150, 150)
    entityStandingAnimation = engine.Animation([enemy_stand0, enemy_stand1, enemy_stand2])
    entityAttackAnimation = engine.Animation([enemy_attack2, enemy_attack5])
    entityWalkingAnimation = engine.Animation([enemy_walking0, enemy_walking1, enemy_walking2, enemy_walking3, enemy_walking4, enemy_walking5, enemy_walking6, enemy_walking7])
    entityDeathAnimation = engine.deathAnimation([enemy_death0, enemy_death1, enemy_death2, enemy_death3, enemy_death4, enemy_death5])
    entity.animations.add('standing', entityStandingAnimation)
    entity.animations.add("attack", entityAttackAnimation)
    entity.animations.add("walking", entityWalkingAnimation)
    entity.animations.add("death", entityDeathAnimation)
    entity.damage = damage
    entity.potions = potions
    entity.type = 'enemy'
    entity.name = 'Enemy0'
    return entity

enemy1_stand0 = pygame.image.load("images/Enemy1/enemy_standing/0.png")
enemy1_stand0 = pygame.transform.scale(enemy1_stand0, (70, 113))

enemy1_block0 = pygame.image.load("images/Enemy1/enemy_block/0.png")
enemy1_block0 = pygame.transform.scale(enemy1_block0, (70, 113))

enemy1_attack0 = pygame.image.load("images/Enemy1/enemy_attack/0.png")
enemy1_attack0 = pygame.transform.scale(enemy1_attack0, (70, 113))
enemy1_attack1 = pygame.image.load("images/Enemy1/enemy_attack/1.png")
enemy1_attack1 = pygame.transform.scale(enemy1_attack1, (73, 113))
enemy1_attack2 = pygame.image.load("images/Enemy1/enemy_attack/2.png")
enemy1_attack2 = pygame.transform.scale(enemy1_attack2, (105, 113))

enemy1_walking0 = pygame.image.load("images/Enemy1/enemy_walking/0.png")
enemy1_walking0 = pygame.transform.scale(enemy1_walking0, (70, 113))
enemy1_walking1 = pygame.image.load("images/Enemy1/enemy_walking/1.png")
enemy1_walking1 = pygame.transform.scale(enemy1_walking1, (70, 113))
enemy1_walking2 = pygame.image.load("images/Enemy1/enemy_walking/2.png")
enemy1_walking2 = pygame.transform.scale(enemy1_walking2, (70, 113))
enemy1_walking3 = pygame.image.load("images/Enemy1/enemy_walking/3.png")
enemy1_walking3 = pygame.transform.scale(enemy1_walking3, (70, 113))
enemy1_walking4 = pygame.image.load("images/Enemy1/enemy_walking/4.png")
enemy1_walking4 = pygame.transform.scale(enemy1_walking4, (70, 113))

enemy1_death0 = pygame.image.load("images/Enemy1/enemy_death/0.png")
enemy1_death0 = pygame.transform.scale(enemy1_death0, (70, 113))
enemy1_death1 = pygame.image.load("images/Enemy1/enemy_death/1.png")
enemy1_death1 = pygame.transform.scale(enemy1_death1, (78, 113))
enemy1_death2 = pygame.image.load("images/Enemy1/enemy_death/2.png")
enemy1_death2 = pygame.transform.scale(enemy1_death2, (103, 113))
enemy1_death3 = pygame.image.load("images/Enemy1/enemy_death/3.png")
enemy1_death3 = pygame.transform.scale(enemy1_death3, (113, 113))
enemy1_death4 = pygame.image.load("images/Enemy1/enemy_death/4.png")
enemy1_death4 = pygame.transform.scale(enemy1_death4, (113, 113))
enemy1_death5 = pygame.image.load("images/Enemy1/enemy_death/5.png")
enemy1_death5 = pygame.transform.scale(enemy1_death5, (108, 113))
def makeEnemy1(x, y, damage, potions):
    entity = engine.Entity()
    entity.x = x
    entity.y = y
    entity.position = engine.Position(entity.x, entity.y, 80, 300)
    entity.rect = pygame.rect.Rect(480, 340, 150, 150)
    entityStandingAnimation = engine.Animation([enemy1_stand0])
    entityAttackAnimation = engine.Animation([enemy1_attack0, enemy1_attack2])
    entityBlockAnimation = engine.Animation([enemy1_block0])
    entityWalkingAnimation = engine.Animation([enemy1_walking0, enemy1_walking1, enemy1_walking2, enemy1_walking3, enemy1_walking4])
    entityDeathAnimation = engine.deathAnimation([enemy1_death0, enemy1_death1, enemy1_death2, enemy1_death3, enemy1_death4, enemy1_death5])
    entity.animations.add('standing', entityStandingAnimation)
    entity.animations.add("attack", entityAttackAnimation)
    entity.animations.add("block", entityBlockAnimation)
    entity.animations.add("walking", entityWalkingAnimation)
    entity.animations.add("death", entityDeathAnimation)
    entity.damage = damage
    entity.potions = potions
    entity.type = 'enemy'
    entity.name = "Enemy1"
    return entity

enemy2_stand0 = pygame.image.load("images/Enemy2/enemy_standing/0.png")
enemy2_stand0 = pygame.transform.scale(enemy2_stand0, (81, 180))

enemy2_walking0 = pygame.image.load("images/Enemy2/enemy_walking/0.png")
enemy2_walking0 = pygame.transform.scale(enemy2_walking0, (81, 180))
enemy2_walking1 = pygame.image.load("images/Enemy2/enemy_walking/1.png")
enemy2_walking1 = pygame.transform.scale(enemy2_walking1, (81, 180))
enemy2_walking2 = pygame.image.load("images/Enemy2/enemy_walking/2.png")
enemy2_walking2 = pygame.transform.scale(enemy2_walking2, (81, 180))
enemy2_walking3 = pygame.image.load("images/Enemy2/enemy_walking/3.png")
enemy2_walking3 = pygame.transform.scale(enemy2_walking3, (81, 180))
enemy2_walking4 = pygame.image.load("images/Enemy2/enemy_walking/4.png")
enemy2_walking4 = pygame.transform.scale(enemy2_walking4, (81, 180))

enemy2_attack0 = pygame.image.load("images/Enemy2/enemy_attack/0.png")
enemy2_attack0 = pygame.transform.scale(enemy2_attack0, (81, 180))
enemy2_attack1 = pygame.image.load("images/Enemy2/enemy_attack/1.png")
enemy2_attack1 = pygame.transform.scale(enemy2_attack1, (81, 180))
enemy2_attack2 = pygame.image.load("images/Enemy2/enemy_attack/2.png")
enemy2_attack2 = pygame.transform.scale(enemy2_attack2, (81, 180))
enemy2_attack3 = pygame.image.load("images/Enemy2/enemy_attack/3.png")
enemy2_attack3 = pygame.transform.scale(enemy2_attack3, (81, 180))
enemy2_attack4 = pygame.image.load("images/Enemy2/enemy_attack/4.png")
enemy2_attack4 = pygame.transform.scale(enemy2_attack4, (81, 180))
enemy2_attack5 = pygame.image.load("images/Enemy2/enemy_attack/5.png")
enemy2_attack5 = pygame.transform.scale(enemy2_attack5, (93, 180))

enemy2_death0 = pygame.image.load("images/Enemy2/enemy_death/0.png")
enemy2_death0 = pygame.transform.scale(enemy2_death0, (81, 180))
enemy2_death1 = pygame.image.load("images/Enemy2/enemy_death/1.png")
enemy2_death1 = pygame.transform.scale(enemy2_death1, (75, 180))
enemy2_death2 = pygame.image.load("images/Enemy2/enemy_death/2.png")
enemy2_death2 = pygame.transform.scale(enemy2_death2, (84, 180))
enemy2_death3 = pygame.image.load("images/Enemy2/enemy_death/3.png")
enemy2_death3 = pygame.transform.scale(enemy2_death3, (99, 180))
enemy2_death4 = pygame.image.load("images/Enemy2/enemy_death/4.png")
enemy2_death4 = pygame.transform.scale(enemy2_death4, (99, 180))
enemy2_death5 = pygame.image.load("images/Enemy2/enemy_death/5.png")
enemy2_death5 = pygame.transform.scale(enemy2_death5, (99, 180))

def makeEnemy2(x, y, damage, potions):
    entity = engine.Entity()
    entity.x = x
    entity.y = y
    entity.position = engine.Position(entity.x, entity.y, 80, 300)
    entity.rect = pygame.rect.Rect(480, 340, 150, 150)
    entityStandingAnimation = engine.Animation([enemy2_stand0])
    entityAttackAnimation = engine.Animation([enemy2_attack1, enemy2_attack2, enemy2_attack3, enemy2_attack4, enemy2_attack5])
    entityWalkingAnimation = engine.Animation([enemy2_walking0, enemy2_walking1, enemy2_walking2, enemy2_walking3, enemy2_walking4])
    entityDeathAnimation = engine.deathAnimation([enemy2_death0, enemy2_death1, enemy2_death2, enemy2_death3, enemy2_death4, enemy2_death5])
    entity.animations.add('standing', entityStandingAnimation)
    entity.animations.add("attack", entityAttackAnimation)
    entity.animations.add("walking", entityWalkingAnimation)
    entity.animations.add("death", entityDeathAnimation)
    entity.damage = damage
    entity.potions = potions
    entity.type = 'enemy'
    entity.name = "Enemy2"
    return entity

enemy3_stand0 = pygame.image.load("images/Enemy3/enemy_standing/0.png")
enemy3_stand0 = pygame.transform.scale(enemy3_stand0, (81, 180))

enemy3_walking1 = pygame.image.load("images/Enemy3/enemy_walking/1.png")
enemy3_walking1 = pygame.transform.scale(enemy3_walking1, (81, 180))
enemy3_walking2 = pygame.image.load("images/Enemy3/enemy_walking/2.png")
enemy3_walking2 = pygame.transform.scale(enemy3_walking2, (81, 180))
enemy3_walking3 = pygame.image.load("images/Enemy3/enemy_walking/3.png")
enemy3_walking3 = pygame.transform.scale(enemy3_walking3, (81, 180))
enemy3_walking4 = pygame.image.load("images/Enemy3/enemy_walking/4.png")
enemy3_walking4 = pygame.transform.scale(enemy3_walking4, (81, 180))

enemy3_attack0 = pygame.image.load("images/Enemy3/enemy_attack/0.png")
enemy3_attack0 = pygame.transform.scale(enemy3_attack0, (69, 180))
enemy3_attack1 = pygame.image.load("images/Enemy3/enemy_attack/1.png")
enemy3_attack1 = pygame.transform.scale(enemy3_attack1, (66, 180))
enemy3_attack2 = pygame.image.load("images/Enemy3/enemy_attack/2.png")
enemy3_attack2 = pygame.transform.scale(enemy3_attack2, (60, 180))
enemy3_attack3 = pygame.image.load("images/Enemy3/enemy_attack/3.png")
enemy3_attack3 = pygame.transform.scale(enemy3_attack3, (57, 180))
enemy3_attack4 = pygame.image.load("images/Enemy3/enemy_attack/4.png")
enemy3_attack4 = pygame.transform.scale(enemy3_attack4, (66, 180))
enemy3_attack5 = pygame.image.load("images/Enemy3/enemy_attack/5.png")
enemy3_attack5 = pygame.transform.scale(enemy3_attack5, (57, 180))

enemy3_death0 = pygame.image.load("images/Enemy3/enemy_death/0.png")
enemy3_death0 = pygame.transform.scale(enemy3_death0, (81, 180))
enemy3_death1 = pygame.image.load("images/Enemy3/enemy_death/1.png")
enemy3_death1 = pygame.transform.scale(enemy3_death1, (75, 180))
enemy3_death2 = pygame.image.load("images/Enemy3/enemy_death/2.png")
enemy3_death2 = pygame.transform.scale(enemy3_death2, (84, 180))
enemy3_death3 = pygame.image.load("images/Enemy3/enemy_death/3.png")
enemy3_death3 = pygame.transform.scale(enemy3_death3, (99, 180))
enemy3_death4 = pygame.image.load("images/Enemy3/enemy_death/4.png")
enemy3_death4 = pygame.transform.scale(enemy3_death4, (99, 180))
enemy3_death5 = pygame.image.load("images/Enemy3/enemy_death/5.png")
enemy3_death5 = pygame.transform.scale(enemy3_death5, (99, 180))

def makeEnemy3(x, y, damage, potions):
    entity = engine.Entity()
    entity.x = x
    entity.y = y
    entity.position = engine.Position(entity.x, entity.y, 80, 300)
    entity.rect = pygame.rect.Rect(480, 340, 150, 150)
    entityStandingAnimation = engine.Animation([enemy3_stand0])
    entityAttackAnimation = engine.Animation([enemy3_attack0, enemy3_attack1, enemy3_attack2, enemy3_attack3, enemy3_attack4, enemy3_attack5])
    entityWalkingAnimation = engine.Animation([enemy3_walking1, enemy3_walking2, enemy3_walking3, enemy3_walking4])
    entityDeathAnimation = engine.deathAnimation([enemy3_death0, enemy3_death1, enemy3_death2, enemy3_death3, enemy3_death4, enemy3_death5])
    entity.animations.add('standing', entityStandingAnimation)
    entity.animations.add("attack", entityAttackAnimation)
    entity.animations.add("walking", entityWalkingAnimation)
    entity.animations.add("death", entityDeathAnimation)
    entity.damage = damage
    entity.potions = potions
    entity.type = 'enemy'
    entity.name = "Enemy3"
    return entity

enemy4_stand0 = pygame.image.load("images/Enemy4/enemy_standing/0.png")
enemy4_stand0 = pygame.transform.scale(enemy4_stand0, (99, 180))
enemy4_stand1 = pygame.image.load("images/Enemy4/enemy_standing/1.png")
enemy4_stand1 = pygame.transform.scale(enemy4_stand1, (99, 180))
enemy4_stand2 = pygame.image.load("images/Enemy4/enemy_standing/2.png")
enemy4_stand2 = pygame.transform.scale(enemy4_stand2, (99, 180))
enemy4_stand3 = pygame.image.load("images/Enemy4/enemy_standing/3.png")
enemy4_stand3 = pygame.transform.scale(enemy4_stand3, (99, 180))

enemy4_walking0 = pygame.image.load("images/Enemy4/enemy_walking/0.png")
enemy4_walking0 = pygame.transform.scale(enemy4_walking0, (99, 180))
enemy4_walking1 = pygame.image.load("images/Enemy4/enemy_walking/1.png")
enemy4_walking1 = pygame.transform.scale(enemy4_walking1, (99, 180))
enemy4_walking2 = pygame.image.load("images/Enemy4/enemy_walking/2.png")
enemy4_walking2 = pygame.transform.scale(enemy4_walking2, (99, 180))
enemy4_walking3 = pygame.image.load("images/Enemy4/enemy_walking/3.png")
enemy4_walking3 = pygame.transform.scale(enemy4_walking3, (99, 180))

enemy4_attack0 = pygame.image.load("images/Enemy4/enemy_attack/0.png")
enemy4_attack0 = pygame.transform.scale(enemy4_attack0, (99, 180))
enemy4_attack1 = pygame.image.load("images/Enemy4/enemy_attack/1.png")
enemy4_attack1 = pygame.transform.scale(enemy4_attack1, (126, 180))
enemy4_attack2 = pygame.image.load("images/Enemy4/enemy_attack/2.png")
enemy4_attack2 = pygame.transform.scale(enemy4_attack2, (132, 180))
enemy4_attack3 = pygame.image.load("images/Enemy4/enemy_attack/3.png")
enemy4_attack3 = pygame.transform.scale(enemy4_attack3, (132, 180))

enemy4_shoot0 = pygame.image.load("images/Enemy4/enemy_shoot/0.png")
enemy4_shoot0 = pygame.transform.scale(enemy4_shoot0, (99, 180))
enemy4_shoot1 = pygame.image.load("images/Enemy4/enemy_shoot/1.png")
enemy4_shoot1 = pygame.transform.scale(enemy4_shoot1, (99, 180))
enemy4_shoot2 = pygame.image.load("images/Enemy4/enemy_shoot/2.png")
enemy4_shoot2 = pygame.transform.scale(enemy4_shoot2, (102, 180))
enemy4_shoot3 = pygame.image.load("images/Enemy4/enemy_shoot/3.png")
enemy4_shoot3 = pygame.transform.scale(enemy4_shoot3, (93, 180))

enemy4_death0 = pygame.image.load("images/Enemy4/enemy_death/0.png")
enemy4_death0 = pygame.transform.scale(enemy4_death0, (93, 180))
enemy4_death1 = pygame.image.load("images/Enemy4/enemy_death/1.png")
enemy4_death1 = pygame.transform.scale(enemy4_death1, (93, 180))
enemy4_death2 = pygame.image.load("images/Enemy4/enemy_death/2.png")
enemy4_death2 = pygame.transform.scale(enemy4_death2, (93, 180))
enemy4_death3 = pygame.image.load("images/Enemy4/enemy_death/3.png")
enemy4_death3 = pygame.transform.scale(enemy4_death3, (93, 180))
enemy4_death4 = pygame.image.load("images/Enemy4/enemy_death/4.png")
enemy4_death4 = pygame.transform.scale(enemy4_death4, (93, 180))
enemy4_death5 = pygame.image.load("images/Enemy4/enemy_death/5.png")
enemy4_death5 = pygame.transform.scale(enemy4_death5, (108, 180))

def makeEnemy4(x, y, damage, potions):
    entity = engine.Entity()
    entity.x = x
    entity.y = y
    entity.position = engine.Position(entity.x, entity.y, 80, 300)
    entity.rect = pygame.rect.Rect(480, 340, 150, 150)
    entityStandingAnimation = engine.Animation([enemy4_stand0, enemy4_stand1, enemy4_stand2, enemy4_stand3])
    entityAttackAnimation = engine.Animation([enemy4_attack0, enemy4_attack1, enemy4_attack2, enemy4_attack3])
    entityShootAnimation = engine.Animation([enemy4_shoot0, enemy4_shoot1, enemy4_shoot2, enemy4_shoot3])
    entityWalkingAnimation = engine.Animation([enemy4_walking1, enemy4_walking2, enemy4_walking3])
    entityDeathAnimation = engine.deathAnimation([enemy4_death0, enemy4_death1, enemy4_death2, enemy4_death3, enemy4_death4, enemy4_death5])
    entity.animations.add('standing', entityStandingAnimation)
    entity.animations.add("attack", entityAttackAnimation)
    entity.animations.add("shoot", entityShootAnimation)
    entity.animations.add("walking", entityWalkingAnimation)
    entity.animations.add("death", entityDeathAnimation)
    entity.damage = damage
    entity.potions = potions
    entity.type = 'enemy'
    entity.type1 = 'enemy1'
    entity.name = "Enemy4"
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

def draw_coinText(window, text, x, y):
    font = pygame.font.SysFont('franklingothicmedium', 25)
    text = font.render(text, True, WHITE)
    text_rectangle = text.get_rect()
    text_rectangle.topleft = (x, y)
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
    gui_font = pygame.font.SysFont('franklingothicmedium', 24)
    text = text
    name_surface = gui_font.render(text, False, color)
    window.blit(name_surface, (x, y))

gui_font = pygame.font.SysFont('franklingothicmedium', 24)
font0 = pygame.font.SysFont('franklingothicmedium', 20)
font = pygame.font.SysFont('franklingothicmedium', 15)
font1 = pygame.font.SysFont('franklingothicmedium', 10)

second_surface = pygame.Surface([720, 400])
second_surface.fill((BLACK))
door_text = "press 1 to go to hall"
text0 = "press E to talk"
text1 = "Hello, I am Spiculus. They brought you here last night. I don't know "
text2 = "what crime you committed, but you got into the gladiatorial arena."
text3 = "You have to defeat five chosen gladiators and then you will be free."


dialogue_surface0 = font.render(text0, False, '#FFFFFF')
door_surface = font.render(door_text, False, '#FFFFFF')
dialogue_surface1 = gui_font.render(text1, False, '#FFFFFF')
dialogue_surface2 = gui_font.render(text2, False, '#FFFFFF')
dialogue_surface3 = gui_font.render(text3, False, '#FFFFFF')

hall_text = "Press B to go back to the Hall"

sword_text = "+ 3 DMG"
sword_surface = font.render(sword_text, False, '#FFFFFF')
sword1_text = "CAN PIERCE"
sword1_surface = font1.render(sword1_text, False, '#FFFFFF')
sword1_text1 = "SHIELD"
sword1_surface1 = font1.render(sword1_text1, False, '#FFFFFF')
shield_text = "SHIELD"
shield_surface = font.render(shield_text, False, '#FFFFFF')
armor_text = "+ 7 HP"
armor_surface = font.render(armor_text, False, '#FFFFFF')
potion_text = "HEALS"
potion_surface = font.render(potion_text, False, '#FFFFFF')
poisonPotion_text = "ANTI-POISON"
poisonPotion_surface = font.render(poisonPotion_text, False, '#FFFFFF')
pcost_text = "COST: 10"
pcost_surface = font.render(pcost_text, False, '#FFFFFF')
acost_text = "COST: 20"
acost_surface = font.render(acost_text, False, '#FFFFFF')
scost_text = "COST: 20"
scost_surface = font.render(scost_text, False, '#FFFFFF')

load_hintText1 = "Hint: before every arena save your progress by clicking on Save the Game button"
load_hintText2 = "so you can load your game through the arena and you do not lose your progress."
load_hintSurface1 = font0.render(load_hintText1, False, '#FFFFFF')
load_hintSurface2 = font0.render(load_hintText2, False, '#FFFFFF')
shop_hintText = "Hint: Press E to buy item"
shop_hintSurface = font0.render(shop_hintText, False, '#FFFFFF')
shield_hintText = "Hint: You cannot damage enemies with shield"
shield_hintSurface = font0.render(shield_hintText, False, '#FFFFFF')
bow_hintText = "Hint: You can avoid the arrows with a shield"
bow_hintSurface = font0.render(bow_hintText, False, '#FFFFFF')
boss_hintText = "Hint: Next enemy is the best gladiator. Good luck."
boss_hintSurface = font0.render(boss_hintText, False, '#FFFFFF')
useShield_hintText = "Hint: You can use shield by holding SPACE"
useShield_hintSurface = font0.render(useShield_hintText, False, '#FFFFFF')
poisonArrow_hintText1 = "Hint: Next enemy is using poison for his arrows so some attacks "
poisonArrow_hintText2 = "can poison you. Poison do damage over time. Avoid it by jumping"
poisonArrow_hintText3 = "or buy anti-poison potion. Your shield might not help you."
poisonArrow_hintSurface1 = font0.render(poisonArrow_hintText1, False, '#FFFFFF')
poisonArrow_hintSurface2 = font0.render(poisonArrow_hintText2, False, '#FFFFFF')
poisonArrow_hintSurface3 = font0.render(poisonArrow_hintText3, False, '#FFFFFF')

arena_bg = pygame.image.load("images/Backgrounds/arena_bg.png")
arena_bg = pygame.transform.scale(arena_bg, (GAME_WIDTH, GAME_HEIGHT))

hit_text = "Hit!"
hit_surface = font.render(hit_text, False, '#FF0000')
miss_text = "Miss!"
miss_surface = font.render(miss_text, False, '#FF0000')

arena_intro_text1 = "Gladiator games culminate today."
arena_intro_text2 = "The last gladiator who survives will receive"
arena_intro_text3 = "a wooden sword, which is a symbol of freedom!"
arena_intro_surface1 = gui_font.render(arena_intro_text1, False, '#FFFFFF')
arena_intro_surface2 = gui_font.render(arena_intro_text2, False, '#FFFFFF')
arena_intro_surface3 = gui_font.render(arena_intro_text3, False, '#FFFFFF')
skip_text = 'Press space to skip'
skip_surface = font0.render(skip_text, False, '#FF0000')

won_text = "You Won! Press 4 to go to the Hall"
won_surface = gui_font.render(won_text, False, '#FFFFFF')
bossWon_text = "You won! Now you are free!(PRESS 4)"
bossWon_surface = gui_font.render(bossWon_text, False, '#FFFFFF')
gameWon_text = "You won and you got your freedom!"
gameWon_surface = gui_font.render(gameWon_text, False, '#FFFFFF')
mainMenu_text = "press ESC to go back to the main menu"
mainMenu_surface = font0.render(mainMenu_text, False, '#FF0000')
lost_text = "You Lost! Press ESC to go to the Main Menu"
lost_surface = gui_font.render(lost_text, False, '#FFFFFF')

load_text = "You can load your game by clicking on load button."
load_surface = gui_font.render(load_text, False, '#FFFFFF')

saved_text = "saved"
saved_surface = font.render(saved_text, False, '#FF0000')