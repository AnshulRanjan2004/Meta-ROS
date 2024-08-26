import time

from metaros import Subscriber
from metaros.messages import Float


def callback(msg: Float):
    print("Received message:\n", msg)


def main():
    sub = Subscriber("/test_topic", Float, callback)  # noqa: F841
    print("Subscribing to /test_topic")
    print("Press Ctrl+C to stop.")
    while True:
        time.sleep(5)


if __name__ == "__main__":
    main()
