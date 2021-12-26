import pygame
#KOmentarz do testów ;)
pygame.init()

width = 1280
height = 720
screen = pygame.display.set_mode((width, height))

class FlyingObject:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.VertSpeed = 0
        self.img = pygame.image.load(img)

    def show(self):
        screen.blit(self.img, (self.x, self.y))

    def move(self):
        if self.VertSpeed > 0:
            self.img = pygame.transform.rotate(self.img, 45)
        else:
            self.img = pygame.transform.rotate(self.img, 315)

class deer(FlyingObject):
    def wave(self):
        pass



#Obiekty początkowe
deer = deer(200, 300, "assets/deer.png")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("Up")
                deer.VertSpeed = -10
            if event.key == pygame.K_DOWN:
                print("Down")
                deer.VertSpeed = 10

    screen.fill((0, 0, 0))
    deer.show()
    deer.move()
    pygame.display.update()