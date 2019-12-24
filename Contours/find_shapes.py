import argparse
import imutils
import cv2
import numpy as np


def main():
    find_shapes()

def find_shapes():
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", help="path to the image file")
    args = vars(ap.parse_args())

    # load the image
    image = cv2.imread(args["image"])

    lower=np.array([0,0,0])
    upper=np.array([15,15,15])
    shapeMask=cv2.inRange(image,lower,upper)

    cnts=cv2.findContours(shapeMask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts=imutils.grab_contours(cnts)
    print(f' i found {len(cnts)} black shapes')
    cv2.imshow('mask',shapeMask)

    for c in cnts:
        cv2.drawContours(image,[c],-1,(0,255,0),2)
        cv2.imshow('image',image)
        cv2.waitKey(0)


if __name__ == '__main__':
    main()