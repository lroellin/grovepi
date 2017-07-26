import icons
import screen
import weather_support
import requests
import requests_cache
import json
import os

OWM_RATE_LIMIT_SECONDS = 600
OWM_RATE_LIMIT_SECONDS_BUFFER = 10
OWM_CITY_ID = "7286859"
OWM_BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
OWM_API_KEY = os.environ["OWM_API_KEY"]

ROW = 0


class Weather(object):
    def __init__(self, temp, temp_min, temp_max, humidity, icon):
        self.temp = temp
        self.temp_min = temp_min
        self.temp_max = temp_max
        self.humidity = humidity
        self.icon = icon


def print_weather_icon(icon):
    icon_parts = icons.icon_mapping[icon[:2]]
    screen.print_16x16_icon(icon_parts)


def print_weather():
    try:
        weather = get_weather()

        screen.print_string(0, ROW, weather_support.format_accurate_temperature(weather.temp))

        min_max = weather_support.format_inaccurate_temperature(
            weather.temp_min) + "/" + weather_support.format_inaccurate_temperature(weather.temp_max)
        screen.print_string(screen.OLED_COLUMNS - 1 - len(min_max), 0, min_max)

        screen.print_string(6, ROW, weather_support.format_humidity(weather.humidity))

        print_weather_icon(weather.icon)
    except IOError as error:
        screen.print_string(0, ROW, "!" * screen.OLED_COLUMNS)
        print str(error)


def get_weather():
    requests_cache.install_cache('openweathermap', expire_after=OWM_RATE_LIMIT_SECONDS + OWM_RATE_LIMIT_SECONDS_BUFFER)
    parameters = {'id': OWM_CITY_ID, 'APPID': OWM_API_KEY,
                  'units': 'metric'}
    request = requests.get(OWM_BASE_URL, params=parameters)
    if request.status_code == 200:
        # print "Cache: " + str(request.from_cache)
        # print json.dumps(request.json(), indent=2)
        # print request.url
        return Weather(
            request.json()['main']['temp'],
            request.json()['main']['temp_min'],
            request.json()['main']['temp_max'],
            request.json()['main']['humidity'],
            request.json()['weather'][0]['icon']
        )
    else:
        raise IOError("Return code not 200")
