import time

from metaros import Publisher
from metaros.messages import Int


def main():
    pub = Publisher("/test_topic", Int)
    print("Publishing to /test_topic")
    print("Press Ctrl+C to stop.")
    while True:
        pub.publish(Int(10))
        time.sleep(1)


if __name__ == "__main__":
    main()
