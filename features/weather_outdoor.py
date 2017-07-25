import requests
import requests_cache
import json
import grove_128_64_oled as oled
import icons

OWM_RATE_LIMIT_SECONDS = 600
OWM_RATE_LIMIT_SECONDS_BUFFER = 10
OWM_CITY_ID = "7286859"
OWM_BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
OWM_API_KEY = "0509248a42ba828d7d2c4d2077269d0b"


class Weather(object):
    def __init__(self, temp, temp_min, temp_max, humidity):
        self.temp = temp
        self.temp_min = temp_min
        self.temp_max = temp_max
        self.humidity = humidity


def print_custom_character(character):
    for i in range(8):
        oled.sendData(character[i])


def print_16x16_icon(parts):
    COLUMN_START = 6
    ROW_START = 4

    oled.setTextXY(COLUMN_START, ROW_START)
    print_custom_character(parts[0])
    oled.setTextXY(COLUMN_START, ROW_START + 1)
    print_custom_character(parts[1])
    oled.setTextXY(COLUMN_START + 1, ROW_START)
    print_custom_character(parts[2])
    oled.setTextXY(COLUMN_START + 1, ROW_START + 1)
    print_custom_character(parts[3])


def print_weather_icon(weather):
    print_16x16_icon(icons.cloud_with_cloud_and_snow_parts)


def print_weather(display_width, display_height):
    weather = get_weather()

    oled.setTextXY(0, 0)
    oled.putString(format_main_temperature(weather.temp))

    min_max = format_minmax_temperature(weather.temp_min) + "/" + format_minmax_temperature(weather.temp_max)
    oled.setTextXY(display_width - 1 - len(min_max), 0)
    oled.putString(min_max)

    oled.setTextXY(0, display_height - 1)
    oled.putString(str(weather.humidity) + "%")

    print_weather_icon(weather)


def format_main_temperature(temp):
    return "{:.1f}C".format(temp)

def format_minmax_temperature(temp):
    return "{:.0f}".format(temp)


def get_weather():
    requests_cache.install_cache('openweathermap', expire_after=OWM_RATE_LIMIT_SECONDS + OWM_RATE_LIMIT_SECONDS_BUFFER)
    parameters = {'id': OWM_CITY_ID, 'APPID': OWM_API_KEY,
                  'units': 'metric'}
    request = requests.get(OWM_BASE_URL, params=parameters)
    # print "Cache: " + str(request.from_cache)
    # print json.dumps(request.json(), indent=2)
    return Weather(
        request.json()['main']['temp'],
        request.json()['main']['temp_min'],
        request.json()['main']['temp_max'],
        request.json()['main']['humidity'],
    )
