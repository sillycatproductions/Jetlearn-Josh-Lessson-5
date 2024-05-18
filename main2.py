import cv2
import numpy as np
import random

img = cv2.imread('circleeee.jpg')

params = cv2.SimpleBlobDetector_Params()

params.filterByArea = True
params.minArea = 100

params.filterByCircularity = True
params.minCircularity = 0.8

params.filterByConvexity = True
params.minConvexity = 0.9

params.filterByInertia = True
params.minInertiaRatio = 0.01

detector = cv2.SimpleBlobDetector_create(params)

keypoints = detector.detect(img)
blank = np.zeros((1,1))
blobs = cv2.drawKeypoints(img, keypoints, blank, (random.randint(100,255),random.randint(100,255),random.randint(100,255)), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

numblo = len(keypoints)
text = 'Circles in image: '+ str(numblo)

cv2.putText(blobs, text, (20,550), cv2.FONT_HERSHEY_COMPLEX, 1, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), 2)

cv2.imshow('njjuhnkhjunkjhuk', blobs)
cv2.waitKey(0)
cv2.destroyAllWindows()