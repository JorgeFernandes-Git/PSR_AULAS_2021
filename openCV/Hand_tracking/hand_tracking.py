#!/usr/bin/python3

import cv2
import mediapipe as mp
import time


def main():
    cap = cv2.VideoCapture(0)

    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands()  # press ctrl to enter function
    mp_draw = mp.solutions.drawing_utils

    prev_time = 0
    cur_time = 0

    while True:
        success, img = cap.read()
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(img_rgb)
        # print(results)

        if results.multi_hand_landmarks:
            for hand_lms in results.multi_hand_landmarks:
                for id, lm in enumerate(hand_lms.landmark):
                    # print(id, lm)
                    h, w, c = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    # print(id, cx, cy)
                    if id == 0:  # id of the landmark (21 in total)
                        cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
                mp_draw.draw_landmarks(img, hand_lms,
                                       mp_hands.HAND_CONNECTIONS)  # hand_lms is single hand

        # number of frames
        cur_time = time.time()
        fps = 1 / (cur_time - prev_time)
        prev_time = cur_time

        # put text on frame
        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 0), 3)

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