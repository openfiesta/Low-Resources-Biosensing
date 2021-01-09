#include "Arduino.h"
#include "Sensor_functions.h"
#include "temp_table.h"


int read_temperature (int sensor_number, Adafruit_ADS1115 temp_array){
  //Gain is expected to be 1

  unsigned int TH;
  float TH_voltage, TH_resistance;

  if (sensor_number < 0 && sensor_number > 3)
    return -1;
  
  TH = temp_array.readADC_SingleEnded(sensor_number);
  
  if (TH > MAX_ADC_VALUE && TH < 0)
    return -2;

  TH_voltage = float(map(TH,0,MAX_ADC_VALUE,0,MAX_ADC_VOLTAGE))/10000;
//  Serial.print("TH_voltage:");
//  Serial.println(TH_voltage);

  TH_resistance = ((5.01-TH_voltage)*8.200)/TH_voltage;
  Serial.print(TH_voltage, 4);
  Serial.print(",");
  Serial.println(TH_resistance, 4);
//  
//  for (int i,previous=0; i<NUMTEMPS; i++)
//  {
//    if (abs(temptable[i][1]
//  }
  
  return TH_resistance;
}
