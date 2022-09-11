import sys, pygame
import button, map, player

pygame.init()

# generating screen and text
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Not PhotoMath")
clock = pygame.time.Clock()

font = pygame.font.SysFont("arialblack", 40)
font_color = (255, 255, 255)

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

# tiles
tile_size = 200

# game variables
# in_menu always starts at true since the game has to be initialized on the menu
in_menu = True
menu_state = "main"

# function used to print text (might not need it)
def text(text, font, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x,y))

def make_grid():
    for line in range(6):
        pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (width, line * tile_size))
        pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, height))

def generate_equation():
    pass

# loop that makes the game run until the user exits
while(1):
    #screen.fill((52, 78, 91))

    if in_menu == True:
        screen.fill((168, 50, 245))
        if menu_state == "main":
            if resume_button.draw(screen):
                in_menu = False
            if quit_button.draw(screen):
                sys.exit()
            if options_button.draw(screen):
                menu_state = "options"
        if menu_state == "options":
            if video_button.draw(screen):
                pass
            if audio_button.draw(screen):
                pass
            if back_button.draw(screen):
                menu_state = "main"
    
    #if in menu is not true, then we are at the game
            

    #if resume is clicked, game is not paused anymore
    #call play function
    #if esc is clicked while play is happening, game_paused becomes true again
    #and we come back to menu

    make_grid()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()


    pygame.display.update()
    clock.tick(60)

