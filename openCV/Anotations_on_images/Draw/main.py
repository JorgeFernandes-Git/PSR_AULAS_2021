#!/usr/bin/python3

import cv2 as cv


def main():
    image = cv.imread("/home/jorge/Desktop/UA/PSR/Pycharm_EX/psr_21-22/Parte05/images_recog/atlascar.png")

    # positions are in (x, y) format

    # image dimensions and channels
    height, width, channels = image.shape
    print(height, width, channels)

    # circle characteristics
    position = (int(width/2), int(height/2))
    radius = 50
    color = (255, 255, 255)
    thickness = 5
    # make the circle
    cv.circle(image, position, radius, color, thickness)

    # text characteristics
    text = "PSR 2021"
    font_txt = cv.FONT_HERSHEY_SIMPLEX
    pos = (25, 50)
    font_scale = 1
    color_txt = (255, 255, 255)
    thickness_txt = 2
    # write the text
    cv.putText(image, text, pos, font_txt, font_scale, color_txt, thickness_txt)

    # show the image in the end
    cv.imshow("image", image)

    cv.waitKey(0)


if __name__ == '__main__':
    main()
