import pygame
from game import Game

pygame.init()

game = Game()



while game.running:
    game.current_menu.display_menu()
    game.game_loop()
