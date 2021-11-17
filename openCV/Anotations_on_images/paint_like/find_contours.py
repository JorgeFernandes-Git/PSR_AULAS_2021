#!/usr/bin/python3

import cv2
import numpy as np
import pickle

shapes = []  # all shapes in the drawing
path = []  # current shape


def mouse_points(event, x, y, flags, params):
    global path
    if event == cv2.EVENT_LBUTTONDOWN:
        path.append([x, y])
        print(path)


def main():
    global path

    image = cv2.imread("pinguim.png")
    cv2.namedWindow("image")
    cv2.setMouseCallback("image", mouse_points)

    while True:

        # for point in path:
        #     cv2.circle(image, point, 7, (0, 255, 0), cv2.FILLED)

        # create shapes for paint
        pts = np.array(path, np.int32).reshape((-1, 1, 2))  # needed for use of polylines
        image = cv2.polylines(image, [pts], True, (0, 255, 0), 2)

        # show the image
        cv2.imshow("image", image)

        # ESC to close
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

        # save the shape
        if k == ord("s"):
            color_number = int(input("Color: "))
            shapes.append([path, color_number])
            print("Shapes: ", len(shapes))
            path = []

        if k == ord("l"):
            with open("shapes", "wb") as file:
                pickle.dump(shapes, file)
                print("File saved as shapes.")
            break

    # close
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
