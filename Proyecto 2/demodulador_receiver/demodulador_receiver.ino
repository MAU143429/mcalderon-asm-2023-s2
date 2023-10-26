#include <math.h>
#include <arduinoFFT.h>

#define SIZE 128

double nums[SIZE];
double sinecarrier[SIZE];
double miccarrier[SIZE];
double signal[SIZE];
double a[SIZE];

const int speakerPin = 9;

double amplitude =1;
double increment = twoPi / (double)SIZE;

void generateCarriers() {
  for (int i = 0; i < SIZE; i++) {
    sinecarrier[i] = amplitude * cos(increment * 2000 * i);
    miccarrier[i] = amplitude * cos(increment * 200000 * i);
  }
}

void setup() { 
  Serial.begin(9600);
  pinMode(speakerPin, OUTPUT);
  generateCarriers();
}
 
void loop() {
  // put your main code here, to run repeatedly:
String readString;
String Q = "";
 
//-------------------------------Check Serial Port---------------------------------------
 while (Serial.available()) {
    delay(10);
    if (Serial.available() > 0) {
      char c = Serial.read();  //gets one byte from serial buffer
      if (isControl(c)) {
        break;
      }
      readString += c; //makes the string readString    

    }
 }

  Q = readString;

  if(Q != ""){
    for (int i = 0; i < SIZE; i++) {

      a[i] = Q.toDouble()*10;
      
      a[i] *= sinecarrier[i];

      double filteredSignal[SIZE];

      const double alpha = 0.0002;  // Factor de suavizado para el filtro

      filteredSignal[i] = alpha * (a[i]) + (1-alpha) * a[0];

  
      Serial.println(filteredSignal[i]);
      analogWrite(speakerPin,filteredSignal[i]);
    }

  }

}