import pygame
import button
#import map

class Game():
    def __init__(self):
        pygame.init()
        self.running = True
        self.playing = False
        self.UP_KEY, self.DOWN_KEY, self.RIGHT_KEY, self.LEFT_KEY, self.BACK_KEY = False, False, False, False, False
        self.START_KEY = False
        self.widht, self.height = 800, 600
        self.display = pygame.Surface((self.widht, self.height))
        self.window = pygame.display.set_mode(((self.widht, self.height)))
        self.font = pygame.font.SysFont("arialblack", 40)
        self.font_color = (255, 255, 255)
        self.game_icon = pygame.display.set_icon(pygame.image.load("images/game_icon.png"))

    def game_loop(self):
        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing = False
            self.display.fill((0, 0, 0))
            self.window.blit(self.display, (0, 0))
            pygame.display.update()
            self.reset_keys()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.START_KEY = True
                # if event.key == pygame.K_BACKSPACE:
                #     self.BACK_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_LEFT:
                    self.LEFT_KEY = True
                if event.key == pygame.K_RIGHT:
                    self.RIGHT_KEY = True
    
    def reset_keys(self):
        self.START_KEY, self.UP_KEY, self.DOWN_KEY, self.RIGHT_KEY, self.LEFT_KEY, self.BACK_KEY = False, False, False, False, False, False