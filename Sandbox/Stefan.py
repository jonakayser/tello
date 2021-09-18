import djitellopy as tello
from Sandbox import KeyPressModule as kp

import time

kp.init()

# get things going
me = tello.Tello()
me.connect()
print("battery = {}".format(me.get_battery()))
# me.takeoff()

# # countdown
# timer = 5
# while timer > 0:
#     print(timer)
#     time.sleep(1)
#     timer -= 1

while True:
    vals = kp.getKeyboardInput(me)
    me.send_rc_control(vals[0],vals[1],vals[2],vals[3])

    # if 5 seconds passed, say I'm still alive
    timer_delay = 5
    start_time = time.time()
    if time.time()-start_time > timer_delay:
        print('still alive')
        start_time = time.time()


print("let's land")

# land this bird
me.land()
print("that was fun")
me.disconnect()

