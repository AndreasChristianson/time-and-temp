import grequests

urls = [
    'https://api.weather.gov/gridpoints/DMX/69,49/forecast',
    'https://api.weather.gov/stations/KDSM/observations/latest',
]

rs = (grequests.get(u) for u in urls)

def draw_weather(draw):
  forecast,current = get_data()
  print(forecast)


def get_data():
  rs = (grequests.get(u) for u in urls)
  return grequests.map(rs)
