import screen
import datetime
import pytz

ROW = 2


def print_time():
    now = get_time()
    time_string = now.strftime("%H:%M:%S")
    screen.print_string(0, ROW, time_string)
    date_string = now.strftime("%d.%m")
    screen.print_string(10, ROW, date_string)


def get_time():
    return datetime.datetime.now(pytz.timezone('Europe/Zurich'))


def format_timestring(hour, minute, second):
    return str(hour) + ":" + str(minute) + ":" + str(second)
