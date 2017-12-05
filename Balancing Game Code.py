"""Balancing Game."""
import sys
import random
import pygame
from pygame.locals import *
import pymunk
import pymunk.pygame_util

def spawn_small_box(space):
    """A funtion that controls how the boxes will spawn."""
    mass = 10
    h = random.randint(5, 15)
    w = h
    size = (h, w)
    intertia = pymunk.moment_for_box(mass, size)
    body = pymunk.Body(mass, intertia)
    body.position = 300, 500
    box = pymunk.Poly(body, [(-w, -h), (-w, h), (w, -h), (w, h)])
    box.friction = 0.5
    box.elasticity = 0
    space.add(body, box)
    return box

def spawn_medium_box(space):
    """A funtion that controls how the boxes will spawn."""
    mass = 10
    h = random.randint(16, 25)
    w = h
    size = (h, w)
    intertia = pymunk.moment_for_box(mass, size)
    body = pymunk.Body(mass, intertia)
    body.position = 300, 500
    box = pymunk.Poly(body, [(-w, -h), (-w, h), (w, -h), (w, h)])
    box.friction = 0.5
    box.elasticity = 0
    space.add(body, box)
    return box

def spawn_large_box(space):
    """A funtion that controls how the boxes will spawn."""
    mass = 10
    h = random.randint(26, 40)
    w = h
    size = (h, w)
    intertia = pymunk.moment_for_box(mass, size)
    body = pymunk.Body(mass, intertia)
    body.position = 300, 500
    box = pymunk.Poly(body, [(-w, -h), (-w, h), (w, -h), (w, h)])
    box.friction = 0.5
    box.elasticity = 0
    space.add(body, box)
    return box

def help():
    print("Escape: Exit")
    print("S: Spawn Small Box")
    print("M: Spawn Medium Box")
    print("L: Spawn Large Box")
    print("Left: Move Left (Not Working)")
    print("Right: Move Right (Not Working)")


def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("How well can you balance? For command help press 'c'")
    clock = pygame.time.Clock()

    space = pymunk.Space()
    space.gravity = (0.0, -450.0)

    lines = draw_balance_thing(space)
    boxs = []

    draw_options = pymunk.pygame_util.DrawOptions(screen)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                sys.exit(0)
            elif event.type == KEYDOWN and event.key == pygame.K_LEFT:
                x -= 10
            elif event.type == KEYDOWN and event.key == pygame.K_RIGHT:
                boxs += 10
            elif event.type == KEYDOWN and event.key == pygame.K_s:
                box_shape = spawn_small_box(space)
                boxs.append(box_shape)
            elif event.type == KEYDOWN and event.key == pygame.K_m:
                box_shape = spawn_medium_box(space)
                boxs.append(box_shape)
            elif event.type == KEYDOWN and event.key == pygame.K_l:
                box_shape = spawn_large_box(space)
                boxs.append(box_shape)
            elif event.type == KEYDOWN and event.key == pygame.K_c:
                help()

        boxs_to_remove = []
        for box in boxs:
            if box.body.position.y < 0:
                boxnum = len(boxs) - 1
                print(boxnum, "of boxes were stacked successfully")
                boxs_to_remove.append(box)
                sys.exit(0)

        for box in boxs_to_remove:
            space.remove(box, box.body)
            boxs.remove(box)

        screen.fill((255, 255, 255))

        space.debug_draw(draw_options)

        space.step(1 / 100.0)

        pygame.display.flip()
        clock.tick(50)

def draw_balance_thing(space):
    """Adds in the thing we will be balancing on."""
    rotation_center_body = pymunk.Body(body_type=pymunk.Body.STATIC)
    rotation_center_body.position = (300, 200)
    rotation_main_body = pymunk.Body(body_type=pymunk.Body.STATIC)
    rotation_main_body.position = (300, 200)

    body = pymunk.Body(10, 10000)
    body.position = (300, 200)
    l1 = pymunk.Segment(body, (-200, 0), (200, 0.0), 5.0)
    l1.friction = 0.5
    l1.elasticity = 0

    rotation_center_joint = pymunk.constraint.SlideJoint(body, rotation_center_body, anchor_a=(-25,0), anchor_b=(-25,10), min=0, max=10)
    rotation_main_joint = pymunk.constraint.SlideJoint(body, rotation_main_body, anchor_a=(25,0), anchor_b=(25,10), min=0, max=10)
    joint = pymunk.constraint.PinJoint(body, rotation_main_body, anchor_a=(-75,0), anchor_b=(75,0))
    space.add(l1, body, rotation_center_joint, rotation_main_joint, joint)
    return l1



main()
