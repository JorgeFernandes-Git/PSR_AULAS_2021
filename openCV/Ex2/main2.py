#!/usr/bin/python3

import argparse
import time
import numpy as np
import cv2
import readchar


def main():
    # path to image
    image_1 = "/home/jorge/Desktop/UA/PSR/Pycharm_EX/psr_21-22/Parte05/images/atlas2000_e_atlasmv.png"
    image1 = cv2.imread(image_1, cv2.IMREAD_COLOR)  # Load an image
    image_b, image_g, image_r = cv2.split(image1)  # split the image

    ranges = {"b": {"min": 0, "max": 60},
              "g": {"min": 80, "max": 256},
              "r": {"min": 0, "max": 60},
              }

    mins = np.array([ranges['b']['min'], ranges['g']['min'], ranges['r']['min']])
    maxs = np.array([ranges['b']['max'], ranges['g']['max'], ranges['r']['max']])
    image_process = cv2.inRange(image1, mins, maxs)
    image_hsv = cv2.cvtColor(image1, cv2.COLOR_BGR2HSV)

    # show the images
    cv2.namedWindow("image1", cv2.WINDOW_NORMAL)
    cv2.imshow("image1", image1)
    cv2.imshow("image_process", image_process)
    cv2.imshow("image_hsv", image_hsv)

    cv2.waitKey(0)  # wait for 8 seconds
    cv2.destroyAllWindows() # Esc to close


if __name__ == '__main__':
    main()
