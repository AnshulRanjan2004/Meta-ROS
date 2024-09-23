from metaros import Publisher
from metaros.messages import Image as SensorImage
import urllib2  # for downloading an example image
from PIL import Image
import numpy as np

pub = Publisher('/image', SensorImage, queue_size=10)
im = Image.open(urllib2.urlopen('https://cdn.sstatic.net/Sites/stackoverflow/Img/apple-touch-icon.png'))
im = im.convert('RGB')
msg = SensorImage()
msg.header.stamp = rospy.Time.now()
msg.height = im.height
msg.width = im.width
msg.encoding = "rgb8"
msg.is_bigendian = False
msg.step = 3 * im.width
msg.data = np.array(im).tobytes()
pub.publish(msg)