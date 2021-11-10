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
    white_background = np.zeros((900, 900, 3), dtype="float64")
    white_background.fill(255)
    # window for display white background/draw area
    draw_area = "Draw Area"
    cv2.namedWindow(draw_area)

    while True:
        # read the image
        _, image = capture.read()
        image = cv2.resize(image, (750, 422))  # resize the capture window

        # transform the image and show it
        mask = cv2.inRange(image, mins_pcss, maxs_pcss)  # colors mask
        image_segmenter = cv2.bitwise_and(image, image, mask=mask)

        # imshows
        cv2.imshow(window_segmented, image_segmenter)  # drawing object (pen)
        cv2.imshow(draw_area, white_background)  # draw area

        """
        interactive keys (k) -----------------------------------------
        """
        # ESC to close
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

    capture.release()  # free the webcam for other use
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
