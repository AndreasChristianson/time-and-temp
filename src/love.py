from math import ceil
import random
import layout
import fonts
import csv

top = layout.bottom+layout.margin*2+24
with open('love.csv', newline='') as csvfile:
  reader = csv.reader(csvfile)
  love = list(reader)

def draw_love(draw):
    saying = random.choice(love)
    width = 400-layout.margin*2
    first, second, third, fourth = split_phrase(saying[0])
    layout.draw_centered(
        draw, first, fonts.sayings, top, layout.margin, width)
    layout.draw_centered(
        draw, second, fonts.sayings, top+24, layout.margin, width)
    layout.draw_centered(
        draw, third, fonts.sayings, top+48, layout.margin, width)
    layout.draw_centered(
        draw, fourth, fonts.sayings, top+72, layout.margin, width)
    layout.draw_centered(
        draw, "--" + saying[1], fonts.sig, top+120, 200, 100)

def split_phrase(phrase):
  words = phrase.split()

  chunked_list = list()
  print(words)
  chunk_size = max(ceil(len(words)/4),5)
  print(chunk_size)

  for i in range(0, len(words), chunk_size):
    chunked_list.append(" ".join(words[i:i+chunk_size]))
  print(chunked_list)
  chunked_list += [""] * (4 - len(chunked_list))
  print(chunked_list)
  
  return chunked_list