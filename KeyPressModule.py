# Modeule to detect key press

import pygame


def init():
    pygame.init()
    win = pygame.display.set_mode((400, 400))


def getKey(keyName):
    ans = False
    for eve in pygame.event.get(): pass
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame, 'K_{}'.format(keyName))
    if keyInput[myKey]:
        ans = True

    pygame.display.update()

    return ans

def getKeyboardInput(TelloObj):
    me = TelloObj

    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50
    yaw_speed = 60

    if getKey('LEFT'):
        lr = -speed
    elif getKey('RIGHT'):
        lr = speed

    if getKey('UP'):
        fb = speed
    elif getKey('DOWN'):
        fb = -speed

    if getKey('w'):
        ud = speed
    elif getKey('s'):
        ud = -speed

    if getKey('a'):
        yv = -yaw_speed
    elif getKey('d'):
        yv = yaw_speed

    if getKey('q'):
        me.land()
    elif getKey('e'):
        me.takeoff()

    if getKey('b'):
        me.flip('b')

    if getKey('y'):
        me.emergency()


    return [lr, fb, ud, yv]


def main():
    if getKey('LEFT'):
        print('Left key pressed...')
    if getKey('RIGHT'):
        print('Right key pressed...')


if __name__ == '__main__':
    init()
    while True:
        main()
