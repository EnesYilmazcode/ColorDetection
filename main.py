import cv2
from PIL import Image

from utils import get_limits


selected_color = [0, 255, 255]  # Default to yellow in BGR colorspace

def mouse_callback(event, x, y, flags, param):
    global selected_color
    if event == cv2.EVENT_LBUTTONDOWN:
        # Get the frame from param
        frame = param
        # Get the BGR color at the clicked position
        selected_color = frame[y, x].tolist()
        print(f"Selected color (BGR): {selected_color}")

cap = cv2.VideoCapture(0)
cv2.namedWindow('frame')

while True:
    ret, frame = cap.read()
    
    if not ret:
        break
    
    cv2.setMouseCallback('frame', mouse_callback, frame)
    
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit = get_limits(color=selected_color)

    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

    mask_ = Image.fromarray(mask)

    bbox = mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox

        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)
    
    # Display the current selected color in the corner
    color_text = f"Color (BGR): {selected_color}"
    cv2.putText(frame, color_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    cv2.putText(frame, "Click to select color, 'q' to quit", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()
