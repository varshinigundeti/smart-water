def calculate_ph(raw_value):

    voltage = raw_value * 3.3 / 4095

    slope = 3.0 / (PH7_VOLTAGE - PH4_VOLTAGE)

    ph = 7.0 + slope * (voltage - PH7_VOLTAGE)

    return ph