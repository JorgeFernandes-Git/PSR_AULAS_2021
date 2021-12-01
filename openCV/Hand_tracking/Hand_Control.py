#!/usr/bin/python3

import cv2
import time
import numpy


def main():
    # camera param
    w_cam, h_cam = 640, 480

    cap = cv2.VideoCapture(0)

    # measure fps
    prev_time = 0

    while True:
        success, img = cap.read()

        # number of frames
        cur_time = time.time()
        fps = 1 / (cur_time - prev_time)
        prev_time = cur_time

        # put text on frame (frame/seconds)
        cv2.putText(img, f'FPS: {str(int(fps))}', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)

        # show the image
        cv2.imshow("Image", img)

        # ESC to close
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

    """
    finalization
    """
    cap.release()  # free the webcam for other uses if needed
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
