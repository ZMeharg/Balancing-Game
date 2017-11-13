"""Balancing Game?"""
import sys
import random
import pygame
from pygame.locals import *
import pymunk
import pymunk.pygame_util
def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("How well can you balance?")
    clock = pygame.time.Clock()

    space = pymunk.Space()
    space.gravity = (0.0, -900.0)

    draw_options = pymunk.pygame_util.DrawOptions(screen)

    space.debug_draw(draw_options)

    space.step(1 / 50.0)

    pygame.display.flip()
    clock.tick(50)

def spawn_box(space):
    mass = 1
    h = random.randint(10, 20)
    w = random.randint(10, 20)
    size = (h, w)
    intertia = pymunk.moment_for_box(mass, size)

    x = 300
    if event.type == pygame.KEYDOWN:
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RIGHT]:
            x += 10
        if pressed[pygame.K_LEFT]:
            x -= 10
    body = pymunk.Body(mass, intertia)
    body.position = (x, 500)
    box = pymunk.Poly(body, [(-w, -h), (-w, h), (w, -h), (w, h)])
    box.friction = 10
    space.add(body, box)


done = False
while not done:
    main()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    spawn_box()
