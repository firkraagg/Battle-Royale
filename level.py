import pygame
import engine
import utilities
from config import *

class Level1:
    def __init__(self, platforms = None, entities = None):
        window = pygame.display.set_mode((720, 480))
        p_background = pygame.image.load('images/Prison/prison.png')
        p_background = pygame.transform.scale(p_background, (GAME_WIDTH, GAME_HEIGHT))
        window.blit(p_background, (0, 0))
        self.platforms = platforms
        self.entities = entities



        def draw_text(text, x, y):
            text = font1.render(text, True, WHITE)
            text_rectangle = text.get_rect()
            text_rectangle.topleft = (x, y)
            window.blit(text, text_rectangle)

        pygame.init()
        window = pygame.display.set_mode((720, 480))
        pygame.display.set_caption('Battle Royale')
        clock = pygame.time.Clock()
        font1 = pygame.font.SysFont('franklingothicmedium', 25)

        game_state = 'playing'

        second_surface = pygame.Surface([720, 400])
        second_surface.fill((BLACK))
        text00 = "Spiculus"
        text0 = "press E to talk"
        text000 = "Press P to enter next room"
        text1 = "Hello, I am Spiculus. They brought you here last night. I don't know "
        text2 = "what crime you committed, but you got into the gladiatorial arena."
        text3 = "You have to defeat three chosen gladiators and then you will be free. "

        gui_font = pygame.font.SysFont('franklingothicmedium', 24)
        font = pygame.font.SysFont('franklingothicmedium', 15)

        name_surface0 = gui_font.render(text00, False, '#FFFFFF')
        dialogue_surface0 = font.render(text0, False, '#FFFFFF')
        dialogue_surface1 = gui_font.render(text1, False, '#FFFFFF')
        dialogue_surface2 = gui_font.render(text2, False, '#FFFFFF')
        dialogue_surface3 = gui_font.render(text3, False, '#FFFFFF')

        # door_surface = pygame.Surface([50, 50])
        # door_surface.fill(BLACK)
        dialogue_surface00 = font.render(text000, False, '#FFFFFF')
        #
        # door = pygame.Surface((100, 50))
        # door_rect = pygame.rect.Rect(620, 315)


        entities = []

        player_x = 530
        player_y = 261
        player_width = 60
        player_height = 60

        player_direction = 'left'
        player_state = 'standing'

        player_stand0 = pygame.image.load('images/Player/player_standing/img0.png')
        player_stand0 = pygame.transform.scale(player_stand0, (102, 102))
        player_stand1 = pygame.image.load('images/Player/player_standing/img1.png')
        player_stand1 = pygame.transform.scale(player_stand1, (102, 102))
        player_stand2 = pygame.image.load('images/Player/player_standing/img2.png')
        player_stand2 = pygame.transform.scale(player_stand2, (102, 102))
        player_stand3 = pygame.image.load('images/Player/player_standing/img3.png')
        player_stand3 = pygame.transform.scale(player_stand3, (102, 102))
        player_stand4 = pygame.image.load('images/Player/player_standing/img2.png')
        player_stand4 = pygame.transform.scale(player_stand2, (102, 102))
        player_stand5 = pygame.image.load('images/Player/player_standing/img5.png')
        player_stand5 = pygame.transform.scale(player_stand5, (102, 102))

        player_walk0 = pygame.image.load('images/Player/player_walking/p00.png')
        player_walk0 = pygame.transform.scale(player_walk0, (102, 102))
        player_walk1 = pygame.image.load('images/Player/player_walking/p01.png')
        player_walk1 = pygame.transform.scale(player_walk1, (102, 102))
        player_walk2 = pygame.image.load('images/Player/player_walking/p02.png')
        player_walk2 = pygame.transform.scale(player_walk2, (102, 102))
        player_walk3 = pygame.image.load('images/Player/player_walking/p03.png')
        player_walk3 = pygame.transform.scale(player_walk3, (102, 102))
        player_walk4 = pygame.image.load('images/Player/player_walking/p04.png')
        player_walk4 = pygame.transform.scale(player_walk4, (102, 102))
        player_animations = \
            {'standing' : engine.Animation([
                player_stand1,
                player_stand2,
                player_stand3,
                player_stand4,
                player_stand5
            ]),
            'walking' : engine.Animation([
                player_walk0,
                player_walk1,
                player_walk2,
                player_walk3,
                player_walk4

            ])
        }

        platforms = [

            pygame.Rect(52, 350, 610, 5),

            pygame.Rect(25, 405, 5, 50),

            pygame.Rect(656, 405, 5, 50)
        ]

        p_background = pygame.image.load('images/Prison/prison.png')
        p_background = pygame.transform.scale(p_background, (GAME_WIDTH, GAME_HEIGHT))

        npc1_image = pygame.image.load('images/Npc/npc0.png')
        npc1_image = pygame.transform.scale(npc1_image, (135, 135))
        npcs = [
            pygame.Rect(200, 250, 50, 60)
        ]

        npc_image1 = pygame.image.load('images/Npc/npc0.png')
        npc_image1 = pygame.transform.scale(npc_image1, (135, 135))
        npc_image2 = pygame.image.load('images/Npc/npc1.png')
        npc_image2 = pygame.transform.scale(npc_image2, (135, 135))
        npc_image3 = pygame.image.load('images/Npc/npc2.png')
        npc_image3 = pygame.transform.scale(npc_image3, (135, 135))
        npc_image4 = pygame.image.load('images/Npc/npc3.png')
        npc_image4 = pygame.transform.scale(npc_image4, (135, 135))
        npc_image5 = pygame.image.load('images/Npc/npc4.png')
        npc_image5 = pygame.transform.scale(npc_image5, (135, 135))

        npc_animation = engine.Animation([
            npc_image1,
            npc_image2,
            npc_image3,
            npc_image4,
            npc_image5
        ])

        coin_image = pygame.image.load('images/Coins/coin.png')

        coin1 = engine.Entity()
        coin1.position = engine.Position(90, 342, 18, 20)
        coin1Animation = engine.Animation([
            pygame.image.load('images/Coins/coin.png')
        ])
        coin1.animations = engine.Animations()
        coin1.animations.add('standing', coin1Animation)
        coin1.type = 'collectable'

        entities.append(utilities.makeCoin(90, 342))
        entities.append(utilities.makeNpc(150, 226))
        player = utilities.makePlayer(530, 261)

        coin_number = 0
        coin_count_image = pygame.image.load('images/Coins/coin.png')
        coin_count_image = pygame.transform.scale(coin_count_image, (25, 30))

        running = True
        while running:


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            new_player_x = player_x

            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                new_player_x -= 2
                player_direction = 'left'
                player_state = 'walking'
            if keys[pygame.K_d]:
                new_player_x += 2
                player_direction = 'right'
                player_state = 'walking'
            if not keys[pygame.K_a] and not keys[pygame.K_d]:
                player_state = 'standing'


            if game_state == 'playing':

                player_animations[player_state].update()
                npc_animation.update()

                for entity in entities:
                    entity.animations.animationList[entity.state].update()

                new_player_rect = pygame.Rect(new_player_x, 400, 72, 72)
                x_collision = False

                for platform in platforms:
                    if platform.colliderect(new_player_rect):
                        x_collision = True
                        break

                if x_collision == False:
                    player_x = new_player_x

                player_rect = pygame.Rect(player_x, 300, player_width, player_height)
                for entity in entities:
                    if entity.type == 'collectable':
                        if entity.position.rect.colliderect(player_rect):
                            entities.remove(entity)
                            coin_number += 15

                for entity in entities:
                    if entity.type == 'friendly':
                        if entity.position.rect.colliderect(player_rect):
                            window.blit(dialogue_surface0, (175, 240))
                                  # if event.type == pygame.KEYUP and event.key == pygame.K_e:
                            if event.type == pygame.KEYUP:
                                if event.key == pygame.K_e:
                                    window.blit(second_surface, (0, 370)),
                                    window.blit(dialogue_surface1, (0, 380)),
                                    window.blit(dialogue_surface2, (0, 410)),
                                    window.blit(dialogue_surface3, (0, 440))

                window.blit(p_background, (0, 0))

                for npc1 in npcs:
                    if npc1.colliderect(player_rect):
                        window.blit(dialogue_surface0, (175, 240))
                        # if event.type == pygame.KEYUP and event.key == pygame.K_e:
                        if event.type == pygame.KEYUP:
                            if event.key == pygame.K_e:
                                window.blit(second_surface, (0, 370)),
                                window.blit(dialogue_surface1, (0, 380)),
                                window.blit(dialogue_surface2, (0, 410)),
                                window.blit(dialogue_surface3, (0, 440))

                # for c in coins:
                #     window.blit(coin_image, (c[0], c[1]))
                #     coin_animation.draw(window, c.x, c.y, False, False)
                for entity in entities:
                    s = entity.state
                    a = entity.animations.animationList[s]
                    a.draw(window, entity.position.rect.x, entity.position.rect.y, False, False)

                # for npc1 in npcs:
                #     # window.blit(npc1_image, (160, 226))
                #     npc_animation.draw(window, 160, 226, False, False)

                if player_direction == 'right':
                    # window.blit(pygame.transform.flip(player_image, True, False), (player_x, player_y))
                    player_animations[player_state].draw(window, player_x, player_y, True, False)
                elif player_direction == 'left':
                    # window.blit(player_image, (player_x, player_y))
                    player_animations[player_state].draw(window, player_x, player_y, False, False)

                door = pygame.Rect(620, 245, 40, 120)

                if door.colliderect(player_rect):
                    window.blit(dialogue_surface00, (480, 230))


                window.blit(name_surface0, (180, 215))
                # pygame.draw.rect(window, BLACK, door)
                window.blit(coin_count_image, (50, 50))
                draw_text(str(coin_number), 80, 52)
                pygame.display.flip()
                clock.tick(60)

        pygame.quit()