import argparse
import imutils
import cv2
import numpy as np


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="Path to the input image")
    ap.add_argument("-m", "--method", required=True, help="Sorting method")
    args = vars(ap.parse_args())


    image = cv2.imread(args["image"])
    accumEdged = np.zeros(image.shape[:2], dtype="uint8")

    for chan in cv2.split(image):
        chan = cv2.medianBlur(chan, 11)
        edged = cv2.Canny(chan, 50, 200)
        accumEdged = cv2.bitwise_or(accumEdged, edged)

    cv2.imshow("Edge Map", accumEdged)
    cv2.waitKey(0)

    cnts = cv2.findContours(accumEdged.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:5]
    orig = image.copy()

    for (i, c) in enumerate(cnts):
        orig = draw_contour(orig, c, i)

    cv2.imshow("Unsorted", orig)

    (cnts, boundingBoxes) = sorting_contours(cnts, method=args["method"])

    for (i, c) in enumerate(cnts):
        draw_contour(image, c, i)

    cv2.imshow("Sorted", image)
    cv2.waitKey(0)


def sorting_contours(cnts,method='left_to_right'):

    reverse=False #ascending order
    i=0 # x-axis is the start

    if method=='right_to_left' or method=='bottom_to_top':
        reverse=True #decending
    if method=='top_to_bottom' or method== 'bottom_to_top':
        i=1 # y-axis is the start

    boundingBoxes=[cv2.boundingRect(c) for c in cnts]
    (cnts, boundingBoxes) = zip(*sorted(zip(cnts, boundingBoxes),
                                key=lambda b: b[1][i], reverse=reverse))

    # return the list of sorted contours and bounding boxes
    return (cnts, boundingBoxes)

def draw_contour(image,c,i):
    M=cv2.moments(c)
    cX=int(M['m10']/M['m00'])
    cY=int(M['m01']/M['m00'])

    cv2.putText(image,f'{i+1}',(cX-20,cY),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
    return image

if __name__ == '__main__':
    main()