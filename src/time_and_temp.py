import requests
import datetime
from PIL import Image,ImageDraw,ImageFont
from draw_time import draw_time
import draw_weather

def get_image():
  image = Image.new( '1', (400, 300), 255)
  draw = ImageDraw.Draw(image)

  draw_time(draw)
  # weather.draw_weather(draw)

  return image