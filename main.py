import pygame
import sys

import background as bg

pygame.init()

width = 1280
height = 720
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

bg1 = bg.background(0, 0)
bg2 = bg.background(bg1.img.get_width(), 0)

class FlyingObject:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.VertSpeed = 0
        self.img = pygame.image.load(img)
        self.angle = 0
        self.up = False
        self.down = False
        self.align = True

    def show(self):
        screen.blit(pygame.transform.rotate(self.img, self.angle), (self.x, self.y))

    def ChangeState(self, prevY):
        if prevY + 30 < self.y:
            self.up = True
            self.align = False
        elif prevY - 30 > self.y:
            self.down = True
            self.align = False
        elif prevY == self.y:
            self.down = False
            self.up = False
            self.align = True

    def move(self):
        if self.up:
            if self.angle < 45:
                self.angle += 2.5
            self.y -= 7
        elif self.down:
            if self.angle > -45:
                self.angle -= 2.5
            self.y += 7
        elif self.align:
            if self.angle > 0:
                self.angle -= 2.5
            elif self.angle < 0:
                self.angle += 2.5

class deer(FlyingObject):
    def __init__(self, x, y, img):
        super().__init__(x, y, img)
        self.imgCopy = self.img

    def fall(self):
        global falling, height, harness
        self.angle += 5
        self.y += self.VertSpeed
        self.VertSpeed += 0.3
        self.imgCopy = pygame.transform.rotate(self.img, self.angle)
        screen.blit(self.imgCopy, (self.x - int(self.imgCopy.get_width() / 2), self.y - int(self.imgCopy.get_height() / 2)))
        if self.y > height:
            falling.pop(0)
            self.VertSpeed = 0
            harness[0].up = False
            harness[0].down = False
            harness[0].align = True

#Obiekty początkowe
harness = []
falling = []

def InitializeHarness():
    global harness
    x = 400
    y = 200
    for i in range(3):
        harness.append(deer(x, y, "assets/deer.png"))
        x -= 80
    harness.append(FlyingObject(x, y, 'assets/sleigh.png'))

InitializeHarness()

#Zmienne pomocnicze
up = False
down = False

running = True

while running:
    #Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                up = True
                if harness[-1].align:
                    harness[0].up = True
                    harness[0].align = False
            if event.key == pygame.K_DOWN:
                down = True
                if harness[-1].align:
                    harness[0].down = True
                    harness[0].align = False
            if event.key == pygame.K_SPACE:
                falling.append(harness[0])
                harness.pop(0)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                up = False
                harness[0].up = False
                harness[0].align = True
            if event.key == pygame.K_DOWN:
                down = False
                harness[0].down = False
                harness[0].align = True

    bg1.slide(screen)
    bg2.slide(screen)

    if bg1.x < -bg1.img.get_width():
        bg2.wrap(bg1.x + bg1.img.get_width())

    if bg2.x < -bg2.img.get_width():
        bg1.wrap(bg1.x + bg2.img.get_width())

    if up:
        if harness[-1].align:
            harness[0].up = True
            harness[0].align = False
    elif down:
        if harness[-1].align:
            harness[0].down = True
            harness[0].align = False

    for index, deer in enumerate(harness):
        if index > 0:
            deer.ChangeState(harness[index - 1].y)
        deer.show()
        deer.move()

    for deer in falling:
        deer.fall()

    pygame.display.update()
    clock.tick(60)