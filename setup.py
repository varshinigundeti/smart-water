def setup():

    led.value(0)
    pump_off()

    lcd.clear()
    lcd.move_to(0, 0)
    lcd.putstr("SMART WATER")

    lcd.move_to(0, 1)
    lcd.putstr("QUALITY SYSTEM")

    sleep(2)
    lcd.clear()