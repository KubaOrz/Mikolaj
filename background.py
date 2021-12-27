import pygame
import random
import particles as prt

#wszystko co związane z tłem
class background:
    def __init__(self, x, y, width, height, img):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.img, (width, height))

    def slide(self, screen):
        self.x -= 5
        screen.blit(self.img, (self.x, self.y))

    def wrap(self, x):
        self.x = x

#Domki

class house:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = random.randint(1, 1)
        self.HouseTypes = {1: "Cottage", 2: "Chimney", 3: "brick"}
        self.img = pygame.image.load("assets/" + self.HouseTypes[self.type] + ".png")

    def render(self, screen):
        screen.blit(self.img, (self.x, self.y))