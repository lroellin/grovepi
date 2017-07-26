import screen
import datetime
import pytz

ROW = 3


def print_time():
    now = get_time()
    time_string = now.strftime("%H:%M:%S")
    screen.print_string(0, ROW, time_string)
    date_string = now.strftime("%d.%-m")
    screen.print_string(screen.OLED_COLUMNS - len(date_string) - 1, ROW, date_string)


def get_time():
    return datetime.datetime.now(pytz.timezone('Europe/Zurich'))
