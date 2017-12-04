"""Balancing Game."""
import sys
import random
import pygame
from pygame.locals import *
import pymunk
import pymunk.pygame_util

def spawn_box(space):
    """A funtion that controls how the boxes will spawn."""
    mass = 10
    h = random.randint(10, 40)
    w = random.randint(10, 40)
    size = (h, w)
    intertia = pymunk.moment_for_box(mass, size)
    body = pymunk.Body(mass, intertia)
    body.position = (300, 500)
    box = pymunk.Poly(body, [(-w, -h), (-w, h), (w, -h), (w, h)])
    box.friction = 10
    box.elasticity = 0
    space.add(body, box)
    return box

class mover:

    def __init__(self, x, y, keys):
        self.x = x
        self.y = y
        self.keys = keys
        self.up = ord(keys["up"])
        self.down = ord(keys["down"])
        self.left = ord(keys["left"])
        self.right = ord(keys["right"])
        self.origin = (x, y)

    def update(self):
        pressed = pygame.key.get_pressed()
        if pressed[self.up]:
            self.y -= 55
        if pressed[self.down]:
            self.y += 55
        if pressed[self.left]:
            self.x -= 55
        if pressed[self.right]:
            self.x += 55
        if self.x < 20:
            self.x = 20
        if self.x > b:
            self.x = b
        if self.y < 20:
            self.y = 20
        if self.y > b:
            self.y = b

mover1 = mover(100, 600, {"left": "j", "down": "k", "right": "l", "up": "i"})

def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Joints. Just wait and the L will tip over")
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
            elif event.type == KEYDOWN and event.key == pygame.K_SPACE:
                box_shape = spawn_box(space)
                boxs.append(box_shape)

        for box in boxs:
            if box.body.position.y < 0:
                sys.exit(0)
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
    l1.friction = 10
    l1.elasticity = 0

    rotation_center_joint = pymunk.constraint.PinJoint(body, rotation_center_body, anchor_a=(-75,0), anchor_b=(-75,25))
    rotation_main_joint = pymunk.constraint.PinJoint(body, rotation_main_body, anchor_a=(75,0), anchor_b=(75,25))
    joint = pymunk.constraint.PinJoint(body, rotation_main_body, anchor_a=(-75,0), anchor_b=(75,0))
    space.add(l1, body, rotation_center_joint, rotation_main_joint, joint)
    return l1



main()
