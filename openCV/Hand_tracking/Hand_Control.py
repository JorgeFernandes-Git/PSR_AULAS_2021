#!/usr/bin/python3

import cv2
import time
import numpy
import hand_tracking_class as htm


def main():
    # camera param
    w_cam, h_cam = 640, 480

    cap = cv2.VideoCapture(0)

    # measure fps
    prev_time = 0

    # hand object
    detector = htm.HandDetector()

    while True:
        success, img = cap.read()

        # detect hands and put dots and lines
        img = detector.find_hands(img)
        lm_list = detector.find_position(img, draw=False)

        if not len(lm_list) == 0:

            # find thumb and index fingertips (see hand_landmarks.png)
            print(lm_list[4], lm_list[8])

            # find center of the fingers by landmarks
            x1, y1 = lm_list[4][1], lm_list[4][2]
            x2, y2 = lm_list[8][1], lm_list[8][2]

            # draw a circle in the center
            cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)

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
