/////////////////////////////////////////////    
//    Instituto Tecnológico de Costa Rica  //
//       Análisis de Señales Mixtas        //
//                                         //
//           Controlador PID               //
//                                         //
//        Jose Pablo Ramos Madrigal        //
//        Harold Espinoza Matarrita        //
//       Mauricio Calderon Chavarría       //
//       Jose Antonio Espinoza Chavez      //
/////////////////////////////////////////////

// Se defienen los pines para la entrada de los valores de los potenciometros 
int potPrincipal = A3;         
int potPlato = A4;    

// Se defienen variables para almacenar los valores leidos de los potenciometros
int valPotPrincipal = 0;
int valPotPlato = 0;

// Se establecen los valores de los coeficientes del PID
float kp = 0.2;
float ki = 0.00000;
float kd = 2.00;

// serviran para almacenar el valor que da el potenciometro (interpretado como valor angular de la posicion del potenciometro)
float theta, thetaPlato;

// Permitira guardar el valor de tiempo actual asi como el anterior
int dt
unsigned long t;
unsigned long tPrev = 0;

// Estas varibles van a almacenar los valores para el calculo de la integral
// actual y el de la anterior asi como el error actual y el anterior.
int valPrev = 0;
float e, ePrev = 0;
float inte, intePrev = 0;

// Establece los valores para el voltaje maximo y minimo asi como el valor inicial de V 
float Vmax = 12;
float Vmin = -12;
float V = 0.1;

// Se establecen los pines para comunicación con el Driver que controla el motor
// Un pin habilitador (enable)
// Dos pines controladores (Gira derecha, Gira izquierda)
const byte pinPWM  = 6;
const byte pinDirMotor1 = 7;
const byte pinDirMotor2 = 8;

/ Permite enviar la señal para que funcione el motor
// Se basa en la dirección de giro e indica un valor  
// analógico para establece la velocidad
void controlDriverVoltage(float V, float Vmax) {
  int valPWM = int(255 * abs(V) / Vmax);
  if (valPWM > 255) {
    valPWM = 255;
  }
  if (V > 0) {
    digitalWrite(pinDirMotor1, HIGH);
    digitalWrite(pinDirMotor2, LOW);
  }
  else if (V < 0) {
    digitalWrite(pinDirMotor1, LOW);
    digitalWrite(pinDirMotor2, HIGH);
  }
  else {
    digitalWrite(pinDirMotor1, LOW);
    digitalWrite(pinDirMotor2, LOW);
  }
  analogWrite(pinPWM, valPWM);

}

void setup() {

  // Se establece el puerto serial y los pines para controlar el motor usando el L298N
  Serial.begin(9600);
  pinMode(pinDirMotor1, OUTPUT);
  pinMode(pinDirMotor2, OUTPUT);

}

void loop() {
  /// Se lee los valores de Vout de cada potenciometro
  valPotPrincipal = analogRead(potPrincipal);                           
  valPotPlato = analogRead(potPlato); 

  // permite establecer el tiempo del sistema asi como realizar el calculo basico del delta t               
  t = millis();
  dt = (t - tPrev);

  // Se almacenan los valores de Vout que representan la posicion angular del motor
  // y del potenciometro principal.

  theta = valPotPrincipal;                                        
  thetaPlato = valPotPlato;                              

  // Se calcula el error sencillo (Valor del potenciometro del plato - valor del potenciometro principal)
  e = thetaPlato - theta;                                



  // Se realiza el calculo de la integral haciendo uso del metodo del trapezoide.
  inte = intePrev + (dt * (e + ePrev) / 2);         

  // Se hace el calculo del valor de V utilizando la formula del modelo del PID y los coeficientes establecidos
  V = kp * e + ki * inte + (kd * (e - ePrev) / dt) ; 

  if (V > Vmax) {
      V = Vmax;
      inte = intePrev;
    }
    if (V < Vmin) {
      V = Vmin;
      inte = intePrev;
      valPrev= valPotPrincipal;
    }
    
  WriteDriverVoltage(V, Vmax);
  Serial.println(Theta_d); Serial.print(" \t");
  Serial.print(Theta); Serial.print(" \t ");
  tPrev = t;
  intePrev = inte;
  ePrev = e;
  delay(10);

}
