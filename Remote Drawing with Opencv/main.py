import cv2
import numpy as np

canvas = np.ones((480, 640, 3), dtype=np.uint8) * 255
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([40, 255, 255])
prev_center = None
while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_frame, lower_yellow, upper_yellow)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) > 0:
        max_contour = max(contours, key=cv2.contourArea)
        if cv2.contourArea(max_contour) > 0:
            moment = cv2.moments(max_contour)
            center = (int(moment["m10"] / moment["m00"]), int(moment["m01"] / moment["m00"]))
            size = cv2.contourArea(max_contour)
            if prev_center is not None:               
                cv2.line(canvas, prev_center, center, (0, 0, 0), 2)           
            prev_center = center
            x, y, w, h = cv2.boundingRect(max_contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)    
    output_frame = np.concatenate((frame, canvas), axis=1)
    cv2.imshow("Webcam", output_frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
