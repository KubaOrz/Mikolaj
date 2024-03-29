import pygame
import random
import particles as prt

harness = []
falling = []
OnGround = []
gifts = []
snowBalls = []

class FlyingObject:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.VertSpeed = 0
        self.img = pygame.image.load(img).convert_alpha()
        self.angle = 0
        self.up = False
        self.down = False
        self.align = True
        self.rect = self.img.get_rect()

    def show(self, screen):
        screen.blit(pygame.transform.rotate(self.img, self.angle), (self.x, self.y))
        self.rect.update(self.x, self.y, self.img.get_width(), self.img.get_height())

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
        self.color = 6

    def fall(self, screen, height, lives):
        global falling, harness, OnGround
        self.angle += 5
        self.y += self.VertSpeed
        self.VertSpeed += 0.3
        self.imgCopy = pygame.transform.rotate(self.img, self.angle)
        screen.blit(self.imgCopy, (self.x - int(self.imgCopy.get_width() / 2), self.y - int(self.imgCopy.get_height() / 2)))
        if self.y > height - 100:
            OnGround.append(falling[0])
            falling.pop(0)
            prt.CreateParticles(int(self.VertSpeed) * 5, int(self.x), int(self.y), (230, 230, 230))
            self.VertSpeed = 0
            if lives > 0:
                harness[0].up = False
                harness[0].down = False
                harness[0].align = True

    def SlideOut(self):
        global OnGround
        self.x -= 5
        self.rect.update(self.x, self.y, self.img.get_width(), self.img.get_height())
        if self.x < -64:
            OnGround.pop(0)

class gift(deer):
    def __init__(self, x, y, img, color):
        super().__init__(x, y, img)
        self.color = color
        self.img = pygame.transform.scale(self.img, (32, 32))

class SnowBall():
    def __init__(self):
        self.x = random.randint(1300, 3000)
        self.y = random.randint(50, 650)
        self.speed = random.randint(8, 20)
        self.size = random.randint(10, 20)
        self.rect = pygame.rect.Rect(self.x - self.size, self.y - self.size, 2 * self.size, 2 * self.size)
        self.remove = False

    def throw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), self.size)
        self.rect.update(self.x - self.size, self.y - self.size, 2 * self.size, 2 * self.size)
        self.x -= self.speed

def InitializeHarness():
    global harness
    x = 400
    y = 200
    for i in range(3):
        harness.append(deer(x, y, "assets/deer.png"))
        x -= 80
    harness.append(deer(x, y, 'assets/sleigh.png'))