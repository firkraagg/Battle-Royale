import pygame
import globals
import pickle
import utilities

class Level:
    def __init__(self, platforms=None, entities=None):
        self.platforms = platforms
        self.entities = entities

def save(entity):
    if entity.type == "player":
        with open("save_game.pkl", "wb") as save_game:
            pickle.dump(entity.position, save_game, protocol=pickle.HIGHEST_PROTOCOL)
            pickle.dump(entity.score, save_game, protocol=pickle.HIGHEST_PROTOCOL)
            pickle.dump(entity.maxHealth, save_game, protocol=pickle.HIGHEST_PROTOCOL)
            pickle.dump(entity.health, save_game, protocol=pickle.HIGHEST_PROTOCOL)
            pickle.dump(entity.damage, save_game, protocol=pickle.HIGHEST_PROTOCOL)
            pickle.dump(entity.swordLvl, save_game, protocol=pickle.HIGHEST_PROTOCOL)
            pickle.dump(entity.shieldLvl, save_game, protocol=pickle.HIGHEST_PROTOCOL)
            pickle.dump(entity.potions, save_game, protocol=pickle.HIGHEST_PROTOCOL)
            pickle.dump(entity.poisonPotions, save_game, protocol=pickle.HIGHEST_PROTOCOL)

def load(entity):
    if entity.type == "player":
        with open("save_game.pkl", "rb") as load_game:
            entity.position = pickle.load(load_game)
            entity.score = pickle.load(load_game)
            entity.maxHealth = pickle.load(load_game)
            entity.health = pickle.load(load_game)
            entity.damage = pickle.load(load_game)
            entity.swordLvl = pickle.load(load_game)
            entity.shieldLvl = pickle.load(load_game)
            entity.potions = pickle.load(load_game)
            entity.poisonPotions = pickle.load(load_game)
