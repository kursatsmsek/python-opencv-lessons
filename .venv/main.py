import cv2

img = cv2.imread('resources/kursatsimsek-pp.jpeg')

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('Profile Photo', imgGray)

cv2.waitKey(0)