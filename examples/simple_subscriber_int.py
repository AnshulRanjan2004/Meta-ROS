import time

from metaros import Subscriber
from metaros.messages import Int


def callback(msg: Int):
    print("Received message:\n", msg)


def main():
    sub = Subscriber("/test_topic", Int, callback)  # noqa: F841
    print("Subscribing to /test_topic")
    print("Press Ctrl+C to stop.")
    while True:
        time.sleep(1)


if __name__ == "__main__":
    main()
