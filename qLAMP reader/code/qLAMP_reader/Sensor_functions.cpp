#include "Arduino.h"
#include "Sensor_functions.h"
#include "temp_table.h"
#include <math.h>


float read_temperature (int sensor_number, Adafruit_ADS1115 temp_array){
  
  int TH, TH_REF;
  float TH_voltage, TH_voltage_reference, TH_resistance, temperature;

  if (sensor_number < 0 && sensor_number > 3)
    return -1;
  
  TH = temp_array.readADC_SingleEnded(sensor_number);
  TH_REF = temp_array.readADC_SingleEnded(3);

//  Serial.print(TH_REF);
//  Serial.print(",");
  
  if (TH >= MAX_ADC_VALUE || TH < 0)
    return -2;

  TH_voltage = 0.000015625 * TH;
  TH_voltage_reference = 0.000015625 * TH_REF;
  
//  Serial.print(TH);
//  Serial.print(",");
//  Serial.println(TH_REF);

  TH_resistance = (TH_voltage_reference/TH_voltage) * AUX_RESISTOR;
  

//  Serial.print(TH_voltage, 8);
//  Serial.print(",");
//  Serial.print(TH_voltage_reference, 8);
//  Serial.print(",");
//  Serial.print(TH_resistance, 4);
//  Serial.print(",");
  

  temperature = log((TH_resistance - 0.5261)/31.4839)/-0.04758

  return temperature;
}
