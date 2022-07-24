
import time
import adafruit_ahtx0
import busio
import RPi.GPIO as gpio
import adafruit_tca9548a
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
# define globals
SCL_pin = 3
SDA_pin = 2
#creating objects
i2c = busio.I2C(SCL_pin, SDA_pin)
tca = adafruit_tca9548a.TCA9548A(i2c)
disp = Adafruit_SSD1306.SSD1306_128_64(rst=None)


disp.begin()

# Clear display.
disp.clear()
disp.display()
#display settings
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)


def ReadTempAndHum(senseNum):
    sensor = adafruit_ahtx0.AHTx0(tca[senseNum])
    return sensor.temperature, sensor.relative_humidity

def AddRect(x_1,x_2,y_1,y_2,outline_num,fill_num):
    draw.rectangle((x_1,x_2,y_1,y_2), outline=outline_num, fill=fill_num)
def diplayText(text, fontFile,size,x,y,fill_num):
    font = ImageFont.truetype(fontFile, size=size)
    draw.text((x, y),text,font=font, fill=fill_num)
def display():
    disp.image(image)
    disp.display()
    disp.clear()
    

