# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 18:02:05 2020

@author: Shaurya Prakash
 
"""
import cv2 as cv
 
image = cv.imread("C:/Users/HP/Pictures/sigCapture-1.jpeg",cv.WINDOW_NORMAL)

  

cv.imshow('image',image)

cv.waitKey(0)

cv.destroyAllWindows()


