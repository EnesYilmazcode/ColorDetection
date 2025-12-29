import numpy as np
import cv2


def get_limits(color):

    c = np.uint8([[color]])
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)
    h = int(hsvC[0, 0, 0])

    # Clip hue to [0,179] and build uint8 arrays for cv2.inRange
    lowerLimit = np.array([max(h - 10, 0), 100, 100], dtype=np.uint8)
    upperLimit = np.array([min(h + 10, 179), 255, 255], dtype=np.uint8)

    return lowerLimit, upperLimit