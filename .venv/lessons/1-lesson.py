import cv2

img = cv2.imread('../resources/kursatsimsek-pp.jpeg')

img = cv2.resize(img, (600, 600))
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (15, 15), 0)
imgCanny = cv2.Canny(imgBlur, 10, 10)
imgCropped = img[0:600, 0:300]

cv2.imshow('Gray Photo', imgGray)
cv2.imshow('Canny Photo', imgCanny)
cv2.imshow('Blur Photo', imgBlur)
cv2.imshow('Cropped Photo', imgCropped)

cv2.waitKey(0)