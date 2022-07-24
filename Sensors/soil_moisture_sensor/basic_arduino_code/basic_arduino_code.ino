int sensor_pin = A0; 
float output_value ;

void setup() {
  Serial.begin(9600);
  }

void loop() {
  output_value= analogRead(sensor_pin);
  float percentage = 100 - output_value*100/1024;
  Serial.print("Mositure : ");
  int out = round(percentage);
  Serial.print(out);
  Serial.println("%");
  delay(1000);
  }
