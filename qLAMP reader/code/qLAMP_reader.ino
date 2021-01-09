#include <Wire.h>
#include "Sensor_functions.h"

Adafruit_ADS1115 temperature_array (0x4B);

void setup() {
  Serial.begin(9600);

  
  temperature_array.setGain(GAIN_ONE);    //+/- 0.256V  1 bit = 0.0078125mV 
  temperature_array.begin();
}

void loop() {
  Serial.println(read_temperature (2, temperature_array));
  delay(1000);
}
