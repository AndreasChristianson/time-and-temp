import datetime
from PIL import Image,ImageDraw
from draw_time import draw_time
from draw_weather import draw_weather
from layout import draw_layout
from love import draw_love

def get_image():
  image = Image.new( '1', (400, 300), 255)
  draw = ImageDraw.Draw(image)

  draw_time(draw)
  draw_weather(draw)

  draw_love(draw)
  draw_layout(draw)

  return image