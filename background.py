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
        self.rect = self.img.get_rect()
        self.WantedGift = pygame.image.load("assets/gift" + str(self.color) + ".png")
        self.alpha = 0
        self.FadeOut = False
        self.Given = False

    def render(self, screen):
        screen.blit(self.img, (self.x, self.y))
        self.WantedGift.set_alpha(self.alpha)
        screen.blit(self.WantedGift, (self.x + 50, self.y - 50))
        if self.FadeOut == False:
            self.alpha += 5
            if self.alpha >= 255:
                self.FadeOut = True
        else:
            self.alpha -= 5
            if self.alpha <= 0:
                self.FadeOut = False
        self.x -= 5
        self.rect.update(self.x, self.y, 128, 128)

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
