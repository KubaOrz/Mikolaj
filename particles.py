import pygame
import random

particles = []

class particle():
    def __init__(self, x, y, duration, color, vx, vy, rangeX, rangeY):
        self.x = x
        self.y = y
        self.duration = duration
        self.color = color
        self.vx = random.randint(vx - rangeX, vx + rangeX)
        self.vy = random.randint(vy - rangeY, vy + rangeY)

def CreateParticles(amount, x, y):
    for i in range(amount):
        particles.append(particle(random.randint(x - 30, x + 30), random.randint(y, y + 40), random.randint(20, 40), (230, 230, 230), 0, -3, 6, 3))

def RenderParticles(screen):
    global particles
    for particle in particles:
        pygame.draw.circle(screen, particle.color, (particle.x, particle.y), particle.duration / 2)
        particle.duration -= 1
        particle.x += particle.vx
        particle.y += particle.vy
        particle.vy += 0.2
        if particle.duration <= 0:
            particles.remove(particle)

def ContinuousParticles(x ,y, color, size, vx, vy, rangeX, rangeY):
    global particles
    particles.append(particle(x, y, random.randint(size - 10, size + 10), color, vx, vy, rangeX, rangeY))