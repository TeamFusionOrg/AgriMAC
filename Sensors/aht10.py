import time
import adafruit_ahtx0
import busio


def ReadTempAndHum(sclPin,sdaPin,A0,A1,A2):## 000,001,010,.... --> 1 st sensir, 2nd sensor .....
    i2c = busio.I2C(sclPin,sdaPin)  
    sensor = adafruit_ahtx0.AHTx0(i2c)
    
    return sensor.temperature, sensor.relative_humidity

