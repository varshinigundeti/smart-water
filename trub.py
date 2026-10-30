def read_turbidity():

    total = 0

    for i in range(20):
        total += turbidity_sensor.read()
        sleep(0.01)

    return total / 20