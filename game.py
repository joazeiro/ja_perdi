import pygame

class Game():
    def __init__(self):
        pygame.init()
        self.running = True
        self.playing = False
        self.UP_KEY, self.DOWN_KEY, self.RIGHT_KEY, self.LEFT_KEY, self.ESCAPE_KEY = False, False, False, False, False
        self.widht, self.height = 800, 600
        self.display = pygame.Surface((self.widht, self.height))
        self.window = pygame.display.set_mode(((self.widht, self.height)))
        self.font = pygame.font.SysFont("arialblack", 40)
        self.font_color = (255, 255, 255)
        self.game_icon = pygame.display.set_icon(pygame.image.load("ja_perdi/images/game_icon.png"))