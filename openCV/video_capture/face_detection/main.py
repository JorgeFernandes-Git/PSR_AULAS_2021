#!/usr/bin/python3

import cv2 as cv


def onTrackbar(threshold):
    print("Selected threshold " + str(threshold) + " for limit")


def main():
    # flags for select the modes
    gray_bool = False
    mask_bool = False

    # initial setup
    capture = cv.VideoCapture(0)  # connect to webcam

    # create the window
    window_name = 'Video_Capture'
    cv.namedWindow(window_name, cv.WINDOW_AUTOSIZE)

    # create trackbars
    cv.createTrackbar("min", window_name, 0, 255, onTrackbar)
    cv.createTrackbar("max", window_name, 0, 255, onTrackbar)

    # cycle for continuously capture the image
    while True:

        # read the image
        _, image = capture.read()

        if not gray_bool:
            # show the image
            cv.imshow(window_name, image)

        if gray_bool:
            # convert to gray scale
            gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
            cv.imshow(window_name, gray)

        if mask_bool:
            min_gray = cv.getTrackbarPos("min", window_name)
            max_gray = cv.getTrackbarPos("max", window_name)
            gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
            mask = cv.inRange(gray, min_gray, max_gray)
            cv.imshow(window_name, mask)

        # ESC to close
        k = cv.waitKey(1) & 0xFF
        if k == 27:
            break

        if k == ord("g"):
            gray_bool = True
            mask_bool = False
        if k == ord("r"):
            gray_bool = False
            mask_bool = False
        if k == ord("m"):
            mask_bool = True
            gray_bool = False

    capture.release()  # free the webcam for other use
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
