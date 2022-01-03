import pygame
import sys
import random

import background as bg
import harness as hrn
import particles as prt
import menu as menu

pygame.init()

width = 1280
height = 720
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
lives = 3

bg1 = bg.background(0, 0, width, height, "assets/background.jpg")
bg2 = bg.background(bg1.width, 0, width, height, "assets/background.jpg")
snow1 = bg.background(0, 0, width, height, "assets/snow.png")
snow2 = bg.background(bg1.width, 0, width, height, "assets/snow.png")
bg.Createhouse()
menu.loadImages()
color = random.randint(1, 4)
menu.switchAlpha(color)

# Obiekty początkowe
hrn.InitializeHarness()
good = 0
bad = 0
missed = 0
hrn.snowBalls.append(hrn.SnowBall())
hrn.snowBalls.append(hrn.SnowBall())

# Zmienne pomocnicze
up = False
down = False

running = True

while running:

    if lives == 0 and not hrn.falling:
        running = False
        menu.deathScreen(screen)

    # Input
    for event in pygame.event.get():
        if lives == 0:
            break
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
                hrn.falling.append(hrn.gift(hrn.harness[-1].x + 20, hrn.harness[-1].y + 60, "assets/gift" + str(color) + ".png", color))
            if event.key == pygame.K_1:
                color = 1
                menu.switchAlpha(color)
            if event.key == pygame.K_2:
                color = 2
                menu.switchAlpha(color)
            if event.key == pygame.K_3:
                color = 3
                menu.switchAlpha(color)
            if event.key == pygame.K_4:
                color = 4
                menu.switchAlpha(color)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                up = False
                hrn.harness[0].up = False
                hrn.harness[0].align = True
            if event.key == pygame.K_DOWN:
                down = False
                hrn.harness[0].down = False
                hrn.harness[0].align = True

    if lives == 0:
        up = False
        down = False
        align = False

    # Przesuwanie tła
    bg1.slide(screen)
    bg2.slide(screen)

    menu.gifts(screen)

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
            if not house.Given:
                missed += 1
            bg.Createhouse()
            house.ToRemove = True
            bg.HouseCount -= 1
    bg.RemoveHouses()

    for snowball in hrn.snowBalls:
        snowball.throw(screen)
        for deer in hrn.harness:
            if snowball.rect.colliderect(deer.rect):
                hrn.falling.append(hrn.harness[0])
                hrn.harness.pop(0)
                lives -= 1
                prt.CreateParticles(30, int(deer.x), int(deer.y), (255, 225, 219))
                snowball.remove = True
                if lives == 0:
                    hrn.falling.append(hrn.harness[0])
                    hrn.harness.pop(0)

        if snowball.x < -snowball.size:
            snowball.remove = True

    for snowball in hrn.snowBalls:
        if snowball.remove:
            hrn.snowBalls.remove(snowball)
            hrn.snowBalls.append(hrn.SnowBall())

    for deer in hrn.falling:
        deer.fall(screen, height, lives)

    for deer in hrn.OnGround:
        deer.show(screen)
        deer.SlideOut()
        for house in bg.houses:
            if deer.rect.colliderect(house.rect):
                if deer.color == house.color:
                    if not house.Given:
                        prt.CreateParticles(30, int(deer.x), int(deer.y), (57, 225, 119))
                        good += 1
                    house.Given = True
                else:
                    if not house.Given:
                        prt.CreateParticles(30, int(deer.x), int(deer.y), (225, 60, 60))
                        bad += 1
                    house.Given = True

    prt.RenderParticles(screen)

    prt.ticks += 1

    pygame.display.update()
    clock.tick(60)
