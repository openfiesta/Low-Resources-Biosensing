#include <Wire.h>
#include "Sensor_functions.h"

Adafruit_ADS1115 temperature_array (0x4B);

void setup() {
  Serial.begin(9600);

  
  temperature_array.setGain(GAIN_ONE);    //+/-4.096V
  temperature_array.begin();
}

void loop() {
  read_temperature (1, temperature_array);
  delay(1000);
}
