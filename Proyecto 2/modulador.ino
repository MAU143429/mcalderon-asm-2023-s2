#include <arduinoFFT.h>

const int micPin = A0;    // Entrada analógica del micrófono
const int receptor1Pin = 9;  // Pin de salida al receptor

arduinoFFT FFT = arduinoFFT();  // Objeto de la librería arduinoFFT

double N = 256;

void setup() {
  Serial.begin(9600);

  pinMode(micPin, INPUT);
  pinMode(receptor1Pin, OUTPUT);
}

void loop() {

  unsigned long tiempo = millis();

  // Leer el valor del micrófono
  double micValue = analogRead(micPin);

  // Crear señal portadora para el micrófono (tono seno de 1 kHz)
  double carrierMic = cos(2 * PI * 5000 * millis() / 1000.0) * 127 + 128; // Frecuencia de portadora para el micrófono

  // Modular la señal del micrófono con la portadora
  double modulatedMic = micValue * carrierMic;

  double sine = 1 * sin(2 * PI * 10 * millis() / 1000.0) * 127 + 128; //"pista de auido"

  // Crear señal portadora para el audio (tono seno de 1 kHz)
  double carrierAudio = cos(2 * PI * 5000 * millis() / 1000.0) * 127 + 128; // Frecuencia de portadora para el audio

  // Modular la muestra de audio con la portadora
  double modulatedAudio = sine * carrierAudio;

  // Sumar las señales moduladas
  double transmittedSignal = modulatedMic + modulatedAudio;

  // Enviar la señal modulada al altavoz
  analogWrite(receptor1Pin, transmittedSignal);
}
