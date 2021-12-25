import pygame
import engine
import utilities
from config import *

class Level:
    def __init__(self, platforms = None, entities = None, doors = None):
        # window = pygame.display.set_mode((720, 480))
        # p_background = pygame.image.load('images/Prison/prison.png')
        # p_background = pygame.transform.scale(p_background, (GAME_WIDTH, GAME_HEIGHT))
        # window.blit(p_background, (0, 0))
        self.platforms = platforms
        self.entities = entities
        self.doors = doors