import requests
import datetime
from PIL import Image,ImageDraw,ImageFont

def get_image():
  image = Image.new( '1', (400, 300), 255)

  return image