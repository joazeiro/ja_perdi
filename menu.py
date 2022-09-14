import pygame
import button
import game

# NOT READY

class Menu():

    # loading all images for buttons
    resume_game_button_img = pygame.image.load("ja_perdi/images/button_resume.png").convert_alpha()
    video_game_button_img = pygame.image.load("ja_perdi/images/button_video.png").convert_alpha()
    quit_game_button_img = pygame.image.load("ja_perdi/images/button_quit.png").convert_alpha()
    options_game_button_img = pygame.image.load("ja_perdi/images/button_options.png").convert_alpha()
    back_game_button_img = pygame.image.load("ja_perdi/images/button_back.png").convert_alpha()
    audio_game_button_img = pygame.image.load("ja_perdi/images/button_audio.png").convert_alpha()

    # creating the instance of the buttons
    resume_button = button.Button(304, 200, resume_game_button_img, 1)
    quit_button = button.Button(336, 450, quit_game_button_img, 1)
    options_button = button.Button(297, 325, options_game_button_img, 1)
    video_button = button.Button(226, 200, video_game_button_img, 1)
    audio_button = button.Button(225, 300, audio_game_button_img, 1)
    back_button = button.Button(332, 450, back_game_button_img, 1)

    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.width / 2, self.game.height / 2
        self.run_display = True

    def blit_screen(self):
        self.game.screen.blit(self.game.display, (0,0))
        pygame.display.update()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        
    def run_menu(self):
        self.run_display = True

        while self.run_display:
            self.game.screen.fill((168, 50, 245))
