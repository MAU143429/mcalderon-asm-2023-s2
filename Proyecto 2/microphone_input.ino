const int pinMicrofono = A0;  // Puerto analógico al que está conectado el micrófono
unsigned long previousMillis = 0;
const long interval = 100;  // Intervalo de tiempo en milisegundos

void setup() {
  Serial.begin(9600);  // Inicializa la comunicación serial
}

void loop() {
  unsigned long currentMillis = millis();
  if (currentMillis - previousMillis >= interval) {
    previousMillis = currentMillis;
    
    int valorMicrofono = analogRead(pinMicrofono);  // Lee el valor analógico del micrófon
    Serial.print("\t");
    Serial.println(valorMicrofono);  // Envía el valor por la comunicación serial
  }
}
