#include <arduinoFFT.h>
#include <math.h>

// Definir el tamaño de la FFT
#define N 64

// Crear objeto de FFT para entrada y salida
arduinoFFT FFT = arduinoFFT();

// Frecuencia de la señal seno en Hz
int sineFrecuency = 1000; // 1 kHz

// Frecuencia de la señal coseno (portadora) en Hz
int carrierFrecuency = 5000; // 5 kHz

// Amplitud de la señal seno
int sineAmplitude = 2;

// Amplitud de la señal coseno (portadora)
int carrierAmplitude = 1;

int samplingFrecuency = 1000;

float increment = twoPi / (double)N;

// Variables para almacenar datos de entrada y salida de la FFT
double vRealSin[N];
double vRealPort[N];
double vRealModulada[N];
double vImagModulada[N];

double modulatedPeak;

//double vRealDemodulada[N];
//double vImagDemodulada[N];




void generateCarrierSignal() {
  for (int i = 0; i < N; i++) {
    double time = (double)i / (samplingFrecuency * 2);
    vRealPort[i] = carrierAmplitude * cos(2.0 * M_PI * carrierFrecuency * time);
  }
}

void generateSineSignal(){
  for (int i = 0; i < N; i++) {
    double val = sineAmplitude * sin(increment * i);
    vRealSin[i] = val; // Read the generated signal and store it in the real part
  }
}

void modulateSignals(){
  for (int i = 0; i < N; i++) {
    vRealModulada[i] = vRealSin[i]  * vRealPort[i] ; // Read the generated signal and store it in the real part
    vImagModulada[i] = 0.0 ; // Set the imaginary part to zero
  }
}

void getFFT(){
  FFT.Windowing(vRealModulada, N, FFT_WIN_TYP_HAMMING, FFT_FORWARD);
  FFT.Compute(vRealModulada, vImagModulada, N, FFT_FORWARD);
  FFT.ComplexToMagnitude(vRealModulada, vImagModulada, N);
  modulatedPeak = FFT.MajorPeak(vRealModulada, N, samplingFrecuency);
}

void plotSine(){
  for (int i = 0; i < N; i++) {
  Serial.println(vRealSin[i]);
  }
}

void plotCarrier(){
  for (int i = 0; i < N; i++) {
  Serial.println(vRealPort[i]);
  }
}

void plotFourier(){
  for (int i = 0; i < N; i++) {
  Serial.println(vRealModulada[i]);
  }
}

void setup() {
  Serial.begin(9600);

  float deltaF = samplingFrecuency/N;

  generateCarrierSignal();
  generateSineSignal();
  modulateSignals();

  plotSine();
  delay(1000);
  plotCarrier();
  delay(1000);
  plotFourier();
  delay(1000);
  getFFT();
  delay(1000);
  plotFourier();
  delay(1000);
  Serial.print("Frecuencia de modulación: " );
  Serial.print(modulatedPeak*deltaF);
  Serial.print(" Hz");
}

void loop() {
 
}
