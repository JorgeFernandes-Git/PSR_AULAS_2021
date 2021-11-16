#!/usr/bin/python3
import time

import cv2 as cv
import numpy as np

image = None  # background image
moving_mouse = False  # bool for drawing
color_draw = (0, 0, 0)  # pen color


def mouse_draw(event, x, y, flags, param):
    global image, pt1_y, pt1_x
    global moving_mouse
    global color_draw

    # detect if left button is pressed
    if event == cv.EVENT_LBUTTONDOWN:
        moving_mouse = True
        pt1_x, pt1_y = x, y

    # disable the flag to stop drawing
    if event == cv.EVENT_LBUTTONUP:
        moving_mouse = False
        cv.line(image, (pt1_x, pt1_y), (x, y), color_draw, 2)


    # draw while mouse is moving
    if event == cv.EVENT_MOUSEMOVE:
        if moving_mouse:
            cv.line(image, (pt1_x, pt1_y), (x, y), color_draw, 2)
            pt1_x, pt1_y = x, y


def main():
    global image
    global color_draw

    # create a white image background dim 600*400
    image = np.zeros((600, 400, 3), dtype="float64")
    image.fill(255)

    # mouse call back
    cv.namedWindow("image")
    cv.setMouseCallback("image", mouse_draw)

    # instructions
    print("Use the mouse to draw by holding left button")
    print("Press r to select red color")
    print("Press g to select green color")
    print("Press b to select blue color")
    print("Press B to select black color")
    print("Press c to clean")
    print("Press ESC to quit")

    # draw cycle
    while True:

        # ESC to close
        k = cv.waitKey(1) & 0xFF
        if k == 27:
            break

        # clean the screen
        if k == ord("c"):
            image = np.zeros((600, 400, 3), dtype="float64")
            image.fill(255)
            print("CLEAN")

        # red color
        if k == ord("r"):
            color_draw = (0, 0, 255)
            print("YOU SELECT RED COLOR")

        # green color
        if k == ord("g"):
            color_draw = (0, 255, 0)
            print("YOU SELECT GREEN COLOR")

        # blue color
        if k == ord("b"):
            color_draw = (255, 0, 0)
            print("YOU SELECT BLUE COLOR")

        # black color
        if k == ord("B"):
            color_draw = (0, 0, 0)
            print("YOU SELECT BLACK COLOR")

        # show the image
        cv.imshow("image", image)

    # close
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
