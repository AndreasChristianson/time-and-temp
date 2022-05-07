import requests
from datetime import datetime
from PIL import ImageFont
import os
assets = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'assets')
font = ImageFont.truetype(os.path.join(assets, 'skyhook.ttf'), 36)

def draw_time(draw):
  draw.text((10, 100), datetime.now().strftime("%m/%d/%Y, %H:%M"), font = font)