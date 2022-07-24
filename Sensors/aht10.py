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
#kdjd
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)



def ReadTempAndHum(senseNum):
    sensor = adafruit_ahtx0.AHTx0(tca[senseNum])
    return sensor.temperature, sensor.relative_humidity

while True:
    sen_1 = ReadTempAndHum(0)
    sen_2 = ReadTempAndHum(1)
    sen_3 = ReadTempAndHum(2)
    print("running")
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    font = ImageFont.truetype("arial.ttf", size=15)
    draw.text((0, -2),"running",font=font, fill=255)
    draw.text((0,15),"Temperature: "+ str(round(sen_1[0],2)) ,font=font, fill=100)
    draw.text((0, 40),"Humidity: "+ str(round(sen_1[1],2)) ,font= font, fill=255)
    disp.image(image)
    disp.display()
    time.sleep(3)
    disp.clear()

























# while True:
# #     gpio.output(22, 1)
# #     print(ReadTempAndHum(),"sen_1")
# #     time.sleep(1)
# #     gpio.output(22, 0)
# #     time.sleep(3)
# #     gpio.output(27, 1)
# #     print(ReadTempAndHum(3,2),"sen_2")
# #     time.sleep(1)
# #     gpio.output(27, 0)
# #     time.sleep(1)
#     gpio.output(17, 1)
#     print(ReadTempAndHum(),"sen_3")
#     time.sleep(1)
#     gpio.output(17, 0)
#     time.sleep(3)
