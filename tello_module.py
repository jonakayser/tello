'''
classes and functions for tello control
by Jona
'''

import numpy as np
import cv2
from djitellopy import tello
import pygame
from pygame.locals import *

axis_values = [0, 0, 0, 0]

def startup():
    # instantiate and connect tello drone
    drone = tello.Tello()
    drone.connect()

    # get battery status
    print('Drone connected. Battery status: {}'.format(drone.get_battery()))

    # start video
    print('Starting video thread...')
    drone.streamon()
    print('Video ink established')

    return drone


def update_video(drone):
    img = drone.get_frame_read().frame
    img = cv2.resize(img, (360,240))    # resize for better processing speed
    cv2.imshow("Image", img)
    cv2.waitKey(1)

def init_joystick():
    pygame.init()
    pygame.joystick.init()
    joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
    for joystick in joysticks:
        print('Joystick: {} ...connected'.format(joystick.get_name()))

    pygame.display.set_caption('game base')
    screen = pygame.display.set_mode((200, 200), 0, 32)

    return screen

def fly(drone, screen):

    # get joystick inputs
    for event in pygame.event.get():
        if event.type == JOYBUTTONDOWN:
            print(event)
            if event.button == 3:
                drone.land()
            elif event.button == 5:
                drone.takeoff()
            elif event.button == 0:
                axis_values[3] = 0.5
            elif event.button == 1:
                axis_values[3] = -0.5

        if event.type == JOYBUTTONUP:
            if event.button == 0:
                axis_values[3] = 0
            elif event.button == 1:
                axis_values[3] = 0

        if event.type == JOYAXISMOTION and abs(event.value) > 0.1:
            print(event)
            if event.axis < 4:
                axis_values[event.axis] = event.value

    # apply dead zones and scaling ->refactor
    print('raw axis values: {}'.format(axis_values))
    for axis_id in range(len(axis_values)):
        if abs(axis_values[axis_id]) < 0.1:
            axis_values[axis_id] = 0
    max_input = 100
    controls = [int(x*max_input) for x in axis_values]
    print('dead zone axis values: {}'.format(axis_values))
    print('controls: {}'.format(controls))

    # draw joystick position
    position_indicator = pygame.Rect(10, 10, 10, 10)
    pygame.draw.rect(screen, (255, 0, 0), position_indicator)
    position_indicator.x = controls[0] + 100
    position_indicator.y = controls[1] + 100

    # send controls to drone
    drone.send_rc_control(controls[0], -controls[1], controls[3], controls[2])
