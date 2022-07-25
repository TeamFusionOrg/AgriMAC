from time import sleep
import client
from threading import Thread

#global things
before_content = ""
update_file_location = r"E:\\soft_installations\\xampp\\htdocs\\adminkit\\static\\scripts\\edit_by_web.txt"

SERVER = "192.168.56.1"
PORT = 5151
PASSWRD = "A4nJ!dk@12en#jfdk*kjns.sdjk"

client_inst = client.Client("WebSite", SERVER, PORT, PASSWRD)


with open(update_file_location, 'r') as update_file:
    before_content = update_file.read()


def check_for_update():
    """
    DOCSTRING: this function constantly waiting for a update from the website and send to the raspberry pi
    """
    global before_content 

    while True:
        
        try:
            with open(update_file_location, 'r') as update_file:
                content = update_file.read()
                
            if (before_content != content):
                before_content = content

                
                humidity = content.split(",")[1]
                moister = content.split(",")[2]
                
                print("Updated Content {}".format(content.split(",")[1]))
                print(client_inst.send_message("send_to_rpi {} {}".format(humidity, moister)))
                sleep(1)


        
        except Exception as err:
            print (err)

def web_data_editor():
    """
    DOCSTRING" this function recives the current weather inside the greenhouse and update the database
    """
    while True:
        message = client_inst.recv_message(False)
        if message:
            message = list(map(float, message.split(","))) # humidity and moisterization
            
            with open(r"E:\\soft_installations\\xampp\\htdocs\\adminkit\\static\\virus.txt", "w") as webfile:
                topline = "{} C<sup>0</sup>,{} %,{} %,{} Watt\n".format(message[0], message[1], message[2], message[3])
                bottom_line = "0.45%,-0.41%,0.07%,0.46%"

                webfile.write(topline + bottom_line)


def main():


    if (client_inst.start_client()[0]):
        print("client started")

        sending_thread = Thread(target=check_for_update)
        reciving_thread = Thread(target=web_data_editor)

        sending_thread.start()
        reciving_thread.start()


        sending_thread.join()
        reciving_thread.join()

        client_inst.stop_client()

if __name__ == '__main__':
    main()