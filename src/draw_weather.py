from requests import Session
import fonts
import layout


urls = [
    'https://api.weather.gov/gridpoints/DMX/69,49/forecast',
    'https://api.weather.gov/stations/KDSM/observations/latest',
]

rs = (grequests.get(u) for u in urls)


def draw_weather(draw):
    forecast, current = get_data()
    print_forecast(forecast, draw)
    print_current(current, draw)


def get_data():
    session = Session()
    forecast = session.get(urls[0])
    current = session.get(urls[1])
    return forecast.json(), current.json()


def print_forecast(forecast, draw):
    print_period(forecast["properties"]["periods"][0], draw, 0)
    print_period(forecast["properties"]["periods"]
                 [1], draw, 18+12+layout.margin)
    print_period(forecast["properties"]["periods"]
                 [2], draw, (18+12+layout.margin)*2)


def print_period(period, draw, top):
    layout.draw_centered(draw, period["name"]+": "+str(
        period["temperature"])+"°"+period["temperatureUnit"], fonts.small, top, layout.top_left_border+layout.margin, 400-layout.top_left_border-layout.margin*2)
    layout.draw_centered(draw, period["shortForecast"], fonts.tiny, top+18,
                         layout.top_left_border+layout.margin, 400-layout.top_left_border-layout.margin*2)


def print_current(current, draw):
    temp = current["properties"]["temperature"]["value"]
    layout.draw_centered(draw, str(round(c_to_f(temp), 1))+"°F", fonts.large,
                         36+12+layout.margin, layout.margin, layout.top_left_border-layout.margin)
    textDescription = current["properties"]["textDescription"]
    layout.draw_centered(draw, textDescription, fonts.tiny, 36+12 +
                         layout.margin+36, layout.margin, layout.top_left_border-layout.margin)


def c_to_f(c):
    return c * 1.8 + 32
