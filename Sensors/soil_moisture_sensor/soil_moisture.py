import RPi.GPIO as gp

gp.setmode(gp.BOARD)
gp.setup(8,gp.IN)   #setup pin8 (GPIO 14) as input

while True:
    try:
        if gp.input(8) == 1:   #raspberry pi only can detect digital values. It can't process analog inputs
            print("No water detected")
        else:
            print("Water detected")
    except:
        gp.cleanup
    
    