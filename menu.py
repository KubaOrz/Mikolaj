import pygame
import sys

def deathScreen(screen):
    font = pygame.font.SysFont('Comic Sans MS', 30)
    death = font.render("Koniec gry!", False, (200, 200, 200))
    deathbg = pygame.image.load("assets/menuTree.jpg").convert()
    deathbg = pygame.transform.scale(deathbg, (300, 720))
    button1Img = pygame.image.load("assets/christmas-ornament.png").convert_alpha()
    button2Img = pygame.image.load("assets/christmas-ornament.png").convert_alpha()
    button3Img = pygame.image.load("assets/christmas-ornament.png").convert_alpha()
    deathbg.set_alpha(230)
    bSize = 64
    button1 = pygame.rect.Rect(100, 300, bSize, bSize)
    button2 = pygame.rect.Rect(150, 450, bSize, bSize)
    button3 = pygame.rect.Rect(70, 550, bSize, bSize)
    while True:
        screen.blit(deathbg, (0, 0))
        left, scroll, right = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()
        screen.blit(death, (100, 100))
        screen.blit(button1Img, button1)
        screen.blit(button2Img, button2)
        screen.blit(button3Img, button3)
        if button1.collidepoint(pos):
            print("Kliknięto przycisk 1")
            button1.update(90, 290, bSize + 20, bSize + 20)
            button1Img = pygame.transform.scale(button1Img, (bSize * 2, bSize * 2))
            if left:
                print("Kliknięto przycisk 1")
                sys.exit()
        elif button2.collidepoint(pos):
            print("Kliknięto przycisk 2")
            button2.update(140, 440, bSize + 20, bSize + 20)
            button2Img = pygame.transform.scale(button2Img, (bSize * 2, bSize * 2))
            if left:
                print("Kliknięto przycisk 2")
        elif button3.collidepoint(pos):
            print("Kliknięto przycisk 3")
            button3.update(60, 540, bSize + 20, bSize + 20)
            button3Img = pygame.transform.scale(button3Img, (bSize * 2, bSize * 2))
            if left:
                print("Klikięto przycisk 3")
        else:
            button1.update(100, 300, bSize, bSize)
            button1Img = pygame.transform.scale(button1Img, (bSize, bSize))
            button2.update(150, 450, bSize, bSize)
            button2Img = pygame.transform.scale(button2Img, (bSize, bSize))
            button3.update(70, 550, bSize, bSize)
            button3Img = pygame.transform.scale(button3Img, (bSize, bSize))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.update()

def menu():
    pass

images = []

def loadImages():
    global images
    for i in range(4):
        images.append(pygame.image.load("assets/gift" + str(i + 1) + ".png").convert_alpha())
        images[i] = pygame.transform.scale(images[i], (50, 50))

def switchAlpha(color):
    global images
    for image in images:
        image.set_alpha(70)
    images[color - 1].set_alpha(255)

def gifts(screen):
    global images
    x = 50
    for image in images:
        screen.blit(image, (x, 50))
        x += 70