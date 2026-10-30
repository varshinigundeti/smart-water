def read_ph():
    total = 0

    for i in range(20):
        total += ph_sensor.read()
        sleep(0.01)

    return total / 20
