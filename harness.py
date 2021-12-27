import pygame

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
        self.IfFall = False

    def show(self, screen):
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

    def fall(self, screen, height):
        global falling, harness, OnGround
        if self.IfFall:
            self.angle += 5
            self.y += self.VertSpeed
            self.VertSpeed += 0.3
        self.imgCopy = pygame.transform.rotate(self.img, self.angle)
        screen.blit(self.imgCopy, (self.x - int(self.imgCopy.get_width() / 2), self.y - int(self.imgCopy.get_height() / 2)))
        if self.y > height - 150:
            self.x -= 5
            if self.IfFall:
                OnGround.append(falling[0])
                falling.pop(0)
                self.VertSpeed = 0
                harness[0].up = False
                harness[0].down = False
                harness[0].align = True
                self.IfFall = False
        if self.x < 0:
            OnGround.pop(0)

harness = []
falling = []
OnGround = []

def InitializeHarness():
    global harness
    x = 400
    y = 200
    for i in range(3):
        harness.append(deer(x, y, "assets/deer.png"))
        x -= 80
    harness.append(FlyingObject(x, y, 'assets/sleigh.png'))