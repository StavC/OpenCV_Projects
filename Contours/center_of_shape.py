import argparse
import imutils
import cv2


def main():
    center_of_shape()

def center_of_shape():
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True,
                    help="path to the input image")
    args = vars(ap.parse_args())

    image=cv2.imread(args['image'])
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    blurred=cv2.GaussianBlur(gray,(5,5),0)
    thresh=cv2.threshold(blurred,60,255,cv2.THRESH_BINARY)[1]

    cv2.imshow('img',thresh)
    cv2.waitKey(0)

    cnts=cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts=imutils.grab_contours(cnts)


    for c in cnts:
        M=cv2.moments(c)
        cX = int(M["m10"] / (M["m00"]+ 1e-7)) # like in the docs
        cY = int(M["m01"] / (M["m00"]+ 1e-7))

        cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
        cv2.circle(image, (cX, cY), 7, (255, 255, 255), -1)
        cv2.putText(image, "center", (cX - 20, cY - 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        cv2.imshow("Image", image)
        cv2.waitKey(0)

def find_shapes():
    pass

if __name__ == '__main__':
    main()