import metaros
from metaros import Publisher
from metaros.messages import Image as SensorImage
import cv2
import numpy as np
import time

# Initialize publisher on the /camera_video topic
pub = Publisher('/camera_video', SensorImage)

# Open the video capture (use 0 for the default camera)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Publish frames in a loop
try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        # Convert frame to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Create and populate the SensorImage message
        msg = SensorImage()
        msg.height = frame_rgb.shape[0]
        msg.width = frame_rgb.shape[1]
        msg.encoding = "rgb8"
        msg.is_bigendian = False
        msg.step = 3 * msg.width
        msg.data = np.array(frame_rgb).flatten()

        # Publish the message
        pub.publish(msg)
        print("Published frame.")

        # Optional delay to control frame rate (e.g., 30 FPS)
        time.sleep(1/30)
except KeyboardInterrupt:
    print("Shutting down publisher...")
finally:
    cap.release()
    print("Camera released.")
