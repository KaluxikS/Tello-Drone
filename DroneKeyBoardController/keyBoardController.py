import KeyPressModule as kp
from djitellopy import tello
from time import sleep
import cv2


def get_keyboard_input():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50

    if kp.get_key("LEFT"): lr = -speed
    elif kp.get_key("RIGHT"): lr = speed

    if kp.get_key("UP"): fb = speed
    elif kp.get_key("DOWN"): fb = -speed

    if kp.get_key("w"): ud = speed
    elif kp.get_key("s"): ud = -speed

    if kp.get_key("d"): yv = speed
    elif kp.get_key("a"): yv = -speed

    if kp.get_key("q"): t.land()
    if kp.get_key("e"): t.takeoff()
    if kp.get_key("p"): t.flip_right()
    if kp.get_key("o"): t.flip_forward()
    if kp.get_key("i"): t.flip_back()
    if kp.get_key("u"): t.flip_left()

    return[lr, fb, ud, yv]


kp.init()
t = tello.Tello()
t.connect()
print(t.get_battery(), "%")
t.streamon()


while True:
    img = t.get_frame_read().frame
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cv2.imshow("Image", img_rgb)
    vals = get_keyboard_input()
    t.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(0.05)

