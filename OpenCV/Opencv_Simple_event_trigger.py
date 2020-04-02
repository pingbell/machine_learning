# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 14:10:25 2020

@author: HP
"""
import cv2 as cv
import numpy as np

image = cv.imread("C:/Users/HP/Pictures/sigCapture-1.jpeg",cv.WINDOW_NORMAL)
#define named window
cv.namedWindow("image")
#Event callback function 
def mouse_event(event, x, y, flags, param) :
    if ( event == cv.EVENT_LBUTTONDBLCLK ) :
        print("Left click")
 
# call callback function
cv.setMouseCallback("image"  , mouse_event)  