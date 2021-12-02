#!/usr/bin/python3

import cv2
import mediapipe as mp
import time
import math
import numpy as np


class HandDetector():

    def __init__(self, mode=False, max_hands=2, detection_confidant=0, track_confidant=0.5):
        self.mode = mode
        self.max_hands = max_hands
        self.detection_confidant = detection_confidant
        self.track_confidant = track_confidant

        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(self.mode, self.max_hands,
                                         self.detection_confidant, self.track_confidant)  # press ctrl to enter function
        self.mp_draw = mp.solutions.drawing_utils
        self.tip_ids = [4, 8, 12, 16, 20]  # landmarks tips

    def find_hands(self, img, draw=True):
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(img_rgb)

        if self.results.multi_hand_landmarks:
            for hand_lms in self.results.multi_hand_landmarks:
                if draw:
                    self.mp_draw.draw_landmarks(img, hand_lms,
                                                self.mp_hands.HAND_CONNECTIONS)  # hand_lms is single hand
        return img

    def find_position(self, img, hand_num=0, draw=True):
        x_list = []
        y_list = []
        bbox = []
        self.lm_list = []

        if self.results.multi_hand_landmarks:
            my_hand = self.results.multi_hand_landmarks[hand_num]

            for id, lm in enumerate(my_hand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                x_list.append(cx)
                y_list.append(cy)
                self.lm_list.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy),
                               5, (255, 0, 255), cv2.FILLED)

            x_min, x_max = min(x_list), max(x_list)
            y_min, y_max = min(y_list), max(y_list)
            bbox = x_min, y_min, x_max, y_max

            # hand rectangle
            if draw:
                cv2.rectangle(img, (x_min - 20, y_min - 20), (x_max + 20, y_max + 20), (0, 255, 0, 2))

        return self.lm_list, bbox

    def finger_up(self):
        fingers = []
        # thumb
        if self.lm_list[self.tip_ids[0]][1] > self.lm_list[self.tip_ids[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        # fingers
        for id in range(1, 5):
            if self.lm_list[self.tip_ids[id]][2] < self.lm_list[self.tip_ids[id] - 1][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        # total fingers = fingers.count(1)
        return fingers

    def find_distance(self, p1, p2, img, draw=True, r=15, t=3):
        x1, y1 = self.lm_list[p1][1:]
        x2, y2 = self.lm_list[p2][1:]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        if draw:
            cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), t)
            cv2.circle(img, (x1, y1), r, (255, 0, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), r, (0, 0, 255), cv2.FILLED)
        length = math.hypot(x2 - x1, y2 - y1)  # find center of the line

        return length, img, [x1, y1, x2, y2, cx, cy]


def main():
    cap = cv2.VideoCapture(0)
    detector = HandDetector()

    prev_time = 0

    while True:
        success, img = cap.read()
        img = detector.find_hands(img)
        lm_list, bbox = detector.find_position(img)

        if not len(lm_list) == 0:
            print(lm_list[4])

        # number of frames
        cur_time = time.time()
        fps = 1 / (cur_time - prev_time)
        prev_time = cur_time

        # put text on frame
        cv2.putText(img, str(int(fps)), (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)

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
