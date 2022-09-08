import sys, pygame
import button

pygame.init()

width = 800
height = 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Not PhotoMath")

font = pygame.font.SysFont("arialblack", 40)
font_color = (255, 255, 255)

def text(text, font, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x,y))

while 1:
    
    screen.fill((52, 78, 91))

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()


    pygame.display.update()

