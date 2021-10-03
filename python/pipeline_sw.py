#!/usr/bin/env python3
import cv2 as cv

filter_names = ['median', 'gauss']
boolean_names = ['and', 'or']
kernel_sizes = [3, 41, 81]

for boolean_name in boolean_names:
    for filter_name in filter_names:
        for kernel_size in kernel_sizes:
            # load image and mask
            img = cv.imread('person.png')
            mask = cv.imread('mask_big.png')
            mask_inv = cv.bitwise_not(mask)

            # filter
            if filter_name == 'gauss':
                f = cv.GaussianBlur(img, (kernel_size, kernel_size), 0)
            elif filter_name == 'median':
                f = cv.medianBlur(img, kernel_size)

            # boolean
            img_bg = cv.bitwise_and(f, mask_inv)
            if boolean_name == 'and':
                img_fg = cv.bitwise_and(img, mask)
            elif boolean_name == 'or':
                img_fg = cv.bitwise_or(f, mask)

            # put it back together
            res = cv.add(img_fg, img_bg)

            cv.imwrite(f'{boolean_name}_{filter_name}_{kernel_size}.png', res)
