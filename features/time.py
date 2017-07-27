import screen
import datetime
import pytz

ROW = 2


def print_time():
    now = get_time()
    time_string = now.strftime("%H:%M:%S")
    screen.print_string(0, ROW, time_string)
    date_string = now.strftime("%a %d.%m.%Y")
    screen.print_string(screen.align_right(date_string), ROW + 1, date_string)


def get_time():

    return datetime.datetime.now(pytz.timezone('Europe/Zurich'))
