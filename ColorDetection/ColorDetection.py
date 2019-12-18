import numpy as np
import argparse
import cv2


def main():

    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", help="path to the image")
    args = vars(ap.parse_args())

    # load the image
    image = cv2.imread(args["image"])
    image=cv2.resize(image,(500,500))


    boundaries = [
        ([100, 100, 150], [140, 140, 255]),
        ([60, 40, 0], [255, 200, 40]),
        ([0, 145, 40], [30, 255, 255]),
        ([70, 140, 50], [200, 255, 170])
    ]

    for (lower,upper) in boundaries:

        lower=np.array(lower,dtype='uint8')
        upper=np.array(upper,dtype='uint8')

        mask=cv2.inRange(image,lower,upper)
        output=cv2.bitwise_and(image,image,mask=mask)

        cv2.imshow('image',np.hstack([image,output]))
        cv2.waitKey(0)


if __name__ == '__main__':
    main()