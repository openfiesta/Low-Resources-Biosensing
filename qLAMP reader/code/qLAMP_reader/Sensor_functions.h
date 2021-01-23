#ifndef qLAMP_h
#define qLAMP_h

#include "Arduino.h"
#include <Adafruit_ADS1015.h>

#define MAX_ADC_VALUE 65535
#define AUX_RESISTOR 8.2

float read_temperature (int sensor_number, Adafruit_ADS1115 temp_array);

#endif
