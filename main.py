import cv2
from PIL import Image
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

    mask_ = Image.fromarray(mask)
    bbox = mask_.getbbox()

    if bbox:
        x1, y1, x2, y2 = bbox
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)




    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()