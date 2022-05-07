import logging
import epd4in2
import time_and_temp

def update_eink():
  try:
    image = time_and_temp.get_image()
    epd = epd4in2.EPD()
    logging.debug("init...")
    epd.init()
    logging.debug("get frame...")
    frame = epd.get_frame_buffer(image)
    logging.debug("update...")
    epd.display_frame(frame)
    logging.debug("sleep...")
    epd.sleep()
    logging.debug("done")
    
  except IOError as e:
    logging.warning(e)