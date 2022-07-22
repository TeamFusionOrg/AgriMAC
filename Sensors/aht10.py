import time
import adafruit_ahtx0
import busio
import RPi.GPIO as gpio
import adafruit_tca9548a

# define globals
SCL_pin = 3
SDA_pin = 2
#creating objects
i2c = busio.I2C(SCL_pin, SDA_pin)
tca = adafruit_tca9548a.TCA9548A(i2c)
def ReadTempAndHum(senseNum):
    sensor = adafruit_ahtx0.AHTx0(tca[senseNum])
    return sensor.temperature, sensor.relative_humidity

