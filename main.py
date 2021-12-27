import pygame
import sys

import background as bg
import harness as hrn

pygame.init()

width = 1280
height = 720
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

bg1 = bg.background(0, 0, width, height, "assets/background.jpg")
bg2 = bg.background(bg1.width, 0, width, height, "assets/background.jpg")
snow1 = bg.background(0, 0, width, height, "assets/snow.png")
snow2 = bg.background(bg1.width, 0, width, height, "assets/snow.png")

#Obiekty początkowe
hrn.InitializeHarness()

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
                if hrn.harness[-1].align:
                    hrn.harness[0].up = True
                    hrn.harness[0].align = False
            if event.key == pygame.K_DOWN:
                down = True
                if hrn.harness[-1].align:
                    hrn.harness[0].down = True
                    hrn.harness[0].align = False
            if event.key == pygame.K_SPACE:
                hrn.falling.append(hrn.harness[0])
                hrn.falling[0].IfFall = True
                hrn.harness.pop(0)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                up = False
                hrn.harness[0].up = False
                hrn.harness[0].align = True
            if event.key == pygame.K_DOWN:
                down = False
                hrn.harness[0].down = False
                hrn.harness[0].align = True

    #Przesuwanie tła
    bg1.slide(screen)
    bg2.slide(screen)

    if bg1.x < -bg1.width:
        bg1.wrap(bg2.x + bg2.width)
        snow1.wrap(bg2.x + bg2.width)
    if bg2.x < -bg2.width:
        bg2.wrap(bg1.x + bg1.width)
        snow2.wrap(bg1.x + bg1.width)

    if up:
        if hrn.harness[-1].align:
            hrn.harness[0].up = True
            hrn.harness[0].align = False
    elif down:
        if hrn.harness[-1].align:
            hrn.harness[0].down = True
            hrn.harness[0].align = False

    for index, deer in enumerate(hrn.harness):
        if index > 0:
            deer.ChangeState(hrn.harness[index - 1].y)
        deer.show(screen)
        deer.move()

    for deer in hrn.falling:
        deer.fall(screen, height)

    for deer in hrn.OnGround:
        deer.fall(screen, height)

    snow1.slide(screen)
    snow2.slide(screen)
    pygame.display.update()
    clock.tick(60)