from PIL import ImageFont
import os
assets = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'assets')
small = ImageFont.truetype(os.path.join(assets, 'Roboto-Regular.ttf'), 18)
large = ImageFont.truetype(os.path.join(assets, 'Roboto-Regular.ttf'), 36)
tiny = ImageFont.truetype(os.path.join(assets, 'Roboto-Regular.ttf'), 12)
sayings = ImageFont.truetype(os.path.join(assets, 'IndieFlower-Regular.ttf'), 24)
sig = ImageFont.truetype(os.path.join(assets, 'Roboto-Italic.ttf'), 24)

