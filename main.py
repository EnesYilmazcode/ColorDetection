import cv2

from utils import get_limits


targetColor = [0, 0, 0]  # BGR format
cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()
    if not ret:
        continue

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)



    lower_limit, upper_limit = get_limits(targetColor)

    mask = cv2.inRange(hsvImage, lower_limit, upper_limit)

    # cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()