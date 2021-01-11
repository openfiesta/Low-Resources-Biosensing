#include "Arduino.h"
#include "Sensor_functions.h"
#include "temp_table.h"


int read_temperature (int sensor_number, Adafruit_ADS1115 temp_array){
  //Gain is expected to be 1

  unsigned int TH, TH_REF;
  float TH_voltage, TH_voltage_reference, TH_resistance, V_total;

  if (sensor_number < 0 && sensor_number > 3)
    return -1;
  
  TH = temp_array.readADC_SingleEnded(sensor_number);
  TH_REF = temp_array.readADC_SingleEnded(0);
  
  if (TH > MAX_ADC_VALUE || TH < 0)
    return -2;

  TH_voltage = float(map(TH,0,MAX_ADC_VALUE,0,MAX_ADC_VOLTAGE))/100000;
  TH_voltage_reference = float(map(TH_REF,0,MAX_ADC_VALUE,0,MAX_ADC_VOLTAGE))/100000;
  
//  Serial.print(TH);
//  Serial.print(",");
//  Serial.println(TH_REF);

  V_total = ((AUX_RESISTOR + 8.2)/((2*AUX_RESISTOR)+8.2)) * TH_voltage_reference;

  TH_resistance = (TH_voltage_reference/TH_voltage) * AUX_RESISTOR;
  
  Serial.print(TH_voltage, 4);
  Serial.print(",");
  Serial.print(TH_voltage_reference, 4);
  Serial.print(",");
  Serial.println(V_total, 4);
//  
//  for (int i,previous=0; i<NUMTEMPS; i++)
//  {
//    if (abs(temptable[i][1]
//  }
  
  return TH_resistance;
}
