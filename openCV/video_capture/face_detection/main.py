#!/usr/bin/python3

import cv2 as cv
import numpy as np


def onTrackbar(threshold):
    # print("Selected threshold " + str(threshold) + " for limit")
    pass


def main():
    # load the cascade
    face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
    # initial setup
    capture = cv.VideoCapture(0)  # connect to webcam

    # create the window
    window_name = 'Video_Capture'
    cv.namedWindow(window_name, cv.WINDOW_AUTOSIZE)

    # cycle for continuously capture the image
    while True:
        # read the image
        _, image = capture.read()
        # Convert to grayscale
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        # Detect the faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        # Draw the rectangle around each face
        try:
            for (x, y, w, h) in faces:
                cv.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
                shapes = np.zeros_like(image, np.uint8)
                cv.rectangle(shapes, (x, y), (x + w, y + h), (0, 255, 0), cv.FILLED)
                # mask the rectangle in the image with transparency
                final_image = image.copy()
                alpha = 0.7
                mask = shapes.astype(bool)
                final_image[mask] = cv.addWeighted(image, alpha, shapes, 1 - alpha, 0)[mask]
            # Display
            cv.imshow(window_name, final_image)
        except:
            cv.imshow(window_name, image)

        # ESC to close
        k = cv.waitKey(30) & 0xFF
        if k == 27:
            break

    capture.release()  # free the webcam for other uses if needed
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
