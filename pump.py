def pump_off():

    if RELAY_ACTIVE_LOW:
        relay.value(1)
    else:
        relay.value(0)