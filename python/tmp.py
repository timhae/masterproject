#!/usr/bin/env python3
import cv2 as cv

mask = cv.imread('mask_big.png', cv.IMREAD_GRAYSCALE)
cv.imwrite('mask_big2.png', mask, [cv.IMWRITE_PNG_BILEVEL, 1])
