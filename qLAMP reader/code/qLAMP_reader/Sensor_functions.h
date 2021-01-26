#ifndef qLAMP_h
#define qLAMP_h

#include "Arduino.h"
#include <Adafruit_ADS1015.h>

#define MAX_ADC_VALUE 65535
#define AUX_RESISTOR 8.2

class io_status {
  private:
  //input
    float temperature[3];
    float PD[8];
    Adafruit_ADS1115 temperature_array {0x4B};

    float read_temperature(int sensor_number);
  
  
  //output
    int PWM_power;
    byte LED;
    

  public:
    io_status();
    void update_temperature();
    
};

#endif
