import numpy as np
import cv2
import argparse
import imutils
from RotateObjectsCorrectly.Rotate import RotateCorrectly
def main():
    #ap = argparse.ArgumentParser()
    #ap.add_argument("-i", "--image", required=True,
                    #help="path to the image file")
    #args = vars(ap.parse_args())

    #image=cv2.imread(args['image'])
    image=cv2.imread('watch.jpg',cv2.IMREAD_COLOR)
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(3,3),0)
    edged=cv2.Canny(gray,20,100)

    cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    if len(cnts) > 0:
        # grab the largest contour, then draw a mask for the pill
        c = max(cnts, key=cv2.contourArea)
        mask = np.zeros(gray.shape, dtype="uint8")
        cv2.drawContours(mask, [c], -1, 255, -1)

        # compute its bounding box of pill, then extract the ROI,
        # and apply the mask
        (x, y, w, h) = cv2.boundingRect(c)
        imageROI = image[y:y + h, x:x + w]
        maskROI = mask[y:y + h, x:x + w]
        imageROI = cv2.bitwise_and(imageROI, imageROI,
                                   mask=maskROI)

        for angle in np.arange(0, 360, 15):
            image_center = tuple(np.array(image.shape[1::-1]) / 2)
            rot_mat=cv2.getRotationMatrix2D(image_center,angle,1.0)
            rotated =  cv2.warpAffine(image, rot_mat, image.shape[1::-1])
            cv2.imshow("Rotated (Problematic)", rotated)
            cv2.waitKey(0)


        for angle in np.arange(0, 360, 15):
            rotated = RotateCorrectly(imageROI, angle)
            cv2.imshow("Rotated (Correct)", rotated)
            cv2.waitKey(0)


















if __name__ == '__main__':
    main()