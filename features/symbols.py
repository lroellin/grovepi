OFFSET = 127

THERMOMETER = chr(OFFSET + 1)
_thermometer = [
    0b11111111,
    0b00101010,
    0b10000000,
    0b11111100,
    0b11111100,
    0b10000000,
    0b00101010,
    0b11111111
]

PLUSMINUS = chr(OFFSET + 2)
_plusminus = [
    0b00000000,
    0b10001100,
    0b10001100,
    0b10111111,
    0b10111111,
    0b10001100,
    0b10001100,
    0b00000000,
]
