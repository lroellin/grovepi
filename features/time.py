import screen
import datetime
import pytz

ROW = 3


def print_time():
    now = get_time()
    colon = ":" if now.time().second % 2 == 0 else " "
    time_string = now.strftime("%H" + colon + "%M" + colon + "%S")
    screen.print_string(0, ROW, time_string)
    date_string = now.strftime("%d.%-m")
    screen.print_string(screen.OLED_COLUMNS - len(date_string) - 1, ROW, date_string)


def get_time():
    return datetime.datetime.now(pytz.timezone('Europe/Zurich'))


def format_timestring(hour, minute, second):
    return str(hour) + ":" + str(minute) + ":" + str(second)
