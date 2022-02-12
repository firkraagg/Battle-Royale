import pygame

class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        self.volume = 0.5
        self.sounds = {
            "coins" : pygame.mixer.Sound("sounds/coin_pickup.ogg"),
            "buying" : pygame.mixer.Sound("sounds/buying.ogg"),
            "room_doors" : pygame.mixer.Sound("sounds/room_doors.wav"),
            "arena_doors": pygame.mixer.Sound("sounds/arena_doors.wav"),
            "player_sword":pygame.mixer.Sound("sounds/player_sword.mp3"),
            "smash": pygame.mixer.Sound("sounds/smash.mp3"),
            "elixir": pygame.mixer.Sound("sounds/elixir.wav"),
            "elixir_drink": pygame.mixer.Sound("sounds/elixir_drink.mp3"),
            "player_pain": pygame.mixer.Sound("sounds/player_pain.mp3"),
            "enemy_pain": pygame.mixer.Sound("sounds/enemy_pain.mp3"),
            "arrow_shot": pygame.mixer.Sound("sounds/arrow_shot.mp3"),
            "shield_block": pygame.mixer.Sound("sounds/shield_block.mp3"),
            "poison": pygame.mixer.Sound("sounds/poison.mp3")
        }
        self.music = {

        }
    def playSound(self, soundName):
        self.sounds[soundName].set_volume(self.volume)
        self.sounds[soundName].play()
    def playMusic(self):
        pass