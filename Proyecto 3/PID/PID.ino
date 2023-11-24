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


void setup() {
  // put your setup code here, to run once:

}

void loop() {
  // put your main code here, to run repeatedly:

}
