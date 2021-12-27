import pygame
import sys
import random

import background as bg
import harness as hrn
import particles as prt

pygame.init()

width = 1280
height = 720
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

bg1 = bg.background(0, 0, width, height, "assets/background.jpg")
bg2 = bg.background(bg1.width, 0, width, height, "assets/background.jpg")
snow1 = bg.background(0, 0, width, height, "assets/snow.png")
snow2 = bg.background(bg1.width, 0, width, height, "assets/snow.png")
bg.Createhouse()

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
                #hrn.falling.append(hrn.harness[0])
                #hrn.harness.pop(0)
                color = random.randint(1, 4)
                hrn.falling.append(hrn.gift(hrn.harness[-1].x + 20, hrn.harness[-1].y + 60, "assets/gift" + str(color) + ".png", color))

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
        if deer == hrn.harness[-1]:
            prt.ContinuousParticles(deer.x, deer.y + 64, (233, random.randint(180, 220), 50), 4, -5, 0, 4, 1, 1)

    snow1.slide(screen)
    snow2.slide(screen)

    for house in bg.houses:
        house.render(screen)
        house.smoke()
        if house.x < -128:
            bg.Createhouse()
            house.ToRemove = True
            bg.HouseCount -= 1
    bg.RemoveHouses()

    for deer in hrn.falling:
        deer.fall(screen, height)

    for deer in hrn.OnGround:
        deer.show(screen)
        deer.SlideOut()
        for house in bg.houses:
            if deer.rect.colliderect(house.rect):
                if deer.color == house.color:
                    if house.Given == False:
                        prt.CreateParticles(30, int(deer.x), int(deer.y), (57, 225, 119))
                    house.Given = True
                else:
                    if house.Given == False:
                        prt.CreateParticles(30, int(deer.x), int(deer.y), (225, 60, 60))
                    house.Given = True

    prt.RenderParticles(screen)

    prt.ticks += 1

    pygame.display.update()
    clock.tick(60)