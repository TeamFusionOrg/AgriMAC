# !/usr/bin/python
from libs.client import Client
import json
import numpy as np
from time import sleep

def read_conf_file():
    """
    DOCSTRING: This function will read the configureation file
    """
    with open('greenhouse.conf', 'r') as config_file:
        config_data = config_file.readlines()

    client_conf_data = {}

    for line in config_data:
        line = line.split()
        client_conf_data[line[0]] = line[1:]

    return client_conf_data

# read the configuration file and create an instance of the client module
conf_data = read_conf_file()
client_instance = Client(conf_data['client_id:'][0], conf_data['host:'][0], int(conf_data['port:'][0]))


class GreenHouse:
    def __init__(self, client):
        """
        DOCSTRING: this function will initialize the green house class
        client: this is the client instance
        """
        self.client = client
    
    def recive_info(self, sampler, date, time):
        """
        DOCSTRING: this function will recive recorded data from the server data base and decode it.
        return: a nested list of data
        """

        # command = f"send_data Sam220507_12 2022-05-08 09:58%"
        command = f"send_data {sampler} {date} {time}%"
        client_instance.send_message(command)
        json_data = client_instance.recv_message()

        raw_data = json.loads(json_data) # now this result may be a collection of JSON strings
        # we have to decode each JSON string back to ditionaries
        
        decoded_data = []

        for JSON_data in raw_data:
            decoded_data.append(json.loads(JSON_data[0]))

        return decoded_data

    def run(self):
        """
        DOCSTRING: this is the main funtion of the class. This will trigger all the functions when necessary
        """
        self.client.start_client() # start the client

        data = self.recive_info("Sam220507_12", "2022-05-08", "09:58")
        
        for sub_data in data:
            print(list(map(float, sub_data['results']['PH'].split(','))), end = "\n\n")

        self.client.stop_client() # ending the communication with the server


greenHouse = GreenHouse(client_instance)
greenHouse.run()