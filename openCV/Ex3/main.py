#!/usr/bin/python3
import argparse
import cv2

# Global variables
window_name = 'image'
image_gray = None


def onTrackbar(threshold):
    # Add code here to threshold image_gray and show image in window
    print(threshold)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', type=str, required=True, help='Full path to image file.')
    args = vars(parser.parse_args())

    image = cv2.imread(args['image'], cv2.IMREAD_COLOR)  # Load an image
    global image_gray  # use global var
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # convert bgr to gray image (single channel)
    cv2.namedWindow(window_name)

    # add code to create the trackbar ...
    cv2.createTrackbar("B", "image", 0, 255, onTrackbar)
    cv2.createTrackbar("G", "image", 0, 255, onTrackbar)
    cv2.createTrackbar("R", "image", 0, 255, onTrackbar)

    cv2.imshow("image", image)

    cv2.waitKey(0)


if __name__ == '__main__':
    main()
