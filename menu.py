import pygame
from config import *

class Button1:
    def __init__(self, game, text, width, height, pos, elevation):
        self.game = game
<<<<<<< Updated upstream
=======
<<<<<<< HEAD
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
            self.game.draw_text('Press Enter', 10, self.mid_w, self.mid_h + 80)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.start_key:
            if self.state == 'Start':
                self.game.playing = True
            self.run_display = False

=======
>>>>>>> Stashed changes
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.original_y_position = pos[1]

        self.window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
        self.gui_font = pygame.font.SysFont('franklingothicmedium', 20)

        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = '#475F90'

        self.bottom_rect = pygame.Rect(pos, (width, elevation))
        self.bottom_color = '#354B5E'

        self.text_surface = self.gui_font.render(text, False, '#FFFFFF')
        self.text_rect = self.text_surface.get_rect(center=self.top_rect.center)

    def draw(self):
        self.top_rect.y = self.original_y_position -self.dynamic_elevation
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation

        pygame.draw.rect(self.window, self.bottom_color, self.bottom_rect, border_radius=12)
        pygame.draw.rect(self.window, self.top_color, self.top_rect, border_radius = 12)
        self.window.blit(self.text_surface, self.text_rect)
        self.check_click()


    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()


        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = '#D74B4B'
            self.dynamic_elevation = self.elevation
            if click[0]:
                self.dynamic_elevation = 0
                self.pressed = True
        else:
            self.dynamic_elevation = self.elevation
            self.top_color = '#475F90'

class Button2:
    def __init__(self, game, text, width, height, pos, elevation):
        self.game = game
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.original_y_position = pos[1]

        self.window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
        self.gui_font = pygame.font.SysFont('franklingothicmedium', 20)

        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = '#475F90'

        self.bottom_rect = pygame.Rect(pos, (width, elevation))
        self.bottom_color = '#354B5E'

        self.text_surface = self.gui_font.render(text, False, '#FFFFFF')
        self.text_rect = self.text_surface.get_rect(center=self.top_rect.center)

    def draw(self):
        self.top_rect.y = self.original_y_position -self.dynamic_elevation
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation

        pygame.draw.rect(self.window, self.bottom_color, self.bottom_rect, border_radius=12)
        pygame.draw.rect(self.window, self.top_color, self.top_rect, border_radius = 12)
        self.window.blit(self.text_surface, self.text_rect)
        self.check_click()


    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()


        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = '#D74B4B'
            self.dynamic_elevation = self.elevation
            if click[0]:
                self.dynamic_elevation = 0
                self.pressed = True
        else:
            self.dynamic_elevation = self.elevation
<<<<<<< HEAD
<<<<<<< Updated upstream
            self.top_color = '#475F90'
=======
            self.top_color = '#475F90'
>>>>>>> 2
>>>>>>> Stashed changes
=======
            self.top_color = '#475F90'
>>>>>>> parent of b5c6820 (Fixed buttons)
