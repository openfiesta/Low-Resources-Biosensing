#include "Arduino.h"
#include "Sensor_functions.h"
#include "temp_table.h"


int read_temperature (int sensor_number, Adafruit_ADS1115 temp_array){
  //Gain is expected to be 1

  int TH, TH_voltage, TH_resistance;

  if (sensor_number < 0 && sensor_number > 3)
    return -1;
  
  TH = temp_array.readADC_SingleEnded(sensor_number);
  
  if (TH > MAX_ADC_VALUE && TH < 0)
    return -2;

  TH_voltage = map(TH,0,MAX_ADC_VALUE,0,MAX_ADC_VOLTAGE);

  TH_resistance = (5-TH_voltage)*8200%TH_voltage;
//  
//  for (int i,previous=0; i<NUMTEMPS; i++)
//  {
//    if (abs(temptable[i][1]
//  }
  
  return TH_resistance;
}
