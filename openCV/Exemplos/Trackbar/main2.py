#!/usr/bin/python3

import numpy as np
import cv2 as cv


def nothing(x):
    print(x)


def main():
    # Create a black image, a window
    cv.namedWindow('image')

    cv.createTrackbar('CP', 'image', 10, 400, nothing)

    switch = 'color/gray'
    cv.createTrackbar(switch, 'image', 0, 1, nothing)

    while True:
        img = cv.imread("/home/jorge/Desktop/UA/PSR/Pycharm_EX/psr_21-22/Parte05/images_recog/atlas2000_e_atlasmv.png")
        pos = cv.getTrackbarPos('CP', 'image')
        font = cv.FONT_HERSHEY_SIMPLEX
        cv.putText(img, str(pos), (50, 150), font, 3, (255, 255, 255), 10)

        k = cv.waitKey(1) & 0xFF
        if k == 27:
            break

        s = cv.getTrackbarPos(switch, 'image')

        if s == 0:
            pass
        else:
            img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        img = cv.imshow('image', img)


cv.destroyAllWindows()

if __name__ == '__main__':
    main()
