import logging
import epd4in2
import time_and_temp

logger = logging.getLogger('update_eink')
logger.setLevel(logging.DEBUG)
image = time_and_temp.get_image()
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
    