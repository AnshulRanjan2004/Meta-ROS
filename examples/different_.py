import time

from metaros import Subscriber
from metaros.messages import String


def callback(msg: String):
    print("Received message:\n", msg)


def main():
    sub = Subscriber(topic="/test_topic", message_class=String, callback_handle=callback, ip="192.168.135.134", port=5556)
    print("Subscribing to /test_topic")
    print("Press Ctrl+C to stop.")
    while True:
        time.sleep(5)


if __name__ == "__main__":
    main()