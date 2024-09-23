import metaros
from metaros import Publisher
from metaros.messages import Image as SensorImage 
from PIL import Image as PILImage
import numpy as np

pub = Publisher('/image', SensorImage)
image_path = 'examples/robot_image.jpg'
im = PILImage.open(image_path)
im = im.convert('RGB')
msg = SensorImage()
msg.height = im.height
msg.width = im.width
msg.encoding = "rgb8"
msg.is_bigendian = False
msg.step = 3 * im.width
msg.data = np.array(im).flatten()
pub.publish(msg)