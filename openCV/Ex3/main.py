#!/usr/bin/python3

import argparse
import cv2

# Global variables
window_name = 'image_negative'
image = None
image_gray = None
image_negative = None


def onTrackbar(threshold):
    global image_negative
    _, image_negative = cv2.threshold(image_gray, threshold, threshold, cv2.THRESH_BINARY)
    cv2.imshow("image_negative", image_negative)


def main():
    global image_gray  # use global var
    global image
    global image_negative

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', type=str, required=True, help='Full path to image file.')
    args = vars(parser.parse_args())

    image = cv2.imread(args['image'], cv2.IMREAD_COLOR)  # Load an image
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # convert bgr to gray image (single channel)
    _, image_negative = cv2.threshold(image_gray, 0, 0, cv2.THRESH_BINARY)

    cv2.namedWindow(window_name)
    cv2.createTrackbar("N", "image_negative", 0, 255, onTrackbar)

    # cv2.imshow("image", image)
    # cv2.imshow("image_gray", image_gray)
    cv2.imshow("image_negative", image_negative)

    cv2.waitKey(0)


if __name__ == '__main__':
    main()
