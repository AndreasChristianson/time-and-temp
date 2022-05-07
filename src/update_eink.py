import logging
import epd4in2
import time_and_temp

def update_eink():
  try:
    image = time_and_temp.get_image()
    epd = epd4in2.EPD()
    logging.debug("init...")
    epd.init()
    logging.debug("clear...")
    epd.Clear()
    logging.debug("update...")
    epd.display(epd.getbuffer(image))
    logging.debug("sleep...")
    epd.sleep()
    logging.debug("done")
    
  except IOError as e:
    logging.warning(e)