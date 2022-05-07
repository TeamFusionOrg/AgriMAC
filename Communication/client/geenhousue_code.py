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

command = "send_data Sam220408_14 2022-05-08 00:30:49"
client_instance.send_message(command)

json_data = client_instance.recv_message()

print(json.loads(json_data))

input()

client_instance.stop_client()