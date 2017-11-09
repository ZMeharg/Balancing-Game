"""Balancing Game?"""
import sys
import random
import pygame
from pygame.locals import *
import pymunk
import pymunk.pygame_util

# def add_ball(space):
#     """Add a ball to the given space at a random position"""
#     mass = 1
#     radius = 10
#     inertia = pymunk.moment_for_circle(mass, 0, radius, (0, 0))
#     body = pymunk.Body(mass, inertia)
#     x = 175
#     body.position = x, 550
#     shape = pymunk.Circle(body, radius, (0, 0))
#     space.add(body, shape)
#     return shape

# def move_box():
#     x = 175
#     for event in pygame.event.get(): 
#         if event.type == pygame.KEYDOWN:
#             pressed = pygame.key.get_pressed()
#             if pressed[pygame.k_LEFT]:
#                 x -= 10
#             if pressed[pygame.k_RIGHT]:
#                 x += 10

def add_box(space):
    """Add a rectangle with random heights and widths."""
    mass = 1
    h = random.randint(10, 20)
    w = random.randint(10, 20)
    size = (h, w)
    inertia = pymunk.moment_for_box(mass, size)
    body = pymunk.Body(mass, inertia)
    body.position.x = 300
    body.position = (300, 500)
    box = pymunk.Poly(body, [(-w, -h), (-w,h), (w,-h), (w,h)])
    box.friction = 10
    space.add(body, box)
    return box

def move_box():
    pressed = pygame.key.get_pressed()
    if pressed[k_RIGHT]:
        body.positoin.x += 10
    if pressed[k_LEFT]:
        body.position.x -= 10



def add_L(space):
    """Add a inverted L shape with two joints"""
    rotation_center_body = pymunk.Body(body_type=pymunk.Body.STATIC)
    rotation_center_body.position = (300, 300)
    rotation_main_body = pymunk.Body(body_type=pymunk.Body.STATIC)
    rotation_main_body.position = (300, -200)

    body = pymunk.Body(10, 10000)
    body.position = (300, 300)
    l1 = pymunk.Segment(body, (-150, 0), (150, 0.0), 5.0)
    l1.friction = 1
    # l2 = pymunk.Segment(body, (0, 0), (0, -400), 5.0)
    # l3 = pymunk.Segment(body, (-150, 0), (0, -200), 5.0)
    

    rotation_center_joint = pymunk.constraint.PinJoint(body, rotation_center_body, anchor_a=(0,0), anchor_b=(0,0))
    rotation_main_joint = pymunk.constraint.PinJoint(body, rotation_main_body, anchor_a=(0,-150), anchor_b=(0, -50))
    # joint_1 = pymunk.constraint.PinJoint(body, rotation_center_body, anchor_a=(0,-200), anchor_b=(0,0))
    # joint_2 = pymunk.constraint.PinJoint(body, rotation_center_body, anchor_a=(0, -200), anchor_b=(50,-200))
    # rotation_center_joint = pymunk.GrooveJoint(body, rotation_center_body, (0, 0), (0, 0))
    # joint_1 = pymunk.GrooveJoint(body, rotation_center_body, (-100, 0), (0, 0))
    # joint_2 = pymunk.PinJoint(body, rotation_center_body, (200, 0), (0, 0))
    space.add(l1, body, rotation_center_joint, rotation_main_joint)
    return l1



def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("How well can you balance")
    clock = pygame.time.Clock()

    space = pymunk.Space()
    space.gravity = (0.0, -900.0)

    lines = add_L(space)
    boxs = []
    draw_options = pymunk.pygame_util.DrawOptions(screen)

    while True:
        # Activation_Keys()

        screen.fill((255, 255, 255))

        # for box in boxs:
        #     if box.body.position.y < 100:
        #         sys.exit(0)


        # ticks_to_next_box = 50

        # if ticks_to_next_box <= 49:
        #     ticks_to_next_box = + 1
        #     box_shape = add_box(space)
        #     boxs.append(box_shape)
        ticks_to_next_box = 3
        for i in range(1, ticks_to_next_box):
            ticks_to_next_boxs = ticks_to_next_box + 1
            if ticks_to_next_box <= 50:
                if ticks_to_next_box == ticks_to_next_boxs:
                    box_shape = add_box(space)
                    boxs.append(box_shape)
            elif ticks_to_next_box >= 50:
                sys.exit(0)
    


        space.debug_draw(draw_options)

        space.step(1 / 50.0)

        pygame.display.flip()
        clock.tick(50)

def Activation_Keys():
    """The list of keys pressed to do things."""
    space = pymunk.Space()
    balls = []
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)
        elif event.type == KEYDOWN:
            pressed = event.key
            if pressed == K_ESCAPE:
                sys.exit(0)
            if pressed == K_SPACE:
                balls.append(add_ball(space))
                return balls

if __name__ == '__main__':
    main()