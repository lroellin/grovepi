#!/usr/bin/python

from features import time, weather_outdoor, weather_indoor, screen
from time import sleep

RESET_FREQUENCY = 1000  # cycles
screen.init()

counter = 0
while True:
    # start_time = timeit.default_timer()
    if counter >= RESET_FREQUENCY:
        screen.clear_display()
        counter = 0
    weather_outdoor.print_weather()
    time.print_time()
    weather_indoor.print_weather()
    counter += 1
    # elapsed = timeit.default_timer() - start_time
    sleep(0.1)
