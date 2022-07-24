import adafruit_ahtx0
import busio
import RPi.GPIO as gpio
import adafruit_tca9548a
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

class OLED_display():
    def __init__(self, scl, sda):
        self.SCL_pin = scl
        self.SDA_pin = sda

        self.i2c = busio.I2C(self.SCL_pin, self.SDA_pin)
        self.disp = Adafruit_SSD1306.SSD1306_128_64(rst=None)
        
        self.disp.begin()
        # Clear display.
        self.disp.clear()
        self.disp.display()
        #display settings
        self.width = self.disp.width
        self.height = self.disp.height
        self.image = Image.new('1', (self.width, self.height))
        self.draw = ImageDraw.Draw(self.image)

    def __AddRect(self, x_1 = 0, x_2 = self.width, y_1 = 0, y_2 = self.height, outline_num = 0,fill_num = 255):
        self.draw.rectangle((x_1,x_2,y_1,y_2), outline=outline_num, fill=fill_num)

    def __display(self):
        self.disp.image(self.image)
        self.disp.display()
        self.disp.clear()

    def diplayText(self, text, fontFile,size,x,y,fill_num):
        self.__AddRect()
        font = ImageFont.truetype(fontFile, size=size)
        self.draw.text((x, y),text,font=font, fill=fill_num)
        self.__display()


class TempHumidSensor():
    def __init__(self, scl, sda):
        self.SCL_pin = scl
        self.SDA_pin = sda

        self.i2c = busio.I2C(self.SCL_pin, self.SDA_pin)
        self.tca = adafruit_tca9548a.TCA9548A(self.i2c)

    def ReadTempAndHum(self, senseNum):
        sensor = adafruit_ahtx0.AHTx0(self.tca[senseNum])
        return sensor.temperature, sensor.relative_humidity






    

