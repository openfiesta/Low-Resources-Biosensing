#include <Wire.h>
#include "Sensor_functions.h"

Adafruit_ADS1115 temperature_array (0x4B);

void setup() {
  Serial.begin(9600);

//  
  temperature_array.setGain(GAIN_EIGHT); 
  temperature_array.begin();
}

void loop() {
  Serial.println(read_temperature (0, temperature_array), 2);
  delay(1000);
}
