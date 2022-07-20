import time
import adafruit_ahtx0
import busio


def ReadTempAndHum(sclPin,sdaPin):
    i2c = busio.I2C(sclPin,sdaPin)  
    sensor = adafruit_ahtx0.AHTx0(i2c)
    
    return sensor.temperature, sensor.relative_humidity

