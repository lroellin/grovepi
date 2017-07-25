import grove_128_64_oled as oled
from features import time, weather_outdoor
from time import sleep

oled.init()  # initialze SEEED OLED display

oled.clearDisplay()  # clear the screen and set start position to top left corner
oled.setNormalDisplay()  # Set display to normal mode (i.e non-inverse mode)
oled.setPageMode()  # Set addressing mode to Page Mode

OLED_COLUMNS = 16
OLED_ROWS = 8

while True:
    time.print_time()
    weather_outdoor.print_weather(OLED_COLUMNS, OLED_ROWS)
    sleep(0.1)
