//Enviar
#include <SPI.h>
#include "SPI_anything.h"
#include <arduinoFFT.h>
#define SIZE 128

arduinoFFT FFT = arduinoFFT();

const int micPin = A0;
double amplitude =1;
double increment = twoPi / (double)SIZE;
float deltaf = 1000/SIZE;
int counter = 0;
double nums[SIZE];
int peakBin = 15;

double vReal[SIZE];
double vImag[SIZE];
double fftarray[SIZE];

double sine[SIZE];
double sinecarrier[SIZE];
double miccarrier[SIZE];
double micValue[SIZE];
double micmodulated[SIZE];
double sinemodulated[SIZE];
double signal[SIZE];

void generateSinSignal() {
  for (int i = 0; i < SIZE; i++) {
    sinecarrier[i] = amplitude * cos(increment * 2000 * i);
    miccarrier[i] = amplitude * cos(increment * 200000 * i);
    sine[i] = amplitude * sin(i * 200 * increment);
  }
}

void fillZeros() {
  for (int i = 0; i < SIZE; i++) {
    vImag[i] = 0;
  }
}

void setFFTZero() {
  for (int i = 0; i < SIZE; i++) {
    fftarray[i] = 0;
  }
}


void setup() {
  // put your setup code here, to run once:
  SPI.begin();
  SPI.setClockDivider(SPI_CLOCK_DIV8);
  Serial.begin(9600);
  pinMode(micPin, INPUT);
  fillZeros();
  generateSinSignal();
  
}
 
void loop() {
  for (int i = 0; i < SIZE; i++) {

    micValue[i] = analogRead(micPin);

    micmodulated[i] = micValue[i] * miccarrier[i];

    sinemodulated[i] = sine[i] * sinecarrier[i];

    signal[i] = micmodulated[i] + sinemodulated[i];

    nums[i] = signal[i];
    fftarray[i] = signal[i];

    //Serial.println(nums[i]);
  }
  

    digitalWrite(SS, LOW);    // SS is pin 10
    SPI_writeAnything (nums);
    digitalWrite(SS, HIGH);
    delay(20);

    

    FFT.Windowing(fftarray, SIZE, FFT_WIN_TYP_HAMMING, FFT_FORWARD);
    FFT.Compute(fftarray, vImag, SIZE, FFT_FORWARD);
    FFT.ComplexToMagnitude(fftarray, vImag, SIZE);

    double peakValue = FFT.MajorPeak(fftarray, SIZE, 1000);

    counter += 1;

    if(counter == peakBin){
        Serial.print("Valor del pico: ");
        Serial.println(peakValue*deltaf);
        Serial.print(" Hz.");
        
    }
    setFFTZero();

}