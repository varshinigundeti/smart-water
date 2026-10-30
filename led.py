def check_led(ph, tds):

    if PH_MIN <= ph <= PH_MAX and tds <= TDS_MAX:
        led.value(1)
    else:
        led.value(0)