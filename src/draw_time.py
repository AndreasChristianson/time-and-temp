from datetime import datetime
from PIL import ImageFont
import os
import fonts

def draw_time(draw):
  draw.text((10, 0), datetime.now().strftime("%I:%M%PM"), font = fonts.large)
  draw.text((10, 36), datetime.now().strftime("%a %b %d"), font = fonts.tiny)
