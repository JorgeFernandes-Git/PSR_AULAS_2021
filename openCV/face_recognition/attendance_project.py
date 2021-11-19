#!/usr/bin/python3

import cv2
import numpy as np
import face_recognition


def main():
    # load image
    img_original = face_recognition.load_image_file("ElonMusk1.jpeg")
    img_original = cv2.cvtColor(img_original, cv2.COLOR_BGR2RGB)

    # image to test landmarks
    img_test = face_recognition.load_image_file("bill_gates.jpg")
    img_test = cv2.cvtColor(img_test, cv2.COLOR_BGR2RGB)


if __name__ == '__main__':
    main()
