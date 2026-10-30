from machine import Pin, ADC, I2C
from time import sleep
from math import pow
from i2c_lcd import I2cLcd

# Sensor pins
PH_PIN = 34
TDS_PIN = 35
TURBIDITY_PIN = 32

# Output pins
LED_PIN = 25
RELAY_PIN = 26

# LCD pins
SDA_PIN = 21
SCL_PIN = 22

# Initialize sensors
ph_sensor = ADC(Pin(PH_PIN))
tds_sensor = ADC(Pin(TDS_PIN))
turbidity_sensor = ADC(Pin(TURBIDITY_PIN))

# ADC configuration
ph_sensor.atten(ADC.ATTN_11DB)
tds_sensor.atten(ADC.ATTN_11DB)
turbidity_sensor.atten(ADC.ATTN_11DB)

# Initialize LED and relay
led = Pin(LED_PIN, Pin.OUT)
relay = Pin(RELAY_PIN, Pin.OUT)

# I2C LCD
i2c = I2C(0, scl=Pin(SCL_PIN), sda=Pin(SDA_PIN))
lcd = I2cLcd(i2c, 0x27, 2, 16)