# top left, bottom left, top right, bottom right
sun_parts = [
    [
        0b10000011,
        0b10000111,
        0b10001110,
        0b00001100,
        0b11100000,
        0b11110000,
        0b00110000,
        0b00110111,

    ],
    [
        0b11000001,
        0b11100001,
        0b01110001,
        0b00110000,
        0b00000111,
        0b00001111,
        0b00001100,
        0b11101100,
    ],
    [
        0b00110111,
        0b00110000,
        0b11110000,
        0b11100000,
        0b00001100,
        0b10001110,
        0b10000111,
        0b10000011
    ],
    [
        0b11101100,
        0b00001100,
        0b00001111,
        0b00000111,
        0b00110000,
        0b01110001,
        0b11100001,
        0b11000001
    ]
]

cloud_parts = [
    [
        0b00000000,
        0b00000000,
        0b11000000,
        0b00100000,
        0b00010000,
        0b00010000,
        0b00100000,
        0b00100000
    ],
    [
        0b00000110,
        0b00001001,
        0b00001000,
        0b00001001,
        0b00001010,
        0b00001000,
        0b00001100,
        0b00001010
    ],
    [
        0b01000000,
        0b10000000,
        0b00000000,
        0b00000000,
        0b00000000,
        0b00000000,
        0b00000000,
        0b00000000
    ],
    [
        0b00001001,
        0b00001000,
        0b00001001,
        0b00000110,
        0b00000000,
        0b00000000,
        0b00000000,
        0b00000000
    ]
]
mist_parts = [
    [
        0b10010010,
        0b01001001,
        0b10010010,
        0b00100100,
        0b10010010,
        0b01001001,
        0b10010010,
        0b00100100
    ],
    [
        0b00100100,
        0b00010010,
        0b00100100,
        0b01001001,
        0b00100100,
        0b00010010,
        0b00100100,
        0b01001001
    ],
    [  # copy of [0]
        0b10010010,
        0b01001001,
        0b10010010,
        0b00100100,
        0b10010010,
        0b01001001,
        0b10010010,
        0b00100100
    ],  # copy of [1]
    [
        0b00100100,
        0b00010010,
        0b00100100,
        0b01001001,
        0b00100100,
        0b00010010,
        0b00100100,
        0b01001001
    ]
]

# We now have the basic icons. From here on, we simply combine those with new "additions"
# This is quite hacky ;)

cloud_with_sun_parts = [
    cloud_parts[0],
    cloud_parts[1],
    [
        cloud_parts[2][0] | 0b10000001,
        cloud_parts[2][1] | 0b01000010,
        cloud_parts[2][2] | 0b00011000,
        cloud_parts[2][3] | 0b00100100,
        cloud_parts[2][4] | 0b00100100,
        cloud_parts[2][5] | 0b00011000,
        cloud_parts[2][6] | 0b01000010,
        cloud_parts[2][7] | 0b10000001
    ],
    cloud_parts[3]
]

cloud_with_cloud_parts = [
    cloud_parts[0],
    cloud_parts[1],
    [
        cloud_parts[2][0] | 0b00000000,
        cloud_parts[2][1] | 0b00001000,
        cloud_parts[2][2] | 0b00010100,
        cloud_parts[2][3] | 0b00010010,
        cloud_parts[2][4] | 0b00010001,
        cloud_parts[2][5] | 0b00011010,
        cloud_parts[2][6] | 0b00010100,
        cloud_parts[2][7] | 0b00001000
    ],
    cloud_parts[3]
]

cloud_with_cloud_and_rain_parts = [
    cloud_with_cloud_parts[0],
    [
        cloud_with_cloud_parts[1][0] | 0b00100000,
        cloud_with_cloud_parts[1][1] | 0b00000000,
        cloud_with_cloud_parts[1][2] | 0b10000000,
        cloud_with_cloud_parts[1][3] | 0b00000000,
        cloud_with_cloud_parts[1][4] | 0b00100000,
        cloud_with_cloud_parts[1][5] | 0b00000000,
        cloud_with_cloud_parts[1][6] | 0b10000000,
        cloud_with_cloud_parts[1][7] | 0b00000000
    ],
    cloud_with_cloud_parts[2],
    [
        cloud_with_cloud_parts[3][0] | 0b00100000,
        cloud_with_cloud_parts[3][1] | 0b00000000,
        cloud_with_cloud_parts[3][2] | 0b10000000,
        cloud_with_cloud_parts[3][3] | 0b00000000,
        cloud_with_cloud_parts[3][4] | 0b00100000,
        cloud_with_cloud_parts[3][5] | 0b00000000,
        cloud_with_cloud_parts[3][6] | 0b10000000,
        cloud_with_cloud_parts[3][7] | 0b00000000
    ]
]

cloud_with_sun_and_rain_parts = [
    cloud_with_sun_parts[0],
    [
        cloud_with_sun_parts[1][0] | 0b00100000,
        cloud_with_sun_parts[1][1] | 0b00000000,
        cloud_with_sun_parts[1][2] | 0b10000000,
        cloud_with_sun_parts[1][3] | 0b00000000,
        cloud_with_sun_parts[1][4] | 0b00100000,
        cloud_with_sun_parts[1][5] | 0b00000000,
        cloud_with_sun_parts[1][6] | 0b10000000,
        cloud_with_sun_parts[1][7] | 0b00000000
    ],
    cloud_with_sun_parts[2],
    [
        cloud_with_sun_parts[3][0] | 0b00100000,
        cloud_with_sun_parts[3][1] | 0b00000000,
        cloud_with_sun_parts[3][2] | 0b10000000,
        cloud_with_sun_parts[3][3] | 0b00000000,
        cloud_with_sun_parts[3][4] | 0b00100000,
        cloud_with_sun_parts[3][5] | 0b00000000,
        cloud_with_sun_parts[3][6] | 0b10000000,
        cloud_with_sun_parts[3][7] | 0b00000000
    ]
]

cloud_with_cloud_and_thunder_parts = [
    cloud_with_cloud_parts[0],
    cloud_with_cloud_parts[1],
    cloud_with_cloud_parts[2],
    [
        cloud_with_cloud_parts[3][0] | 0b00000000,
        cloud_with_cloud_parts[3][1] | 0b00000000,
        cloud_with_cloud_parts[3][2] | 0b00000000,
        cloud_with_cloud_parts[3][3] | 0b10000000,
        cloud_with_cloud_parts[3][4] | 0b01101000,
        cloud_with_cloud_parts[3][5] | 0b00111000,
        cloud_with_cloud_parts[3][6] | 0b00011000,
        cloud_with_cloud_parts[3][7] | 0b00001000
    ]
]

cloud_with_cloud_and_snow_parts = [
    cloud_with_cloud_parts[0],
    [
        cloud_with_cloud_parts[1][0] | 0b10100000,
        cloud_with_cloud_parts[1][1] | 0b00000000,
        cloud_with_cloud_parts[1][2] | 0b01000000,
        cloud_with_cloud_parts[1][3] | 0b10100000,
        cloud_with_cloud_parts[1][4] | 0b01000000,
        cloud_with_cloud_parts[1][5] | 0b00000000,
        cloud_with_cloud_parts[1][6] | 0b10100000,
        cloud_with_cloud_parts[1][7] | 0b00000000
    ],
    cloud_with_cloud_parts[2],
    [
        cloud_with_cloud_parts[3][0] | 0b00000000,
        cloud_with_cloud_parts[3][1] | 0b10100000,
        cloud_with_cloud_parts[3][2] | 0b00000000,
        cloud_with_cloud_parts[3][3] | 0b01000000,
        cloud_with_cloud_parts[3][4] | 0b10100000,
        cloud_with_cloud_parts[3][5] | 0b01000000,
        cloud_with_cloud_parts[3][6] | 0b00000000,
        cloud_with_cloud_parts[3][7] | 0b10100000
    ],
]
