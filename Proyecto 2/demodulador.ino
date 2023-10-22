const int receiverPin = A0;  // Entrada analógica del receptor
const int speakerPin = 9;    // Pin de salida al altavoz

// Frecuencia de la portadora del transmisor
const double carrierFrequency = 5000.0;  // 5 kHz

void setup() {
  pinMode(speakerPin, OUTPUT);
}

void loop() {
  // Leer la señal modulada
  int receivedSignal = analogRead(receiverPin);

  // Demodulación: Multiplicar por la portadora
  double time = millis() / 1000.0;  // Tiempo en segundos
  double carrierSignal = cos(2 * PI * carrierFrequency * time);  // Portadora
  int demodulatedSignal = receivedSignal * carrierSignal;

  // Filtro pasa bajos (media móvil) para eliminar la componente de alta frecuencia
  static int filteredSignal = 0;
  const double alpha = 0.005;  // Factor de suavizado para el filtro
  filteredSignal = alpha * demodulatedSignal + (1 - alpha) * filteredSignal;

  Serial.println(filteredSignal);

  // Enviar la señal demodulada al altavoz
  analogWrite(speakerPin, filteredSignal);
}
