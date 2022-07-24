#include <Wire.h>

int sensor_pin = A0;  //soil moisture sensor is connected to the A0 pin of thr arduino
float sensor_value ;  //soi moisture sensor output
int out; 

void setup() {
  Serial.begin(9600);
  Wire.begin(8);         
  Wire.onRequest(requestEvent);
}

void loop() {
}

void requestEvent() {
  send_soil_moisture();  //when a request came from the master, the slave arduino calls this function
}

void send_soil_moisture(){  //this function read the sensor values and write it to the bus
  sensor_value= analogRead(sensor_pin); 
  float percentage = 100 - sensor_value*100/1024;
  Serial.print("Sending Mositure value: ");
  out = round(percentage);
  Serial.print(out);
  Serial.println("%");
  Wire.write(out);
}
