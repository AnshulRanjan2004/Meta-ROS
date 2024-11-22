import metaros
from metaros import Subscriber
from metaros.messages import Image as SensorImage
import numpy as np
import cv2
import torch
import time

# Load the YOLOv5 model using PyTorch Hub
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

def callback(msg: SensorImage):
    # Convert the flattened image data back to a 3D array (height x width x channels)
    image_data = np.frombuffer(msg.data, dtype=np.uint8).reshape((msg.height, msg.width, 3))
    
    # Convert image to BGR format for YOLOv5
    img_bgr = cv2.cvtColor(image_data, cv2.COLOR_RGB2BGR)
    
    # Perform object detection using YOLOv5
    results = model(img_bgr)
    
    # Render results on the image
    img_with_boxes = results.render()[0]  # Get the image with bounding boxes as a numpy array
    
    # Display the processed frame
    cv2.imshow("YOLOv5 Detection Stream", img_with_boxes)
    
    # Exit the stream gracefully when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Stream stopped by user.")
        cv2.destroyAllWindows()
        exit()

def main():
    # Create a subscriber to the /camera_video topic
    sub = Subscriber("/camera_video", SensorImage, callback)
    print("Subscribed to /camera_video")
    print("Press 'q' to stop the stream.")
    
    # Keep the subscriber running until manually stopped
    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        print("Shutting down subscriber...")
    finally:
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
