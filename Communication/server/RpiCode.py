from time import sleep
import client
from threading import Thread

#global things

SERVER = "192.168.56.1"
PORT = 5151
PASSWRD = "A4nJ!dk@12en#jfdk*kjns.sdjk"

client_inst = client.Client("rpi", SERVER, PORT, PASSWRD)

def recive_data():
    """
    DOCSTRING: this function will recive data from the website, then fire the actuators
    """
    while True:
        message = client_inst.recv_message(False)
        if message:
            print(message)


def send_data():
    """
    DOCSTRING: this function will measure all the weather conditions and send to the server
    """

    while True:

        temp = 27
        humid = 34
        moist = 67
        power = 33

        client_inst.send_message("send_to_WebSite {} {} {} {}".format(temp, humid, moist, power))
        sleep(5)

def main():


    if (client_inst.start_client()[0]):
        print("client started")
        # sleep(4)
        # print("client sleep done")

        reciveing_thread = Thread(target=recive_data)
        sending_thread = Thread(target=send_data)

        reciveing_thread.start()
        sending_thread.start()


        reciveing_thread.join()
        sending_thread.join()


if __name__ == '__main__':
    main()