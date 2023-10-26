//Enviar
#include <arduinoFFT.h>
#define SIZE 128

const int micPin = A0;
double amplitude =1;
double increment = twoPi / (double)SIZE;
double nums[SIZE];

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


void setup() {
  // put your setup code here, to run once:
  Serial1.begin(9600);
  Serial.begin(9600);
  pinMode(micPin, INPUT);
  generateSinSignal();
}
 
void loop() {
  for (int i = 0; i < SIZE; i++) {
    micValue[i] = analogRead(micPin);
    micmodulated[i] = micValue[i] * miccarrier[i];
    sinemodulated[i] = sine[i] * sinecarrier[i];
    signal[i] = micmodulated[i] + sinemodulated[i];
    nums[i] = signal[i];
    
    delay(100);
    Serial1.print(nums[i]);
    Serial.println(nums[i]);
    Serial.print(","); // Agrega una coma para separar los valores
  }
}