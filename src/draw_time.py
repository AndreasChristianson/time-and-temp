from datetime import datetime
from PIL import ImageFont
import os
import fonts
import layout

def draw_time(draw):
  layout.draw_centered(draw,datetime.now().strftime("%I:%M%P"),fonts.large,0,layout.margin,layout.top_left_border-layout.margin)
  layout.draw_centered(draw,datetime.now().strftime("%a %b %d"),fonts.tiny,36,layout.margin,layout.top_left_border-layout.margin)
