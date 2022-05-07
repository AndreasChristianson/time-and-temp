import grequests
import fonts
import layout
from layout import forecast_left


urls = [
    'https://api.weather.gov/gridpoints/DMX/69,49/forecast',
    'https://api.weather.gov/stations/KDSM/observations/latest',
]

rs = (grequests.get(u) for u in urls)


def draw_weather(draw):
    forecast, current = get_data()
    print(current["properties"])
    print_forecast(forecast, draw)
    print_current(current, draw)


def get_data():
    rs = (grequests.get(u) for u in urls)
    responses = grequests.map(rs)
    return map(lambda response: response.json(), responses)


def print_forecast(forecast, draw):
    print_period(forecast["properties"]["periods"][0], draw, 0)
    print_period(forecast["properties"]["periods"][1], draw, 42)
    print_period(forecast["properties"]["periods"][2], draw, 84)


def print_period(period, draw, top):
    draw.text((forecast_left, top), period["name"]+": "+str(period["temperature"])+"°"+period["temperatureUnit"], font=fonts.small)
    draw.text((forecast_left, top+18), period["shortForecast"], font=fonts.tiny)


def print_current(current, draw):
    temp = current["properties"]["temperature"]["value"]
    textDescription = current["properties"]["textDescription"]
    draw.text((10,66), str(round(c_to_f(temp), 1))+"°F", font=fonts.large)
    draw.text((10,66+36), textDescription, font=fonts.tiny)
    


def c_to_f(c):
    return c * 1.8 + 32
