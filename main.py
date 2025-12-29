import cv2

from utils import get_limits


yellow = [0, 255, 255]
cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)



    lower_limit, upper_limit = get_limits(yellow)

    mask = cv2.inRange(hsvImage, lower_limit, upper_limit)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()