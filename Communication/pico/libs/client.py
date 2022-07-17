import utime
   
class Client:
    def __init__(self, uart, client_id, server, port):
        """
        DOCSTRING: this function will initialize the GSM moduel
        """
        print("GSM module initializing")
        
        # initialize variables for the class
        self.uart = uart
        self.client_id = client_id
        self.server = server
        self.port = str(port)
        
        utime.sleep(1) # sleeping is mandetory to prevent initalize crashing
        print(self.sendCMD_waitResp("AT\n"))
        print(self.sendCMD_waitResp("AT+CSQ\n"))
        print(self.sendCMD_waitResp("AT+CCID\n"))
        
        print("---------------------------------------")
        
    def sendCMD_waitResp(self, cmd, timeout=2000):
        """
        DOCSTRING: this function will send command to the GSM module and wait for the response
        return: the response from the GSM module
        """
        self.uart.write(cmd)
        return self.wait_readResp()
    
    def wait_readResp(self, timeout=2000):
        """
        DOCSTRING: this function will wait for the response and read the response
        return: the response from the GSM module
        """
        prvMills = utime.ticks_ms()
        resp = b""
        while (utime.ticks_ms()-prvMills)<timeout:
            if self.uart.any():
                resp = b"".join([resp, self.uart.read(1)])
        try:
            return resp.decode()
        except UnicodeError:
            return resp        

    def sendSMS(self, reciver, message):
        """
        DOCSTRING: this function will send a SMS using GSM module
        return: none
        """
        self.sendCMD_waitResp("AT+CMGF=1\n")
        self.sendCMD_waitResp(f"AT+CMGS=\"{reciver}\"\r\n")
        self.sendCMD_waitResp(f"{message}\n")
        self.sendCMD_waitResp(chr(26) + "\n")
        
    def __setupGPRS(self):
        """
        DOCSTRING: this function will setup the GSM module for TCP communication protocol
        retrun: None
        """
        # the commands list hold the commands needed for the setup in order
        commands = ["AT+CFUN=1", "AT+CPIN?", "AT+CIICR", "AT+CIFSR", "AT+CIPSTART=\"TCP\",\"124.43.59.246\",8080"]
        for command in commands:
            result = self.sendCMD_waitResp(command + "\n")
            print(result)
            
    def send_message(self, message):
        """
        DOCSTRING: this function will send the message given to the server. Note that this function
                   uses a specific protocol to send the data defined by the server itself
        """
        message_size = str(len(message)) # get the message size
        
        # send the size information first
        self.uart.write("AT+CIPSEND\n")
        utime.sleep(0.5)
        self.uart.write(message_size)
        utime.sleep(0.5)
        self.uart.write(chr(26))
        utime.sleep(0.5)
        
        # send the data next
        self.uart.write("AT+CIPSEND\n")
        utime.sleep(0.5)
        self.uart.write(message)
        utime.sleep(0.5)
        self.uart.write(chr(26))
        utime.sleep(0.5)
    
    def start_client(self):
        """
        DOCSTRING: this function will start the client by setting up the TCP communication and
                   sending the client_id information to the server
        """
        self.__setupGPRS()
        self.send_message(self.client_id)
    
    def stop_client(self):
        """
        DOCSTRING: this function will stop the client by sending the disconnect signal and closing
                   the GSM communication
        """
        self.send_message("conn_quit()")
        result = self.sendCMD_waitResp("AT+CIPSHUT\n")
        print(result)
        
