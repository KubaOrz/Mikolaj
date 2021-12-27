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

houses = []
HouseCount = 0
HouseTypes = {1: "Cottage", 2: "Chimney", 3: "brick"}
Colors = {1: "red", 2: "purple", 3: "blue", 4: "yellow"}

class house:
    def __init__(self, x, y):
        global HouseTypes, Colors
        self.x = x
        self.y = y
        self.type = random.randint(1, 3)
        self.img = pygame.image.load("assets/" + HouseTypes[self.type] + ".png")
        self.ToRemove = False
        self.color = random.randint(1, 4)

    def render(self, screen):
        screen.blit(self.img, (self.x, self.y))
        self.x -= 5

    def smoke(self):
        if self.type != 1:
            prt.ContinuousParticles(self.x + 100, self.y, (130, random.randint(110, 140), 130), 20, 0, -1, 1, 1, 2)

def Createhouse():
    global houses, HouseCount
    if HouseCount == 0:
        count = 3
    elif HouseCount < 3:
        count = 2
    else:
        count = 1
    for i in range(count):
        houses.append(house(random.randint(1280, 2560), 500))
        HouseCount += 1

def RemoveHouses():
    global houses
    for house in houses:
        if house.ToRemove:
            houses.remove(house)
