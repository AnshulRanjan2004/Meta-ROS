import time
import numpy as np
from metaros import Subscriber
from PIL import Image as PILImage
from metaros.messages import Image as SensorImage

def callback(msg: SensorImage):
    print("Received image message:")
    print(f"Width: {msg.width}, Height: {msg.height}, Encoding: {msg.encoding}")
    image_data = np.frombuffer(msg.data, dtype=np.uint8).reshape((msg.height, msg.width, 3))
    img = PILImage.fromarray(image_data)
    img.save("examples/received_image.jpg")

def main():
    sub = Subscriber("/image", SensorImage, callback)
    print("Subscribing to /image")
    print("Press Ctrl+C to stop.")
    while True:
        time.sleep(5)

if __name__ == "__main__":
    main()
