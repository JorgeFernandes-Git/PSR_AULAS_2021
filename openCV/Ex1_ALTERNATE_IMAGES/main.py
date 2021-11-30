#!/usr/bin/python3
import argparse
import time

import cv2
import readchar


def main():
    # parser = argparse.ArgumentParser(description="Open image in path")
    # parser.add_argument("-img", "--image", type=str, help="PATH TO IMAGE")
    # args = vars(parser.parse_args())
    # print(args)

    image_1 = "/home/jorge/Desktop/UA/PSR/Pycharm_EX/psr_21-22/Parte05/images_recog/atlascar.png"
    image_2 = "/home/jorge/Desktop/UA/PSR/Pycharm_EX/psr_21-22/Parte05/images_recog/atlascar2.png"
    image1 = cv2.imread(image_1, cv2.IMREAD_COLOR)  # Load an image
    image2 = cv2.imread(image_2, cv2.IMREAD_COLOR)

    # image1 = cv2.imread(args["image"], cv2.IMREAD_COLOR)  # Load an image

    while True:
        cv2.imshow('window1', image1)  # Display the image
        cv2.waitKey(1000)
        cv2.imshow('window1', image2)  # Display the image
        cv2.waitKey(1000)  # wait for a key press before proceeding in milliseconds
        # pressed_continue = readchar.readkey()
        # if pressed_continue:
        #     exit()


if __name__ == '__main__':
    main()
