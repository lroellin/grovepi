# top left, bottom left, top right, bottom right
sun = [
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

cloud = [
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
mist = [
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

cloud_with_sun = [
    cloud[0],
    cloud[1],
    [
        cloud[2][0] | 0b10000001,
        cloud[2][1] | 0b01000010,
        cloud[2][2] | 0b00011000,
        cloud[2][3] | 0b00100100,
        cloud[2][4] | 0b00100100,
        cloud[2][5] | 0b00011000,
        cloud[2][6] | 0b01000010,
        cloud[2][7] | 0b10000001
    ],
    cloud[3]
]

cloud_with_cloud = [
    cloud[0],
    cloud[1],
    [
        cloud[2][0] | 0b00000000,
        cloud[2][1] | 0b00001000,
        cloud[2][2] | 0b00010100,
        cloud[2][3] | 0b00010010,
        cloud[2][4] | 0b00010001,
        cloud[2][5] | 0b00011010,
        cloud[2][6] | 0b00010100,
        cloud[2][7] | 0b00001000
    ],
    cloud[3]
]

cloud_with_cloud_and_rain = [
    cloud_with_cloud[0],
    [
        cloud_with_cloud[1][0] | 0b00100000,
        cloud_with_cloud[1][1] | 0b00000000,
        cloud_with_cloud[1][2] | 0b10000000,
        cloud_with_cloud[1][3] | 0b00000000,
        cloud_with_cloud[1][4] | 0b00100000,
        cloud_with_cloud[1][5] | 0b00000000,
        cloud_with_cloud[1][6] | 0b10000000,
        cloud_with_cloud[1][7] | 0b00000000
    ],
    cloud_with_cloud[2],
    [
        cloud_with_cloud[3][0] | 0b00100000,
        cloud_with_cloud[3][1] | 0b00000000,
        cloud_with_cloud[3][2] | 0b10000000,
        cloud_with_cloud[3][3] | 0b00000000,
        cloud_with_cloud[3][4] | 0b00100000,
        cloud_with_cloud[3][5] | 0b00000000,
        cloud_with_cloud[3][6] | 0b10000000,
        cloud_with_cloud[3][7] | 0b00000000
    ]
]

cloud_with_sun_and_rain = [
    cloud_with_sun[0],
    [
        cloud_with_sun[1][0] | 0b00100000,
        cloud_with_sun[1][1] | 0b00000000,
        cloud_with_sun[1][2] | 0b10000000,
        cloud_with_sun[1][3] | 0b00000000,
        cloud_with_sun[1][4] | 0b00100000,
        cloud_with_sun[1][5] | 0b00000000,
        cloud_with_sun[1][6] | 0b10000000,
        cloud_with_sun[1][7] | 0b00000000
    ],
    cloud_with_sun[2],
    [
        cloud_with_sun[3][0] | 0b00100000,
        cloud_with_sun[3][1] | 0b00000000,
        cloud_with_sun[3][2] | 0b10000000,
        cloud_with_sun[3][3] | 0b00000000,
        cloud_with_sun[3][4] | 0b00100000,
        cloud_with_sun[3][5] | 0b00000000,
        cloud_with_sun[3][6] | 0b10000000,
        cloud_with_sun[3][7] | 0b00000000
    ]
]

cloud_with_cloud_and_thunder = [
    cloud_with_cloud[0],
    cloud_with_cloud[1],
    cloud_with_cloud[2],
    [
        cloud_with_cloud[3][0] | 0b00000000,
        cloud_with_cloud[3][1] | 0b00000000,
        cloud_with_cloud[3][2] | 0b00000000,
        cloud_with_cloud[3][3] | 0b10000000,
        cloud_with_cloud[3][4] | 0b01101000,
        cloud_with_cloud[3][5] | 0b00111000,
        cloud_with_cloud[3][6] | 0b00011000,
        cloud_with_cloud[3][7] | 0b00001000
    ]
]

cloud_with_cloud_and_snow = [
    cloud_with_cloud[0],
    [
        cloud_with_cloud[1][0] | 0b10100000,
        cloud_with_cloud[1][1] | 0b00000000,
        cloud_with_cloud[1][2] | 0b01000000,
        cloud_with_cloud[1][3] | 0b10100000,
        cloud_with_cloud[1][4] | 0b01000000,
        cloud_with_cloud[1][5] | 0b00000000,
        cloud_with_cloud[1][6] | 0b10100000,
        cloud_with_cloud[1][7] | 0b00000000
    ],
    cloud_with_cloud[2],
    [
        cloud_with_cloud[3][0] | 0b00000000,
        cloud_with_cloud[3][1] | 0b10100000,
        cloud_with_cloud[3][2] | 0b00000000,
        cloud_with_cloud[3][3] | 0b01000000,
        cloud_with_cloud[3][4] | 0b10100000,
        cloud_with_cloud[3][5] | 0b01000000,
        cloud_with_cloud[3][6] | 0b00000000,
        cloud_with_cloud[3][7] | 0b10100000
    ],
]

icon_mapping = {
        "01": sun,
        "02": cloud_with_sun,
        "03": cloud,
        "04": cloud_with_cloud,
        "09": cloud_with_cloud_and_rain,
        "10": cloud_with_sun_and_rain,
        "11": cloud_with_cloud_and_thunder,
        "13": cloud_with_cloud_and_snow,
        "50": mist
    }