import pygame

class background:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.img = pygame.image.load("assets/background.jpg")
        self.img = pygame.transform.scale(self.img, (width, height))

    def slide(self, screen):
        self.x -= 5
        screen.blit(self.img, (self.x, self.y))

    def wrap(self, x):
        self.x = x
