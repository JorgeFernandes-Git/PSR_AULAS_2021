#!/usr/bin/python3

import cv2
import time
import numpy as np
import hand_tracking_class as htm
import math


def main():
    # camera param
    w_cam, h_cam = 640, 480

    cap = cv2.VideoCapture(0)

    # measure fps
    prev_time = 0

    # initial bar value
    bar_length = 400

    # hand object
    detector = htm.HandDetector()

    while True:
        success, img = cap.read()

        # detect hands and put dots and lines
        img = detector.find_hands(img, draw=False)
        lm_list = detector.find_position(img, draw=False)

        if not len(lm_list) == 0:
            # find thumb and index fingertips (see hand_landmarks.png)
            # print(lm_list[4], lm_list[8])

            # find center of the fingers by landmarks
            x1, y1 = lm_list[4][1], lm_list[4][2]
            x2, y2 = lm_list[8][1], lm_list[8][2]
            cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

            # draw a circle in the center
            # cv2.circle(img, (x1, y1), 10, (255, 0, 255), cv2.FILLED)  # thumb circle
            # cv2.circle(img, (x2, y2), 10, (255, 0, 255), cv2.FILLED)  # index circle
            # cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)  # line between circles
            # cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)  # circle in center of line

            # length of the line
            length = math.hypot(x2 - x1, y2 - y1)
            print(length)

            # hand range 25 to 200
            bar_length = np.interp(length, [25, 200], [50, 590])
            print(int(length), bar_length)

            # circle line color
            if length < 25:
                pass
                # cv2.circle(img, (cx, cy), 10, (0, 255, 0), cv2.FILLED)  # circle in center of line

            # draw bar
            cv2.rectangle(img, (50, 420), (int(bar_length), 450), (255, 0, 0), cv2.FILLED)
            # cv2.rectangle(img, (50, 150), (85, 400), (0, 255, 0), 3)

        else:
            cv2.putText(img, f'No hand detected', (50, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

        # number of frames
        cur_time = time.time()
        fps = 1 / (cur_time - prev_time)
        prev_time = cur_time

        # put text on frame (frame/seconds)
        cv2.putText(img, f'FPS: {str(int(fps))}', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

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
