import pygame

class Player():
    def __init__(self, x, y):
        my_player = pygame.image.load('ja_perdi/sprites/playerzin.png')
        self.image = pygame.transform.scale(my_player, (40, 80))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_y = 0
        #self.jumped = False

    def update(self):
        dx = 0
        dy = 0

        # player's movement
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            dx -= 5
        if key[pygame.K_RIGHT]:
            dx += 5
        if key[pygame.K_DOWN]:
            dy -= 5
        if key[pygame.K_UP]:
            dy += 5

        # check for collision --> still to be done

        # update player coordinates
        self.rect.x += dx
        self.rect.y += dy
        width = 800
        height = 600
        screen = pygame.display.set_mode((width, height))

        if self.rect.bottom > height:
            self.rect.bottom = width
            dy = 0

        screen.blit(self.image, self.rect)