from features import time, weather_outdoor, weather_indoor, screen
from time import sleep

screen.init()

while True:
    time.print_time()
    weather_outdoor.print_weather()
    weather_indoor.print_weather()
    sleep(0.1)
