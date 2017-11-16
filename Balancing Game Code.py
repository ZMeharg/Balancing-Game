"""Balancing Game."""
import sys
import random
import pygame
from pygame.locals import *
import pymunk
import pymunk.pygame_util


def main():
    """Function that sets up the screen."""
    pygame.init()
    screen = pygame.display.set_mode((600, 800))
    pygame.display.set_caption("How well can you balance?")
    clock = pygame.time.Clock()
    screen.fill((255, 255, 255))

    space = pymunk.Space()
    space.gravity = (0.0, -9000.0)

    lines = draw_balance_thing(space)
    boxes = spawn_box(space)
    draw_options = pymunk.pygame_util.DrawOptions(screen)

    # for box in boxes:
    #     if box <= 30:
    #         box += 1
    #         box_shape = spawn_box(space)
    #         boxes.append(box_shape)

    space.debug_draw(draw_options)

    space.step(1 / 50.0)

    pygame.display.flip()
    clock.tick(50)


def spawn_box(space):
    """A funtion that controls how the boxes will spawn."""
    mass = 1
    h = random.randint(10, 20)
    w = random.randint(10, 20)
    size = (h, w)
    intertia = pymunk.moment_for_box(mass, size)

    # x = 300
    # for event in pygame.event.get():
    #     if event.type == pygame.KEYDOWN:
    #         pressed = pygame.key.get_pressed()
    #         if pressed[pygame.K_RIGHT]:
    #             x += 10
    #         if pressed[pygame.K_LEFT]:
    #             x -= 10
    x = random.randint(150, 450)
    body = pymunk.Body(mass, intertia)
    body.position = x, 700
    box = pymunk.Poly(body, [(-w, -h), (-w, h), (w, -h), (w, h)])
    box.friction = 10
    box.color = ((255, 255, 0))
    space.add(body, box)
    return box

# def spawn_rate():
#     """Determine how long until a new box comes, hopefully."""
#     num_boxes_on_screen = []
#     box = 1
#     for box in num_boxes_on_screen:
#         if box <= 30:
#             box += 1
#             num_boxes_on_screen + 1
#         if box == num_boxes_on_screen:
#             "Print Sorry"


def draw_balance_thing(space):
    """Adds in the thing we will be balancing on."""
    rotation_center_body = pymunk.Body(body_type=pymunk.Body.STATIC)
    rotation_center_body.position = (300, 300)
    rotation_main_body = pymunk.Body(body_type=pymunk.Body.STATIC)
    rotation_main_body.position = (300, -200)

    body = pymunk.Body(10, 10000)
    body.position = (300, 300)
    l1 = pymunk.Segment(body, (-150, 0), (150, 0.0), 5.0)
    l1.friction = 1

    rotation_center_joint = pymunk.constraint.PinJoint(body, rotation_center_body, anchor_a=(0,0), anchor_b=(0,0))
    rotation_main_joint = pymunk.constraint.PinJoint(body, rotation_main_body, anchor_a=(0,-150), anchor_b=(0, -50))
    space.add(l1, body, rotation_center_joint, rotation_main_joint)
    return l1


done = False
while not done:
    main()
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_ESCAPE]:
                sys.exit(0)
            done = True
    
