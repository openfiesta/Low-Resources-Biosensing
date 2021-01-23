#include <Wire.h>
#include "Sensor_functions.h"

#define PWM_PIN 11

Adafruit_ADS1115 temperature_array (0x4B);

char Incoming_byte = '0';


void setup() {
  Serial.begin(9600);

//  
  temperature_array.setGain(GAIN_ONE); // +/- 4.096V  1 bit = 0.125mV
  temperature_array.begin();
}

void loop() {

  if (Serial.available())
  {
    Incoming_byte = Serial.read();
    while (Serial.available())
      Serial.read();
  }

  if (Incoming_byte == '1')
    analogWrite(PWM_PIN, 125);
  else
    analogWrite(PWM_PIN, 0);

  Serial.print(Incoming_byte);
  Serial.print(",");
  Serial.println(read_temperature (0, temperature_array), 2);
  delay(1000);
}
