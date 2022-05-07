top_left_border = 175
margin = 5
bottom = (18+12+margin)*3+margin


def draw_layout(draw):
  # draw.line((top_left_border,0, top_left_border,122))
  draw.line((0,bottom,400,bottom))

def draw_centered(draw, text, font, top, left, container_width):
  w, h = draw.textsize(text, font=font)
  start = max(container_width/2-w/2,0)
  draw.text((left+start ,top), text, font=font)