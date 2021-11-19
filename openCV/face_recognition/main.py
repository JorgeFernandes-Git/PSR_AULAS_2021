#!/usr/bin/python3

import cv2
import numpy as np
import face_recognition


def main():
    # load image
    img_original = face_recognition.load_image_file("elon_musk1.jpeg")
    img_original = cv2.cvtColor(img_original, cv2.COLOR_BGR2RGB)

    # image to test landmarks
    img_test = face_recognition.load_image_file("bill_gates.jpg")
    img_test = cv2.cvtColor(img_test, cv2.COLOR_BGR2RGB)

    # detect the face
    face_loc = face_recognition.face_locations(img_original)[0]
    encode_original = face_recognition.face_encodings(img_original)[0]
    # make the rectangle
    cv2.rectangle(img_original, (face_loc[3], face_loc[0]), (face_loc[1], face_loc[2]), (255, 0, 255), 2)

    # detect the face test
    face_loc_test = face_recognition.face_locations(img_test)[0]
    encode_test = face_recognition.face_encodings(img_test)[0]
    # make the rectangle
    cv2.rectangle(img_test, (face_loc_test[3], face_loc_test[0]),
                  (face_loc_test[1], face_loc_test[2]), (255, 0, 255), 2)

    # compare the encodings (original vs test)
    results = face_recognition.compare_faces([encode_original], encode_test)    # true or false
    face_dist = face_recognition.face_distance([encode_original], encode_test)  # number bitween 0 and 1
    print(results, face_dist)
    cv2.putText(img_test, f'{results} {round(face_dist[0], 2)}',
                (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)  # display the results o the test image

    # show the images
    cv2.imshow("Original", img_original)
    cv2.imshow("Test", img_test)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()
