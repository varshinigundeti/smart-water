def read_tds():
    total = 0

    for i in range(20):
        total += tds_sensor.read()
        sleep(0.01)

    return total / 20