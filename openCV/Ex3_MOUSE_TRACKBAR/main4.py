#!/usr/bin/python3

import argparse
import cv2
import numpy as np


def onTrackbar(threshold):
    print(threshold)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', type=str, required=True, help='Full path to image file.')
    args = vars(parser.parse_args())

    image = cv2.imread(args['image'], cv2.IMREAD_COLOR)  # Load an image
    image_b, image_g, image_r = cv2.split(image)  # split the image

    ranges = {"b": {"min": 100, "max": 256},
              "g": {"min": 100, "max": 256},
              "r": {"min": 100, "max": 256},
              }

    mins = np.array([ranges['b']['min'], ranges['g']['min'], ranges['r']['min']])
    maxs = np.array([ranges['b']['max'], ranges['g']['max'], ranges['r']['max']])
    image_process = cv2.inRange(image, mins, maxs)
    cv2.imshow("image_process", image_process)
    # image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    cv2.namedWindow('image_process')
    cv2.createTrackbar("min B", "image_process", 0, 255, onTrackbar)
    cv2.createTrackbar("max B", "image_process", 0, 255, onTrackbar)
    cv2.createTrackbar("min G", "image_process", 0, 255, onTrackbar)
    cv2.createTrackbar("max G", "image_process", 0, 255, onTrackbar)
    cv2.createTrackbar("min R", "image_process", 0, 255, onTrackbar)
    cv2.createTrackbar("max R", "image_process", 0, 255, onTrackbar)

    while True:
        # close windows on ESC
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

        min_b = cv2.getTrackbarPos("min B", "image_negative")
        max_b = cv2.getTrackbarPos("max B", "image_negative")
        min_g = cv2.getTrackbarPos("min G", "image_negative")
        max_g = cv2.getTrackbarPos("max G", "image_negative")
        min_r = cv2.getTrackbarPos("min R", "image_negative")
        max_r = cv2.getTrackbarPos("max R", "image_negative")

        ranges = {"b": {"min": min_b, "max": max_b},
                  "g": {"min": min_g, "max": max_g},
                  "r": {"min": min_r, "max": max_r},
                  }

        mins = np.array([ranges['b']['min'], ranges['g']['min'], ranges['r']['min']])
        maxs = np.array([ranges['b']['max'], ranges['g']['max'], ranges['r']['max']])

        image_process = cv2.inRange(image, mins, maxs)
        cv2.imshow("image_process", image_process)


if __name__ == '__main__':
    main()
