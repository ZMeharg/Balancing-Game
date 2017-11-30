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



# def add_box(space):
#     ticks_to_next_ball = 10
#     ticks_to_next_ball -= 1
#     if ticks_to_next_ball <= 0:
#         ticks_to_next_ball = 150
#         ball_shape = spawn_box(space)
#         balls.append(ball_shape)


def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Joints. Just wait and the L will tip over")
    clock = pygame.time.Clock()

    space = pymunk.Space()
    space.gravity = (0.0, -450.0)

    lines = draw_balance_thing(space)
    draw_options = pymunk.pygame_util.DrawOptions(screen)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                sys.exit(0)
            elif event.type == KEYDOWN and event.key == pygame.K_SPACE:
                spawn_box(space)
            elif event.type == KEYDOWN and event.key == pygame.K_LEFT:
                x -= 10
                print(x)
            elif event.type == KEYDOWN and event.key == pygame.K_RIGHT:
                x += 10
                print(x)

        # ticks_to_next_ball -= 1
        # if ticks_to_next_ball <= 0:
        #     ticks_to_next_ball = 150
        #     ball_shape = spawn_box(space)
        #     balls.append(ball_shape)

        screen.fill((255, 255, 255))

        # balls_to_remove = []
        # for ball in balls:
        #     if ball.body.position.y < 100:
        #         sys.exit(0)

        # for ball in balls_to_remove:
        #     space.remove(ball, ball.body)
        #     balls.remove(ball)

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
