import argparse
import imutils
import cv2
import numpy as np


def main():
    extreme_points()

def extreme_points():


    # load the image
    image = cv2.imread('hand1.jpg')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    thresh = cv2.threshold(gray, 155, 255, cv2.THRESH_BINARY_INV)[1]
    thresh = cv2.erode(thresh, None, iterations=5)
    cv2.imshow('t',thresh)

    thresh = cv2.dilate(thresh, None, iterations=10)
    cv2.imshow('t2', thresh)
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    c = max(cnts, key=cv2.contourArea)

    extLeft = tuple(c[c[:, :, 0].argmin()][0])
    extRight = tuple(c[c[:, :, 0].argmax()][0])
    extTop = tuple(c[c[:, :, 1].argmin()][0])
    extBot = tuple(c[c[:, :, 1].argmax()][0])
    
    cv2.drawContours(image, [c], -1, (0, 255, 255), 2)
    cv2.circle(image, extLeft, 8, (0, 0, 255), -1)
    cv2.circle(image, extRight, 8, (0, 255, 0), -1)
    cv2.circle(image, extTop, 8, (255, 0, 0), -1)
    cv2.circle(image, extBot, 8, (255, 255, 0), -1)

    # show the output image
    cv2.imshow("Image", image)
    cv2.waitKey(0)



if __name__ == '__main__':
    main()