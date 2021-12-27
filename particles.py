import pygame
import random

particles = []
ticks = 0

class particle():
    def __init__(self, x, y, duration, color, vx, vy, rangeX, rangeY, slowdown):
        self.x = x
        self.y = y
        self.duration = duration
        self.color = color
        self.vx = random.randint(vx - rangeX, vx + rangeX)
        self.vy = random.randint(vy - rangeY, vy + rangeY)
        self.slowdown = slowdown

def CreateParticles(amount, x, y, color):
    for i in range(amount):
        particles.append(particle(random.randint(x - 30, x + 30), random.randint(y, y + 40), random.randint(20, 40), color, 0, -3, 6, 3, 1))

def RenderParticles(screen):
    global particles
    for particle in particles:
        pygame.draw.circle(screen, particle.color, (particle.x, particle.y), particle.duration / 2)
        particle.duration -= 1 / particle.slowdown
        particle.x += particle.vx - 5
        particle.y += particle.vy
        particle.vy += 0.05
        if particle.duration <= 0:
            particles.remove(particle)

def ContinuousParticles(x ,y, color, size, vx, vy, rangeX, rangeY, slowdown):
    global particles, ticks
    if ticks % slowdown == 0:
        particles.append(particle(x, y, random.randint(size - 10, size + 10), color, vx, vy, rangeX, rangeY, slowdown))