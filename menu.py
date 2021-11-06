import pygame
from config import *


class Menu:
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = GAME_WIDTH / 2, GAME_HEIGHT / 2
        self.run_display = True
        self.cursor_rectangle = pygame.Rect(0, 0, 20, 20)
        self.offset = - 100

    def draw_cursor(self):
        self.game.draw_text('*', 15, self.cursor_rectangle.x, self.cursor_rectangle.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()


class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h + 30
        self.cursor_rectangle.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(BLACK)
            self.game.draw_text('Main Menu', 20, self.mid_w, self.mid_h - 20)
            self.game.draw_text("Start Game", 20, self.startx, self.starty)
            self.game.draw_text('Press ENTER', 10, self.mid_w, self.mid_h + 80)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.start_key:
            if self.state == 'Start':
                self.game.playing = True
            self.run_display = False

