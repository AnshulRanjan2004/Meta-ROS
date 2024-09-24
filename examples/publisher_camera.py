import metaros
from metaros import Publisher
from metaros.messages import Image as SensorImage
import cv2
import numpy as np

pub = Publisher('/camera_image', SensorImage)

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

ret, frame = cap.read()

if not ret:
    print("Error: Could not read frame.")
    cap.release()
    exit()

frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

msg = SensorImage()
msg.height = frame_rgb.shape[0]
msg.width = frame_rgb.shape[1]
msg.encoding = "rgb8"
msg.is_bigendian = False
msg.step = 3 * msg.width
msg.data = np.array(frame_rgb).flatten()

pub.publish(msg)
cap.release()

print("Image captured and published successfully.")