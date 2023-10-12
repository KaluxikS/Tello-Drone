import KeyPressModule as kp
from droneblocks.DroneBlocksTello import DroneBlocksTello
from time import sleep
import cv2

def get_keyboard_input():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50
    if kp.get_key("LEFT"):
        t.display_right_arrow()
        lr = -speed

    elif kp.get_key("RIGHT"):
        t.display_left_arrow()
        lr = speed

    if kp.get_key("UP"):
        t.display_up_arrow()
        fb = speed
    elif kp.get_key("DOWN"):
        t.display_down_arrow()
        fb = -speed

    if kp.get_key("w"):
        t.display_up_arrow()
        ud = speed
    elif kp.get_key("s"):
        t.display_down_arrow()
        ud = -speed

    if kp.get_key("d"):
        t.display_left_arrow()
        yv = speed
    elif kp.get_key("a"):
        t.display_right_arrow()
        yv = -speed

    if kp.get_key("q"):
        t.display_character("L")
        t.land()
        is_flying = False

    if kp.get_key("e"):
        t.display_character("S")
        t.takeoff()
        t.display_character("R")

    if t.get_battery() > 51:
        if kp.get_key("p"):
            t.display_heart()
            t.flip_right()
        if kp.get_key("o"):
            t.display_heart()
            t.flip_forward()
        if kp.get_key("i"):
            t.display_heart()
            t.flip_back()
        if kp.get_key("u"):
            t.display_heart()
            t.flip_left()

    if kp.get_key("m"):
        t.display_character("L")
        distance = t.get_height()
        is_flying = True
        while is_flying:
            if t.get_height() > distance + 10:
                t.land()
                is_flying = False

    if kp.get_key("b"):
        for i in range(10):
            print(t.get_battery(), "% - batter lvl")
    if kp.get_key("h"):
        print(t.get_height(), "- current height!")

    if kp.get_key("c"):
        print(is_flying)

    return[lr, fb, ud, yv]


kp.init()
t = DroneBlocksTello()
t.connect()
print(t.get_battery(), "% - batter lvl")
t.streamon()
t.display_heart()


while True:
    img = t.get_frame_read().frame
    cv2.imshow("Image", img)
    vals = get_keyboard_input()
    if all(item == 0 for item in vals):
        t.display_smile()
    t.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(0.05)

