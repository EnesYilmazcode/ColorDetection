import cv2
from PIL import Image
from utils import get_limits

targetColor = [0, 0, 0]  # BGR format
currentFrame = None

# Mouse callback function
def mouse_callback(event, x, y, flags, param):
    global targetColor, currentFrame
    if event == cv2.EVENT_LBUTTONDOWN and currentFrame is not None:
        targetColor = currentFrame[y, x].tolist()
        print(f"New target color selected: BGR{targetColor}")

cap = cv2.VideoCapture(0)

cv2.namedWindow('frame')
cv2.setMouseCallback('frame', mouse_callback)

while True:

    ret, frame = cap.read()
    if not ret:
        continue
    
    currentFrame = frame.copy()

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