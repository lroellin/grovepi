import icons
import screen
import symbols
import weather_support
import requests
import requests_cache
import sys

OWM_RATE_LIMIT_SECONDS = 600
OWM_RATE_LIMIT_SECONDS_BUFFER = 10
OWM_CITY_ID = "7286859"
OWM_BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
OWM_API_KEY = sys.argv[1]

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
    screen.print_16x16_icon(screen.align_center_by_length(2), 6, icon_parts)


def print_weather():
    try:
        weather = get_weather()

        screen.print_string(0, ROW, weather_support.format_accurate_temperature(weather.temp) + symbols.THERMOMETER)

        min_max = weather_support.format_inaccurate_temperature(
            weather.temp_min) + "-" + weather_support.format_inaccurate_temperature(weather.temp_max)
        screen.print_string(screen.align_center(min_max), 0, min_max)

        humidity = weather_support.format_humidity(weather.humidity)
        screen.print_string(screen.align_right(humidity), ROW, humidity)



        print_weather_icon(weather.icon)
    except IOError as error:
        screen.print_string(0, ROW, "!" * screen.OLED_COLUMNS)
        print(str(error.message))


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
