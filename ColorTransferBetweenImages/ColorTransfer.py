import numpy as np
import argparse
import cv2
import tkinter
import tkinter.filedialog
import os


def main():
    ### built by the algorithm from https://www.cs.tau.ac.il/~turkel/imagepapers/ColorTransfer.pdf
    '''
    ap = argparse.ArgumentParser()
    ap.add_argument("-s", "--source", help="path to the colors")
    ap.add_argument("-t", "--target", help="path to the targets")
    args = vars(ap.parse_args())

    source=cv2.imread(args['source'])
    target=cv2.imread(args['target'])
    '''

    source = cv2.imread('5.jpg', cv2.IMREAD_COLOR)
    target = cv2.imread('3.jpg', cv2.IMREAD_COLOR)



    target = cv2.resize(target, (800, 800))
    source = cv2.cvtColor(source, cv2.COLOR_BGR2LAB).astype('float32')
    target = cv2.cvtColor(target, cv2.COLOR_BGR2LAB).astype('float32')
    l_s, a_s, b_s = cv2.split(source)
    l_t, a_t, b_t = cv2.split(target)

    # 10 in the paper
    l = l_t - l_t.mean()
    a = a_t - a_t.mean()
    b = b_t - b_t.mean()
    # 11 in the paper
    l = l_t.std() / l_s.std() * l
    a = a_t.std() / a_s.std() * a
    b = b_t.std() / b_s.std() * b

    # the source mean

    l = l + l_s.mean()
    a = a + a_s.mean()
    b = b + b_s.mean()

    # cliping the outof bounds pixels
    l = np.clip(l, 0, 255)
    a = np.clip(a, 0, 255)
    b = np.clip(b, 0, 255)

    new_img = cv2.merge([l, a, b])
    new_img = cv2.cvtColor(new_img.astype('uint8'), cv2.COLOR_LAB2BGR)

    cv2.imshow('new', new_img)

    cv2.imwrite('new.jpg', new_img)
    cv2.waitKey(0)














if __name__ == '__main__':
    main()