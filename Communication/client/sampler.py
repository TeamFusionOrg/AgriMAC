from libs.client import Client
import json
import numpy as np
from time import sleep
from datetime import datetime
from threading import Thread

def read_conf_file():
    with open('sampler.conf', 'r') as config_file:
        config_data = config_file.readlines()

    client_conf_data = {}

    for line in config_data:
        line = line.split()
        client_conf_data[line[0]] = line[1:]

    return client_conf_data

conf_data = read_conf_file()
client_instance = Client(conf_data['client_id:'][0], conf_data['host:'][0], int(conf_data['port:'][0]), conf_data['passwd:'][0])



class Sampler:
    def __init__(self, client):
        """
        DOCSTRING: this function will initialize the sampler
        """
        self.client = client
        self.unsent = [] # unsent data will append to this list
        self.terminate = False
    
    def record_unsent(self, data):
        pass

    def gen_data(self):
        temp = ""
        PH = ""
        wind = ""

        t_data = np.random.randint(20, 40, size = (6))
        p_data = np.random.randint(50, 80, size = (6)) / 10
        w_data = np.random.randint(0, 40, size = (6))
        for i in range(6):
            temp += str(t_data[i])
            PH += str(p_data[i])
            wind += str(w_data[i])
            if i != 5:
                temp += ","
                PH += ","
                wind += ","

        date = datetime.now().strftime("%Y-%m-%d")
        time = datetime.now().strftime("%H:%M:%S")

        data = {
            "results" : {"temp":temp, "PH":PH, "wind":wind},
            "date": date,
            "time":time,
            "status":"OK"
        }

        return data

    def send_data_to_server(self):
        while not self.terminate:
            if len(self.unsent) > 0:
                current_message = self.unsent.pop(0)  
                while not self.client.send_message(current_message):
                    sleep(1)

    def record_info(self):

        for i in range (100):
            data = json.dumps(self.gen_data())
            self.unsent.append(data)
            print(self.unsent)
            sleep(2)

    def run(self):
        self.client.start_client()

        sendingThread = Thread(target=self.send_data_to_server)
        samplingThread = Thread(target=self.record_info)
        
        sendingThread.start()
        samplingThread.start()

        sendingThread.join()
        samplingThread.join()

        self.client.stop_client()


sampler = Sampler(client_instance)
sampler.run()
