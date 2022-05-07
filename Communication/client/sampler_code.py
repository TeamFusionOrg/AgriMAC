from libs.client_sampler import Client
import json
import numpy as np
from time import sleep

def read_conf_file():
    with open('client.conf', 'r') as config_file:
        config_data = config_file.readlines()

    client_conf_data = {}

    for line in config_data:
        line = line.split()
        client_conf_data[line[0]] = line[1:]

    return client_conf_data

conf_data = read_conf_file()

client_instance = Client(conf_data['client_id:'][0], conf_data['host:'][0], int(conf_data['port:'][0]))
client_instance.start_client()

input()

for i in range (50):
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


    data = {
        "results" : {"temp":temp, "PH":PH, "wind":wind},
        "status":"OK"
    }

    client_instance.send_message(json.dumps(data))

    sleep(0.1)

input()

client_instance.stop_client()