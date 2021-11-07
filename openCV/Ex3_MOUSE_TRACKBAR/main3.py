#!/usr/bin/python3

import argparse
import cv2


def onTrackbar(threshold):
    pass


def mousePosition(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        print("X = " + str(x) + ", " + "Y = " + str(y))
        # print('({}, {})'.format(x, y))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', type=str, required=True, help='Full path to image file.')
    args = vars(parser.parse_args())

    image = cv2.imread(args['image'], cv2.IMREAD_COLOR)  # Load an image
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # convert bgr to gray image (single channel)

    cv2.namedWindow('image_negative')
    cv2.createTrackbar("Contrast", "image_negative", 0, 255, onTrackbar)
    cv2.createTrackbar("Brightness", "image_negative", 0, 255, onTrackbar)
    cv2.setMouseCallback("image_negative", mousePosition)

    while True:

        # close windows on ESC
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

        contrast = cv2.getTrackbarPos("Contrast", "image_negative")
        brightness = cv2.getTrackbarPos("Brightness", "image_negative")

        _, image_negative = cv2.threshold(image_gray, contrast, brightness, cv2.THRESH_BINARY)
        cv2.imshow("image_negative", image_negative)


cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
