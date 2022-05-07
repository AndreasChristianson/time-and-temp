import requests
import datetime
from PIL import Image,ImageDraw,ImageFont

def get_image():
  image = Image.new( '1', (400, 300), 255)
  draw = ImageDraw.Draw(image)

  draw_time(draw)
  draw_weather(draw)

  return image