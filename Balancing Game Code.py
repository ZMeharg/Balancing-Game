"""Balancing Game?"""
import sys
import random
import pygame
from pygame.locals import *
import pymunk
import pymunk.pygame_util

def add_ball(space):
    """Add a ball to the given space at a random position"""
    mass = 1
    radius = random.randint(2, 20)
    inertia = pymunk.moment_for_circle(mass, 0, radius, (0, 0))
    body = pymunk.Body(mass, inertia)
    x = random.randint(200, 350)
    body.position = x, 550
    shape = pymunk.Circle(body, radius, (0, 0))
    space.add(body, shape)
    return shape

# def add_rectangle(space):
#     """Add a rectangle with random heights and widths."""
#     mass = 1
#     h = random.randint(2, 10)
#     w = random.randit(2,10)
#     inertia = pymunk.moment_for_box(mass, w, h)
#     body = pymunk.Body(mass, inertia)
#     x = random.

def add_L(space):
    """Add a inverted L shape with two joints"""
    rotation_center_body = pymunk.Body(body_type=pymunk.Body.STATIC)
    rotation_center_body.position = (300, 300)

    # rotation_limit_body = pymunk.Body(body_type=pymunk.Body.STATIC)
    # rotation_limit_body.position = (200, 300)

    body = pymunk.Body(10, 10000)
    body.position = (300, 300)
    l1 = pymunk.Segment(body, (-150, 0), (255.0, 0.0), 5.0)
    # l2 = pymunk.Segment(body, (-150.0, 0), (-150.0, 50.0), 5.0)

    rotation_center_joint = pymunk.GrooveJoint(body, rotation_center_body, (0, 0), (0, 0))
    joint_1 = pymunk.GrooveJoint(body, rotation_center_body, (-100, 0), (0, 0))
    joint_2 = pymunk.GrooveJoint(body, rotation_center_body, (200, 0), (0, 0))
    space.add(l1, body, rotation_center_joint, joint_1, joint_2)
    return l1 



def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Joints. Just wait and the L will tip over")
    clock = pygame.time.Clock()

    space = pymunk.Space()
    space.gravity = (0.0, -900.0)

    lines = add_L(space)
    balls = []
    draw_options = pymunk.pygame_util.DrawOptions(screen)

    ticks_to_next_ball = 10
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                sys.exit(0)

        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_D:
                ball_shape = add_ball(space)
                balls.append(ball_shape)

        screen.fill((255, 255, 255))

        balls_to_remove = []
        for ball in balls:
            if ball.body.position.y < 150:
                balls_to_remove.append(ball)

        ticks_to_next_ball -= 1
        if ticks_to_next_ball <= 0:
            ticks_to_next_ball = 25
            ball_shape = add_ball(space)
            balls.append(ball_shape)
        # for ball in balls_to_remove:
        #     space.remove(ball, ball.body)
        #     balls.remove(ball)

        space.debug_draw(draw_options)

        space.step(1 / 50.0)

        pygame.display.flip()
        clock.tick(50)

if __name__ == '__main__':
    main()