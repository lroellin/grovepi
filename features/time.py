import grove_128_64_oled as oled
import datetime
import pytz

def print_time():
    now = get_time()
    time_string = now.strftime("%H:%M:%S")
    oled.setTextXY(4, 3)
    oled.putString(time_string)


def get_time():
    return datetime.datetime.now(pytz.timezone('Europe/Zurich'))


def format_timestring(hour, minute, second):
    return str(hour) + ":" + str(minute) + ":" + str(second)