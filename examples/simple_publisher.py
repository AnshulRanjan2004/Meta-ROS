import time

from metaros import Publisher
from metaros.messages import String


def main():
    pub = Publisher("/test_topic", String)
    print("Publishing to /test_topic")
    print("Press Ctrl+C to stop.")
    while True:
        pub.publish(String("Hello World!"))
        time.sleep(1)


if __name__ == "__main__":
    main()
