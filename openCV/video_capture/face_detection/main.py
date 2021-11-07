#!/usr/bin/python3

import cv2 as cv


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
        for (x, y, w, h) in faces:
            cv.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Display
        cv.imshow(window_name, image)

        # ESC to close
        k = cv.waitKey(30) & 0xFF
        if k == 27:
            break

    capture.release()  # free the webcam for other uses if needed
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
