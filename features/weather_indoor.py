import grovepi
import screen
import symbols
import weather_support
import math

DHT_SENSOR_PIN = 4  # D4
DHT_SENSOR_TYPE = 0  # blue
ROW = 7


def print_weather():
    [temperature, humidity] = grovepi.dht(DHT_SENSOR_PIN, DHT_SENSOR_TYPE)
    if not math.isnan(temperature) and temperature >= 0 and not math.isnan(humidity):
        format_temperature = weather_support.format_inaccurate_temperature(temperature) + symbols.THERMOMETER
        screen.print_string(0, ROW, format_temperature)
        format_humidity = weather_support.format_humidity(humidity)
        screen.print_string(screen.align_right(format_humidity), ROW, format_humidity)
