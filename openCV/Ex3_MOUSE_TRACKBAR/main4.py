#!/usr/bin/python3

import argparse
import cv2
import numpy as np


def onTrackbar(threshold):
    print("Selected threshold " + str(threshold) + " for limit")


def main():
    # parse the argument
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', type=str, required=True, help='Full path to image file.')
    args = vars(parser.parse_args())

    # read the image original
    image = cv2.imread(args['image'], cv2.IMREAD_COLOR)  # Load an image
    cv2.imshow("original", image)

    # convert to gray scale
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("image_gray", image_gray)

    # convert to hsv
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    cv2.imshow("image_hsv", image_hsv)

    # dictionary with ranges
    ranges_pcss = {"b": {"min": 100, "max": 256},
                   "g": {"min": 100, "max": 256},
                   "r": {"min": 100, "max": 256},
                   }

    # create the trackbars
    cv2.namedWindow('image_process')
    cv2.createTrackbar("min B", "image_process", 0, 255, onTrackbar)
    cv2.createTrackbar("max B", "image_process", 0, 255, onTrackbar)
    cv2.createTrackbar("min G", "image_process", 0, 255, onTrackbar)
    cv2.createTrackbar("max G", "image_process", 0, 255, onTrackbar)
    cv2.createTrackbar("min R", "image_process", 0, 255, onTrackbar)
    cv2.createTrackbar("max R", "image_process", 0, 255, onTrackbar)

    # create the trackbars
    cv2.namedWindow('mask')
    cv2.createTrackbar("min", "mask", 0, 255, onTrackbar)
    cv2.createTrackbar("max", "mask", 0, 255, onTrackbar)

    # cycle for editing the images
    while True:
        # close windows on ESC
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

        min_b_pcss = cv2.getTrackbarPos("min B", "image_process")
        max_b_pcss = cv2.getTrackbarPos("max B", "image_process")
        min_g_pcss = cv2.getTrackbarPos("min G", "image_process")
        max_g_pcss = cv2.getTrackbarPos("max G", "image_process")
        min_r_pcss = cv2.getTrackbarPos("min R", "image_process")
        max_r_pcss = cv2.getTrackbarPos("max R", "image_process")

        ranges_pcss["b"]["min"] = min_b_pcss
        ranges_pcss["b"]["max"] = max_b_pcss
        ranges_pcss["g"]["min"] = min_g_pcss
        ranges_pcss["g"]["max"] = max_g_pcss
        ranges_pcss["r"]["min"] = min_r_pcss
        ranges_pcss["r"]["max"] = max_r_pcss

        mins_pcss = np.array([ranges_pcss['b']['min'], ranges_pcss['g']['min'], ranges_pcss['r']['min']])
        maxs_pcss = np.array([ranges_pcss['b']['max'], ranges_pcss['g']['max'], ranges_pcss['r']['max']])

        image_process = cv2.inRange(image, mins_pcss, maxs_pcss)
        cv2.imshow("image_process", image_process)

        # gray image --------------------------------------------------------
        min_gray = cv2.getTrackbarPos("min", "mask")
        max_gray = cv2.getTrackbarPos("max", "mask")

        mask = cv2.inRange(image_gray, min_gray, max_gray)
        cv2.imshow("mask", mask)


if __name__ == '__main__':
    main()
