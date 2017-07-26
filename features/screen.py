import grove_128_64_oled as oled

OLED_COLUMNS = 16
OLED_ROWS = 8


def print_custom_character(character):
    for i in range(8):
        oled.sendData(character[i])


def print_16x16_icon(parts):
    COLUMN_START = 6
    ROW_START = 6

    oled.setTextXY(COLUMN_START, ROW_START)
    print_custom_character(parts[0])
    oled.setTextXY(COLUMN_START, ROW_START + 1)
    print_custom_character(parts[1])
    oled.setTextXY(COLUMN_START + 1, ROW_START)
    print_custom_character(parts[2])
    oled.setTextXY(COLUMN_START + 1, ROW_START + 1)
    print_custom_character(parts[3])


def print_string(x, y, string):
    oled.setTextXY(x, y)
    oled.putString(string)


def init():
    oled.init()  # initialize SEEED OLED display

    oled.clearDisplay()  # clear the screen and set start position to top left corner
    oled.setNormalDisplay()  # Set display to normal mode (i.e non-inverse mode)
    oled.setPageMode()  # Set addressing mode to Page Mode
