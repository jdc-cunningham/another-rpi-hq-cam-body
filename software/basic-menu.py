#!/usr/bin/env -S python

import cv2
import numpy as np
import logging
from pynput import mouse

img = np.zeros((480, 640, 3), dtype=np.uint8) 
img.fill(155) # to white

window_name = "Resizable Window"
width = 640
height = 480
font = cv2.FONT_HERSHEY_SIMPLEX

logging.basicConfig(
  filename='/home/pi/app.log',  # Name of the log file
  level=logging.INFO,   # The minimum level of messages to log (INFO and above)
  format='%(asctime)s:%(levelname)s:%(message)s' # Format of each log message
)

logging.info("start")

# listen for mouse input
def on_click(x, y, button, pressed):
  # print(button, pressed, listener)
  logging.info("clicked")
  # cv2.putText(img, f'{x},{y}', (0, 0), font, 4, (0, 255, 0), 2, cv2.LINE_AA)
 
listener = mouse.Listener(on_click=on_click)
listener.start()

# cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
# cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
# cv2.imshow(window_name, img)

while True:
  try:
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow(window_name, img)
    cv2.waitKey(33)
  except KeyboardInterrupt:
    break

cv2.destroyAllWindows()
