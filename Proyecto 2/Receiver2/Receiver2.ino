#include <SPI.h>
#include "SPI_anything.h"
#include <math.h>
#include <arduinoFFT.h>

#define SIZE 128

double nums[SIZE];
double miccarrier[SIZE];
double lowpassFilteredSignal[SIZE];
double lowpassFilteredSignal2[SIZE];

const int speakerPin = 9;

const int fc_lowpass = 2000;
const int fs = 9600;

double amplitude =1;
double increment = twoPi / (double)SIZE;

volatile bool haveData = false;

void generateCarriers() {
  for (int i = 0; i < SIZE; i++) {
    miccarrier[i] = amplitude * cos(increment * 200000 * i);
  }
}

void setup() { 

  Serial.begin (115200);   // debugging

  // have to send on master in, *slave out*
  pinMode(MISO, OUTPUT);
  
  // turn on SPI in slave mode
  SPCR |= _BV(SPE);

  // now turn on interrupts
  SPI.attachInterrupt();
  pinMode(speakerPin, OUTPUT);
  generateCarriers();
}
 
void loop() {
  if (haveData)
     {
      for(int i = 2; i < SIZE; i++){

          nums[i] = nums[i] * miccarrier[i];

          lowpassFilteredSignal2[i] = 0.0001 * nums[i] + 0.0009 * lowpassFilteredSignal2[i-1];
          //lowpassFilteredSignal2[i] = 0.0001 * nums[i] + 0.0005 * lowpassFilteredSignal2[i-1];


           Serial.println (10*lowpassFilteredSignal2[i]);

           analogWrite(speakerPin, 10*lowpassFilteredSignal2[i]);
           
      }
      haveData = false;
    
     }
}
// SPI interrupt routine
ISR (SPI_STC_vect)
  {
  SPI_readAnything_ISR (nums);
  haveData = true;
  }  // end of interrupt routine SPI_STC_vect

