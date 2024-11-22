import time
import numpy as np
import cv2
import torch
from metaros import Subscriber
from PIL import Image as PILImage
from metaros.messages import Image as SensorImage

# Load the YOLOv5 model using PyTorch Hub (assuming internet access is available)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

def callback(msg: SensorImage):
    print("Received image message:")
    print(f"Width: {msg.width}, Height: {msg.height}, Encoding: {msg.encoding}")
    
    # Convert the flattened image data back to a 3D array (height x width x channels)
    image_data = np.frombuffer(msg.data, dtype=np.uint8).reshape((msg.height, msg.width, 3))
    
    # Convert the NumPy array to a PIL image and save it
    img = PILImage.fromarray(image_data)
    img.save("examples/received_camera_image.jpg")
    print("Image saved as 'examples/received_camera_image.jpg'.")
    
    # Convert the NumPy array to the format expected by YOLOv5 (BGR format for OpenCV)
    img_bgr = cv2.cvtColor(image_data, cv2.COLOR_RGB2BGR)
    
    # Perform object detection using the YOLOv5 model
    results = model(img_bgr)
    
    # Print detected objects
    print("Detected objects:")
    results.print()  # This will print the detected objects in the console
    
    # Optionally, save the image with bounding boxes drawn
    results.save("examples/")  # This saves the result with bounding boxes in the default folder
    
    # The saved image with bounding boxes will be available in 'examples/' folder

def main():
    # Create a subscriber to the /camera_image topic
    sub = Subscriber("/camera_image", SensorImage, callback,ip="192.168.135.134", port=5556)
    print("Subscribed to /camera_image")
    print("Press Ctrl+C to stop.")
    
    # Keep the subscriber running until manually stopped
    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        print("Shutting down subscriber...")

if __name__ == "__main__":
    main()