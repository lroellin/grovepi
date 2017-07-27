import grove_128_64_oled as oled

OLED_COLUMNS = 16
OLED_ROWS = 8


def print_custom_character(character):
    for i in range(8):
        oled.sendData(character[i])


def print_16x16_icon(column_start, row_start, parts):
    oled.setTextXY(column_start, row_start)
    print_custom_character(parts[0])
    oled.setTextXY(column_start, row_start + 1)
    print_custom_character(parts[1])
    oled.setTextXY(column_start + 1, row_start)
    print_custom_character(parts[2])
    oled.setTextXY(column_start + 1, row_start + 1)
    print_custom_character(parts[3])


def print_string(x, y, string):
    oled.setTextXY(x, y)
    oled.putString(string)


def init():
    oled.init()  # initialize SEEED OLED display

    oled.clearDisplay()  # clear the screen and set start position to top left corner
    oled.setNormalDisplay()  # Set display to normal mode (i.e non-inverse mode)
    oled.setPageMode()  # Set addressing mode to Page Mode


def clear_display():
    for x in range(OLED_COLUMNS):
        for y in range(OLED_ROWS):
            print_string(x, y, " ")


def align_right(string):
    length = len(string)
    return OLED_COLUMNS - length


def align_center(string):
    return align_center_by_length(len(string))


def align_center_by_length(length):
    center = (OLED_COLUMNS - length) / 2
    if length % 2 != 0:
        center += 1  # bias to the right
    return int(center)
