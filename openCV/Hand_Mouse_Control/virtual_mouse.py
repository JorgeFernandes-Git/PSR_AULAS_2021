#!/usr/bin/python3

import cv2
import numpy as np
import hand_tracking_module as htm
import time
import autopy


def main():
    # variables
    w_cam, h_cam = 640, 480
    frame_r = 100  # frame reduction
    smoothening = 7

    cap = cv2.VideoCapture(0)
    cap.set(3, w_cam)
    cap.set(4, h_cam)

    prev_time = 0
    prev_loc_x, prev_loc_y = 0, 0
    cur_loc_x, cur_loc_y = 0, 0

    detector = htm.HandDetector(max_hands=1)

    w_screen, h_screen = autopy.screen.size()
    # print(w_screen, h_screen)

    while True:
        # 1.FIND HAND LANDMARKS
        success, img = cap.read()
        img = detector.find_hands(img)
        lm_list, bbox = detector.find_position(img)
        # print(lm_list)

        # 2.GET THE TIP OF THE INDEX AND MIDDLE FINGER
        if not len(lm_list) == 0:
            x1, y1 = lm_list[8][1:]
            x2, y2 = lm_list[12][1:]
            # print(x1, y1, x2, y2)

            # 3.CHECK WHICH FINGERS ARE UP
            fingers = detector.finger_up()
            # print(fingers)
            cv2.rectangle(img, (frame_r, frame_r), (w_cam - frame_r, h_cam - frame_r), (255, 0, 255), 2)

            # 4.ONLY INDEX FINGER UP -> MOVING MODE
            if fingers[1] == 1 and fingers[2] == 0:
                # 5.CONVERT COORDINATES
                x3 = np.interp(x1, (frame_r, w_cam - frame_r), (0, w_screen))
                y3 = np.interp(y1, (frame_r, h_cam - frame_r-60), (0, h_screen))

                # 6.SMOOTHEN VALUES
                cur_loc_x = prev_loc_x + (x3 - prev_loc_x) / smoothening
                cur_loc_y = prev_loc_y + (y3 - prev_loc_y) / smoothening

                # 7.MOVE MOUSE
                try:
                    autopy.mouse.move(w_screen - cur_loc_x, cur_loc_y)
                except ValueError:
                    pass
                cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
                prev_loc_x, prev_loc_y = cur_loc_x, cur_loc_y

            # 8.BOTH INDEX AND MIDDLE FINGERS UP -> CLICKING MODE
            if fingers[1] == 1 and fingers[2] == 1:

                # 9.FIND DISTANCE BETWEEN FINGERS
                length, img, line_info = detector.find_distance(8, 12, img)
                # print(length)
                if length < 40:
                    cv2.circle(img, (line_info[4], line_info[5]), 15, (0, 255, 0), cv2.FILLED)

                    # 10.CLICK MOUSE IF DISTANCE SHORT
                    autopy.mouse.click()

        # 11.FRAME RATE
        # number of frames
        cur_time = time.time()
        fps = 1 / (cur_time - prev_time)
        prev_time = cur_time

        # put text on frame
        cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)

        # 12.DISPLAY
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
