#include "max6675.h"

// Definición de los pines de conexión
int thermoDO = 4;  // SO (Data Out)
int thermoCS = 5;  // CS (Chip Select)
int thermoCLK = 6; // SCK (Serial Clock)

// Inicializamos la librería con nuestros pines
MAX6675 thermocouple(thermoCLK, thermoCS, thermoDO);

void setup() {
  // Inicializamos la comunicación serial a 9600 baudios
  Serial.begin(9600);
  
  // Damos tiempo a que el chip MAX6675 se estabilice al arrancar
  delay(500);
}

void loop() {
  // Leemos la temperatura en grados Celsius
  float temp = thermocouple.readCelsius();

  // Imprimimos ÚNICAMENTE el valor numérico.
  // Esto es crucial para que tu script de Python (Fase 2) 
  // pueda leer el dato sin tener que limpiar texto extra.
  Serial.println(temp);

  // El MAX6675 necesita un mínimo de 250ms entre lecturas para ser preciso.
  // Un muestreo de 1 segundo (1000 ms) es ideal para la inercia térmica de tu reactor.
  delay(1000);
}