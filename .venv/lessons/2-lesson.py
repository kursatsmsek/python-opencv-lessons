import cv2

cap = cv2.VideoCapture("../resources/soccer-match.mp4")
#cap = cv2.VideoCapture(0) // webcam

while True:
    ret, frame = cap.read()
    #frame = frame[0:1200, 50:690] // cropped
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break