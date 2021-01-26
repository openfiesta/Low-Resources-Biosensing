#include "Arduino.h"
#include "Sensor_functions.h"
#include <math.h>
#include "ArduinoJson.h"
#include <Adafruit_ADS1015.h>


io_status::io_status()  {
  temperature_array.setGain(GAIN_ONE); // +/- 4.096V  1 bit = 0.125mV
  temperature_array.begin();
}

float io_status::read_temperature (int sensor_number){
  
  int TH, TH_REF;
  float TH_voltage, TH_voltage_reference, TH_resistance;

  if (sensor_number < 0 && sensor_number > 3)
    return -1;
  
  TH = temperature_array.readADC_SingleEnded(sensor_number);
  TH_REF = temperature_array.readADC_SingleEnded(3);
  
  if (TH >= MAX_ADC_VALUE || TH < 0)
    return -2;

  TH_voltage = 0.000125 * TH;
  TH_voltage_reference = 0.000125 * TH_REF;

  TH_resistance = ((2 * AUX_RESISTOR * TH_voltage_reference) / TH_voltage) - AUX_RESISTOR; 

//  DEBUG
//  ----------------------------------------------------
//  Serial.print(TH);
//  Serial.print(",");
//  Serial.println(TH_REF);
//  Serial.print(TH_voltage, 8);
//  Serial.print(",");
//  Serial.print(TH_voltage_reference, 8);
//  Serial.print(",");
//  Serial.print(TH_voltage_reference/TH_voltage, 8);
//  Serial.print(",");
//  Serial.print(TH_resistance, 4);
//  Serial.print(",");
//  -----------------------------------------------------
  
//Function obtained by exponential regression of a NTC 10k 3095 temptable 
  temperature[sensor_number] = log((TH_resistance - 0.5261)/31.4839)/-0.04758;
  return 1;
}

void io_status::update_temperature () {
  for (int i  = 0; i < 3; i++)
    read_temperature (i); 
  }
