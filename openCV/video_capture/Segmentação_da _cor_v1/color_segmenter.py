#!/usr/bin/python3
import json

import cv2
import numpy as np


def onTrackbar(threshold):
    pass


def main():
    # initial setup
    capture = cv2.VideoCapture(0)  # connect to webcam

    # create the window
    window_name = "Color Segmenter"
    window_regular = "Video Capture"
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.namedWindow(window_regular, cv2.WINDOW_NORMAL)

    # create the trackbars
    cv2.createTrackbar("min B", window_name, 0, 255, onTrackbar)
    cv2.createTrackbar("max B", window_name, 0, 255, onTrackbar)
    cv2.createTrackbar("min G", window_name, 0, 255, onTrackbar)
    cv2.createTrackbar("max G", window_name, 0, 255, onTrackbar)
    cv2.createTrackbar("min R", window_name, 0, 255, onTrackbar)
    cv2.createTrackbar("max R", window_name, 0, 255, onTrackbar)

    # dictionary with ranges
    ranges_pcss = {"b": {"min": 100, "max": 256},
                   "g": {"min": 100, "max": 256},
                   "r": {"min": 100, "max": 256},
                   }

    # cycle for continuously capture the image
    while True:

        # read the image
        _, image = capture.read()
        _, image_segmenter = capture.read()
        # cv2.imshow(window_regular, image)

        # ESC to close
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

        min_b_pcss = cv2.getTrackbarPos("min B", window_name)
        max_b_pcss = cv2.getTrackbarPos("max B", window_name)
        min_g_pcss = cv2.getTrackbarPos("min G", window_name)
        max_g_pcss = cv2.getTrackbarPos("max G", window_name)
        min_r_pcss = cv2.getTrackbarPos("min R", window_name)
        max_r_pcss = cv2.getTrackbarPos("max R", window_name)

        ranges_pcss["b"]["min"] = min_b_pcss
        ranges_pcss["b"]["max"] = max_b_pcss
        ranges_pcss["g"]["min"] = min_g_pcss
        ranges_pcss["g"]["max"] = max_g_pcss
        ranges_pcss["r"]["min"] = min_r_pcss
        ranges_pcss["r"]["max"] = max_r_pcss

        mins_pcss = np.array([ranges_pcss['b']['min'], ranges_pcss['g']['min'], ranges_pcss['r']['min']])
        maxs_pcss = np.array([ranges_pcss['b']['max'], ranges_pcss['g']['max'], ranges_pcss['r']['max']])

        image_segmenter = cv2.inRange(image, mins_pcss, maxs_pcss)
        cv2.imshow(window_name, image_segmenter)

    # save json file
    file_name = 'limits.json'
    with open(file_name, 'w') as file_handle:
        print('writing dictionary d to file ' + file_name)
        json.dump(d, file_handle)  # d is the dicionary

    capture.release()  # free the webcam for other use
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()