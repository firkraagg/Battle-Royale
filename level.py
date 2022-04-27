import pygame
import globals
import pickle
import engine
import button
yes = False

window = pygame.display.set_mode((720, 480))
save_image = pygame.image.load("images/save_image.png")
load_image = pygame.image.load("images/load_image.png")
save_button = button.Button1(window, 340, 380, save_image, 60, 50)
load_button = button.Button1(window, 340, 370, load_image, 60, 60)

class Level:
    def __init__(self, platforms=None, entities=None):
        self.platforms = platforms
        self.entities = entities


