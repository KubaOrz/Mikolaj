import pygame
import sys

def deathScreen(screen):
    sys.exit()

def menu():
    pass

images = []

def loadImages():
    global images
    for i in range(4):
        images.append(pygame.image.load("assets/gift" + str(i + 1) + ".png"))
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