#!/usr/bin/python3
import argparse
import time
import numpy as np

import cv2
import readchar


def main():
    # path to image
    image_1 = "/home/jorge/Desktop/UA/PSR/Pycharm_EX/psr_21-22/Parte05/images/atlascar.png"
    image1 = cv2.imread(image_1, cv2.IMREAD_COLOR)  # Load an image
    image_gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)  # convert to gray scale

    # process the image
    _, image_negative = cv2.threshold(image_gray, 128, 255, cv2.THRESH_BINARY)

    # show the images in 3 windows
    cv2.imshow("original", image1)
    cv2.imshow("gray", image_gray)
    cv2.imshow("negative", image_negative)

    cv2.waitKey(8000)  # wait for 8 seconds


if __name__ == '__main__':
    main()
