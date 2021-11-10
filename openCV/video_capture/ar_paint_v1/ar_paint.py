#!/usr/bin/python3


import argparse
import json

import cv2
import numpy as np

# dictionary with ranges
ranges_pcss = {"b": {"min": 100, "max": 256},
               "g": {"min": 100, "max": 256},
               "r": {"min": 100, "max": 256},
               }


def main():
    # parse the json file with BGR limits (from color_segmenter.py)
    parser = argparse.ArgumentParser(description="Load a json file with limits")
    parser.add_argument("-j", "--json", type=str, required=True, help="Full path to json file")
    args = vars(parser.parse_args())

    # read the json file
    with open(args["json"], "r") as file_handle:
        data = json.load(file_handle)

    # print json file then close
    # print(data)  # debug
    file_handle.close()

    ranges_pcss["b"]["min"] = data["b"]["min"]
    ranges_pcss["b"]["max"] = data["b"]["max"]
    ranges_pcss["g"]["min"] = data["g"]["min"]
    ranges_pcss["g"]["max"] = data["g"]["max"]
    ranges_pcss["r"]["min"] = data["r"]["min"]
    ranges_pcss["r"]["max"] = data["r"]["max"]

    # print(ranges_pcss)  # debug

    # numpy arrays
    mins_pcss = np.array([ranges_pcss['b']['min'], ranges_pcss['g']['min'], ranges_pcss['r']['min']])
    maxs_pcss = np.array([ranges_pcss['b']['max'], ranges_pcss['g']['max'], ranges_pcss['r']['max']])

    # initial setup
    capture = cv2.VideoCapture(0)  # connect to webcam

    # create the window
    window_segmented = "Color Segmenter"
    cv2.namedWindow(window_segmented, cv2.WINDOW_AUTOSIZE)

    # create a white image background dim 600*400
    white_background = np.zeros((422, 750, 3), dtype="float64")
    white_background.fill(255)
    # window for display white background/draw area
    draw_area = "Draw Area"
    cv2.namedWindow(draw_area)
    color_draw = (0, 0, 0)
    pen_thickness = 5

    while True:
        # read the image
        _, image = capture.read()
        image = cv2.resize(image, (750, 422))  # resize the capture window

        # apply filters
        # blurred_frame = cv2.GaussianBlur(image, (5, 5), 0)

        # transform the image and show it
        mask = cv2.inRange(image, mins_pcss, maxs_pcss)  # colors mask
        image_segmenter = cv2.bitwise_and(image, image, mask=mask)

        # get contours
        contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        # cv2.drawContours(image_segmenter, contours, -1, (0, 0, 255), 3)
        # cv2.drawContours(image, contours, -1, (0, 0, 255), 3)

        # create the rectangle over object
        for contours in contours:
            (x, y, w, h) = cv2.boundingRect(contours)

            # draw the rectangle only if the area is > 3000 px
            # print(cv2.contourArea(contours)) # debug
            if cv2.contourArea(contours) < 3000:
                continue

            # draw the rectangle
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # dot in the center of the rectangle
            a = x + w/2
            b = y + h/2
            cv2.circle(image, (int(a), int(b)), 10, (0, 0, 0), cv2.FILLED)

            # draw in the white background
            cv2.circle(white_background, (int(a), int(b)), pen_thickness, color_draw, cv2.FILLED)

        # imshows
        cv2.imshow(window_segmented, image_segmenter)  # drawing object (pen)
        cv2.imshow(draw_area, white_background)  # draw area
        cv2.imshow("original", image)

        """
        interactive keys (k) -----------------------------------------
        """
        # ESC to close
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

        # clean the screen
        if k == ord("c"):
            white_background = np.zeros((422, 750, 3), dtype="float64")
            white_background.fill(255)
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

        if k == ord("T"):
            pen_thickness += 1
            print("thickness: " + str(pen_thickness))

        if k == ord("t"):
            pen_thickness -= 1
            if pen_thickness < 0:
                pen_thickness = 0
            print("thickness: " + str(pen_thickness))

    capture.release()  # free the webcam for other use
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
