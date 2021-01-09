#ifndef qLAMP_h
#define qLAMP_h

#include "Arduino.h"
#include <Adafruit_ADS1015.h>

#define MAX_ADC_VALUE 65534
#define MAX_ADC_VOLTAGE 4096

int read_temperature (int sensor_number, Adafruit_ADS1115 temp_array);

#endif
