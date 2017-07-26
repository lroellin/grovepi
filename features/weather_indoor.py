import grovepi
import screen
import weather_support
import math

DHT_SENSOR_PIN = 4  # D4
DHT_SENSOR_TYPE = 0  # blue
ROW = 7


def print_weather():
    [temperature, humidity] = grovepi.dht(DHT_SENSOR_PIN, DHT_SENSOR_TYPE)
    if not math.isnan(temperature) and not math.isnan(humidity):
        screen.print_string(0, ROW, weather_support.format_inaccurate_temperature(temperature) + "C")
        format_humidity = weather_support.format_humidity(humidity)
        screen.print_string(screen.OLED_COLUMNS - len(format_humidity), ROW, format_humidity)
