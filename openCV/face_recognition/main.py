#!/usr/bin/python3

import cv2
import numpy as np
import face_recognition


def main():
    # load image
    img_elon = face_recognition.load_image_file("ElonMusk1.jpeg")
    img_elon = cv2.cvtColor(img_elon, cv2.COLOR_BGR2RGB)

    # image to test landmarks
    img_test = face_recognition.load_image_file("ElonMusk2.jpg")
    img_test = cv2.cvtColor(img_test, cv2.COLOR_BGR2RGB)

    # detect the face
    face_loc = face_recognition.face_locations(img_elon)[0]
    encode_elon = face_recognition.face_encodings(img_elon)[0]
    # make the rectangle
    cv2.rectangle(img_elon, (face_loc[3], face_loc[0]), (face_loc[1], face_loc[2]), (255, 0, 255), 2)

    # detect the face test
    face_loc_test = face_recognition.face_locations(img_test)[0]
    encode_test = face_recognition.face_encodings(img_test)[0]
    # make the rectangle
    cv2.rectangle(img_test, (face_loc_test[3], face_loc_test[0]), (face_loc_test[1], face_loc_test[2]), (255, 0, 255), 2)

    # compare the encodings
    results = face_recognition.compare_faces([encode_elon], encode_test)
    face_dist = face_recognition.face_distance([encode_elon], encode_test)
    print(results)
    print(face_dist)

    # show the images
    cv2.imshow("Elon Musk", img_elon)
    cv2.imshow("Elon Test", img_test)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()
