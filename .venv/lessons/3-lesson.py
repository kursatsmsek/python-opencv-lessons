import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
img[:] = [186, 98, 200]

weight, height = img.shape[0], img.shape[0]
pts = [(90, 60), (180, 100), (400, 60)]

cv2.namedWindow("Image")

def drawImage(thickness):
    temp_img = np.zeros((512, 512, 3), np.uint8)
    temp_img[:] = [186, 98, 200]

    cv2.line(temp_img, (0, 0), (weight, height), (50, 255, 50), thickness)
    cv2.rectangle(temp_img, (256, 256), (weight, height), (50, 255, 50), thickness)
    cv2.circle(temp_img, (256, 256), 100, (50, 255, 50), thickness)
    cv2.polylines(temp_img, [np.array(pts)], True, (50, 255, 50), thickness)
    cv2.putText(temp_img, "Lesson - 3", (50, 500), cv2.FONT_HERSHEY_PLAIN, 2, (50, 255, 50), thickness)
    return temp_img

cv2.createTrackbar('Thickness', 'Image', 1, 15, lambda x: None)

while True:
    thickness = cv2.getTrackbarPos('Thickness', 'Image')
    if thickness == 0:
        thickness = 1

    img_with_shapes = drawImage(thickness)
    cv2.imshow("Image", img_with_shapes)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
