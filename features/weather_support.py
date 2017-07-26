def format_accurate_temperature(temp):
    return "{:.1f}C".format(temp)

def format_inaccurate_temperature(temp):
    return "{:.0f}".format(temp)

def format_humidity(humidity):
    return "{:.0f}%".format(humidity)