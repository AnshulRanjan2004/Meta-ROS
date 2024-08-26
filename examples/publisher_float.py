import time

from metaros import Publisher
from metaros.messages import Float


def main():
    pub = Publisher("/test_topic", Float)
    print("Publishing to /test_topic")
    print("Press Ctrl+C to stop.")
    while True:
        pub.publish(Float(10.01))
        time.sleep(5)


if __name__ == "__main__":
    main()
