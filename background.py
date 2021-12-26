import pygame

class background:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.img = pygame.image.load("assets/background.jpg")

    def slide(self, screen):
        self.x -= 5
        screen.blit(self.img, (self.x, self.y))

    def wrap(self, x):
        self.x = x
