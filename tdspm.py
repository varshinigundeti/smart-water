def calculate_tds(raw_value):

    voltage = raw_value * 3.3 / 4095

    compensation = 1 + 0.02 * (WATER_TEMPERATURE - 25)

    compensated_voltage = voltage / compensation

    tds = (
        133.42 * pow(compensated_voltage, 3)
        - 255.86 * pow(compensated_voltage, 2)
        + 857.39 * compensated_voltage
    ) * TDS_FACTOR

    if tds < 0:
        tds = 0

    return tds