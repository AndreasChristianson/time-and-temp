import fonts
import layout

import logging
import epd4in2

from PIL import Image,ImageDraw

def get_image():
  image = Image.new( '1', (400, 300), 255)
  draw = ImageDraw.Draw(image)

  layout.draw_centered(draw,"Happy Mother's Day!",fonts.large,100,0,400)


  return image

logger = logging.getLogger('one_time_message')
logger.setLevel(logging.DEBUG)
image = get_image()
epd = epd4in2.EPD()
logger.debug("init...")
epd.init()
logger.debug("get frame...")
frame = epd.get_frame_buffer(image)
logger.debug("update...")
epd.display_frame(frame)
logger.debug("sleep...")
epd.sleep()
logger.debug("done")

