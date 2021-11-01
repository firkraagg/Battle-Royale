import pygame
from menu import MainMenu




class Game():
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        self.START_KEY = False
        self.display_W, self.display_H = 480, 270
        self.display = pygame.Surface((self.display_W, self.display_H))
        self.window = pygame.display.set_mode(((self.display_W, self.display_H)))
        self.font_name = pygame.font.get_default_font()
        self.Black, self.White = (0, 0, 0), (255, 255, 255)
        self.current_menu = MainMenu(self)



    def game_loop(self):
        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing = False
            self.display.fill(self.Black)

            self.window.blit(self.display, (0, 0))
            pygame.display.update()
            self.reset_keys()


    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.current_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True

    def reset_keys(self):
        self.START_KEY = False

    def draw_text(self, text, size, x,y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.White)
        text_rectangle = text_surface.get_rect()
        text_rectangle.center = (x, y)
        self.display.blit(text_surface, text_rectangle)
