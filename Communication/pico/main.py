#######################################################
# Team FUSION spark project RPI pico micropython code #
# --------------------------------------------------- #
# date:    14-May-2022                                #
# version: 1.0.0.0                                    #
#######################################################

import uos
import utime
import ujson
from client import Client
from datetime import datetime
from machine import UART, Pin, Timer, I2C
from sensors import Sensors

# define the onboard LED to indicate states
led = Pin(25, Pin.OUT)
LED_state = True
tim = Timer()

def tick(timer):
    global LED_state, led
    LED_state = not LED_state
    led.value(LED_state)

# set frequency to 0.5 to indicate starting
tim.init(freq = 0.5, mode = Timer.PERIODIC, callback=tick)

# define GLOBAL variables needed to define the Client module
uart0 = UART(0, baudrate=9600)
client_id = "Sam220608_134"             # the ID of this SAMPLER (This will be recorded in the databse)
server = "123.231.122.199"              # the IP of the SPARK server 
port = 5151                             # the PORT of connection of the spark server

utime.sleep(1)
# create and instance of client module for communication
client = Client(uart0, client_id, server, port)
i2c_bus = I2C(0, scl = Pin(9), sda = Pin(8), freq=100000)
sensors = Sensors(i2c_bus)

def read_get_data():
    temp_results = dict()
    for _ in range(5):
        keys , values = sensors.getData()
        for index, key in enumerate(keys):
            try:
                temp_results[key].append(values[index])
            except KeyError:
                temp_results[key] = [values[index]]
        utime.sleep(60)
    return temp_results






tim.init(freq = 10, mode = Timer.PERIODIC, callback=tick)
print("Starting Client")

while not client.start_client():
    client.reboot()
    
print("Fetching Datetime")
d = datetime(client)
tim.init(freq = 2, mode = Timer.PERIODIC, callback=tick)

print("Fetching Datetime --> OK")

pass_counter = 0

while True:
    data = {
        "date": d.getDate(),
        "time": d.getTime(),
        "results" : read_get_data(),
        "status":"OK"
    }
    
    tim.init(freq = 5, mode = Timer.PERIODIC, callback=tick)
    result = client.send_message(ujson.dumps(data))
    tim.init(freq = 2, mode = Timer.PERIODIC, callback=tick)
    
    if result:
        print("Data Successfully sent to the server")
        pass_counter += 1
    else:
        print("Data Sending Failed. Recording to the file")
        pass_counter = 0
        with open('record.txt', 'a') as data_file:
            data_file.write(ujson.dumps(data) + '\n')
        client.reboot()

    if pass_counter > 5:
        client.send_file_data('record.txt')
        pass_counter = 0

client.stop_client()