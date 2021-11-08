import pygame
from pygame import image

from config import *
from menu import MainMenu
from animation import Story
from prison import Prison
from prison import Player


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.playing = False
        self.start_key = False
        self.display = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
        self.font_name = pygame.font.get_default_font()
        self.current_menu = MainMenu(self)
        self.animation = Story(self.window)
        self.prison = Prison(self.window)
        self.player = Player(350, 172)




    def game_loop(self):
        while self.playing:
            self.check_events()
            if self.start_key:
                self.playing = True
            pygame.display.update()
            self.clock.tick(FPS)
            self.reset_keys()


    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.current_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.start_key = True

    def reset_keys(self):
        self.start_key = False

    def draw_text(self, text, size, x,y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, WHITE)
        text_rectangle = text_surface.get_rect()
        text_rectangle.center = (x, y)
        self.display.blit(text_surface, text_rectangle)


game = Game()


while game.running:
    game.current_menu.display_menu()
    while game.playing:
        # game.animation.animate_image(BLACK, 'images/Animation/animation.png', 5, 250)
        game.prison.prison_background(BLACK, 'images/Prison/prison.png', 0, 0)
        game.player.update()
        game.player.draw()
        game.game_loop()

