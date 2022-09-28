import cv2
import numpy as np

img = cv2.imread("../DATA/dog_backpack.jpg")

def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x, y), 100, (0, 0, 255), -1)
        
        
cv2.namedWindow(winname='dog_backpack')
cv2.setMouseCallback('dog_backpack', draw_circle)

while True:
    cv2.imshow('dog_backpack',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
