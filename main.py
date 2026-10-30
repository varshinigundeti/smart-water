def main():

    setup()

    while True:

        # Read sensors
        ph_raw = read_ph()
        tds_raw = read_tds()
        turbidity_raw = read_turbidity()

        # Calculate values
        ph = calculate_ph(ph_raw)
        tds = calculate_tds(tds_raw)

        # Serial/REPL output
        print("====================")
        print("pH Value:", round(ph, 2))
        print("TDS Value:", round(tds, 2), "ppm")
        print("Turbidity Raw:", turbidity_raw)

        # LED control
        check_led(ph, tds)

        # Pump control
        if not PUMP_AUTOMATION:
            pump_off()

        # LCD display
        display_lcd(ph, tds, turbidity_raw)

        sleep(0.5)


main()