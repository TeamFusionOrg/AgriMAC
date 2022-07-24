import smbus
import time

addr = 0x08
bus = smbus.SMBus(1)

while True:
    value = bus.read_byte(addr)
    print(value)
    time.sleep(0.5)