import pygame
from pygame import image

from config import *
from menu import MainMenu
from animation import Story
from prison import Prison
from prison import Player
from prison import Npc

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
        pygame.display.set_caption('Battle Royale')
        self.clock = pygame.time.Clock()
        self.running = True
        self.playing = False
        self.start_key = False
        self.display = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
        self.font_name = pygame.font.get_default_font()
        self.current_menu = MainMenu(self)
        self.animation = Story(self.window)
        self.prison = Prison(self, self.window)
        self.player = Player(550, 298)
        self.npc = Npc(self, 'images/Npc/0.png', 250, 290)




    # def new(self):
    #     self.player_group = pygame.sprite.LayeredUpdates()
    #     self.player = Player(self, 350, 172)
    #     self.npc_group = pygame.sprite.LayeredUpdates()
    #     self.npc = Npc(self, 160, 168)

    def game_loop(self):
        self.check_events()
        if self.start_key:
            self.playing = True
        # self.player_group.update()
        # self.player_group.draw(self.window)
        # self.npc_group.update()
        # self.npc_group.draw(self.window)
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

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, WHITE)
        text_rectangle = text_surface.get_rect()
        text_rectangle.center = (x, y)
        self.display.blit(text_surface, text_rectangle)

game = Game()
moving_sprites = pygame.sprite.Group()
player = Player(300, 300)
moving_sprites.add(player)
window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
prison_background = pygame.image.load('images/Prison/prison.png')
        # image = pygame.transform.scale(image, (720, 480))



while game.running:
    game.current_menu.display_menu()
    # game.animation.animate_image(BLACK, 'images/Animation/animation.png', 100, 400)
    game.prison.prison_background(BLACK, 'images/Prison/prison.png', 0, 0)
    while game.playing:
        moving_sprites.draw(window)
        moving_sprites.update()
        # game.player.update()
        # game.player.draw()
        game.npc.draw(image)
        game.game_loop()

