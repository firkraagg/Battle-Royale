import pygame, sys
from config import *

pygame.init()
pygame.display.set_caption('Battle Royale')

class Prison:
    def __init__(self, game,):
        self.game = game
        self.clock = pygame.time.Clock()
        self.window = window

    def prison_bg(self, background, prison_bg, x, y):
        self.prison_bg = pygame.image.load('images/Prison/prison.png')
        rect = prison_bg.get_rect(topleft=(x, y))
        while rect.y < GAME_HEIGHT:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        self.window.fill(background)
        self.window.blit(prison_bg, rect)
        pygame.display.update()
        self.clock.tick(FPS)








