#!/usr/bin/env python3
import cv2 as cv

kernel_size = 81

img = cv.imread('person.png')
mask = cv.imread('mask_big.png')
mask_inv = cv.bitwise_not(mask)

f = cv.medianBlur(img, kernel_size)
img_bg = cv.bitwise_and(f, mask_inv)
img_fg = cv.bitwise_or(img, mask)
res = cv.add(img_fg, img_bg)

mask = cv.imwrite('res.png', res)
