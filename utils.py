import numpy as np
import cv2


def get_limits(color):

    c = np.uint8([[color]])
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)
    h = int(hsvC[0, 0, 0])

    # Balanced ranges - not too strict, not too loose
    lowerLimit = np.array([max(h - 15, 0), 70, 70], dtype=np.uint8)
    upperLimit = np.array([min(h + 15, 179), 255, 255], dtype=np.uint8)

    return lowerLimit, upperLimit