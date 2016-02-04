//initializes/defines the output pin of the LM34 temperature sensor
int outputpin = A0;
//this sets the ground pin to LOW and the input voltage pin to high
void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);
}

//main loop
void loop() {
  int rawVoltage= analogRead(outputpin);
  float millivolts = (rawVoltage/1024.0) * 5000;
  float fahrenheit = millivolts/10;
  
  float celsius = (fahrenheit - 32) * (5.0/9.0);
  
  Serial.print(celsius);

  if (celsius >= 30.0) {
    setLed(true);
  }
  else {
    setLed(false);
  }
  delay(1000);

}

void setLed(boolean on) {
  if (on) {
    digitalWrite(13, HIGH); 
  }
  else {
    digitalWrite(13, LOW);  
  }

}

