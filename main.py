import sys, pygame

pygame.init()

size = width, height = 800, 600
black = 0, 0, 0
pygame.display.set_caption("Not PhotoMath")

screen = pygame.display.set_mode(size)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()