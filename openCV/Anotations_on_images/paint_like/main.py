#!/usr/bin/python3

import copy
import pickle
import cv2
import numpy as np

image = None  # background image
image_contours = None  # image contours
moving_mouse = False  # bool for drawing
color_draw = (0, 0, 0)  # pen color
pen_thickness = 5
pt1_y, pt1_x = 0, 0


def mouse_draw(event, x, y, flags, param):
    global image, image_contours, pt1_y, pt1_x
    global moving_mouse
    global color_draw, pen_thickness

    # detect if left button is pressed
    if event == cv2.EVENT_LBUTTONDOWN:
        moving_mouse = True
        pt1_x, pt1_y = x, y
        # print(x, y)

    # disable the flag to stop drawing
    if event == cv2.EVENT_LBUTTONUP:
        moving_mouse = False
        cv2.line(image, (pt1_x, pt1_y), (x, y), color_draw, pen_thickness)
        # cv2.line(image_contours, (pt1_x, pt1_y), (x, y), color_draw, pen_thickness)

    # draw while mouse is moving
    if event == cv2.EVENT_MOUSEMOVE:
        if moving_mouse:
            cv2.line(image, (pt1_x, pt1_y), (x, y), color_draw, pen_thickness)
            # cv2.line(image_contours, (pt1_x, pt1_y), (x, y), color_draw, pen_thickness)
            pt1_x, pt1_y = x, y


def main():
    global image, image_contours
    global color_draw, pen_thickness

    # create a white image background dim 600*400
    image = cv2.imread("/home/jorge/Desktop/UA/PSR/Pycharm_EX/psr_21-22/Parte07/images/pinguim.png")
    # image = np.zeros((600, 400, 3), dtype="float64") # white background
    # image.fill(255)

    # named windows and mouse callback
    cv2.namedWindow("image")
    # cv2.namedWindow("image_contours")
    cv2.setMouseCallback("image", mouse_draw)
    # cv2.setMouseCallback("image_contours", mouse_draw)

    # instructions
    print("Use the mouse to draw by holding left button")
    print("Press r to select red color")
    print("Press g to select green color")
    print("Press b to select blue color")
    print("Press B to select black color")
    print("Press c to clean")
    print("Press ESC to quit")

    # ----------------------------THIS METHOD DOESN'T WORK---------------
    # mask
    # image_gray = copy.deepcopy(image)
    # image_gray = cv2.cvtColor(image_gray, cv2.COLOR_BGR2GRAY)

    # get contours
    # contours, hierarchy = cv2.findContours(image_gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    # image_contours = cv2.drawContours(image_gray, contours, -1, (0, 255, 0), 3)

    # convert to BGR
    # image_contours = cv2.cvtColor(image_contours, cv2.COLOR_GRAY2BGR)
    # --------------------------------------------------------------------

    # open shapes file from find_contours.py
    with open("shapes", "rb") as file:
        shapes_color = pickle.load(file)
    # print(shapes_color)
    # print(len(shapes_color))

    # draw cycle
    while True:



        """
        interactive keys (k) -----------------------------------------
        """
        # ESC to close
        k = cv2.waitKey(1) & 0xFF
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

        if k == 43:  # caracter + "Aumentar linha"
            pen_thickness += 1
            print("THICKNESS: " + str(pen_thickness))

        if k == 45:  # caracter - "Diminuir linha"
            pen_thickness -= 1
            if pen_thickness < 0:
                pen_thickness = 0
            print("THICKNESS: " + str(pen_thickness))

        # show the image
        cv2.imshow("image", image)
        # cv2.imshow("image_contours", image_contours)

    # close
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
