# Análisis de Tiempos de Convergencia Térmica — Diseño Factorial 2²

**Autores:** Gabriel De Anda Romero, Isaac Sánchez Camacho, Mauro Salinas Jiménez.
**Materia:** Diseño Experimental para Ingenieros en Inteligencia Artificial.

## Descripción del Proyecto

Este repositorio contiene el código fuente, la lógica de instrumentación y el conjunto
de datos de un **diseño experimental factorial 2²**. El objetivo es evaluar
cuantitativamente el efecto de dos factores sobre el tiempo de calentamiento del agua:

- **Factor A — Set-point (temperatura objetivo):** 40 °C y 60 °C.
- **Factor B — Volumen de agua:** 100 ml y 200 ml.

Con 2 réplicas por combinación se obtienen **8 corridas experimentales**, ejecutadas en
orden aleatorizado. El proyecto integra hardware de adquisición de datos en tiempo real
(Arduino UNO + termopar) con procesamiento estadístico y visualización en Python,
comprobando físicamente el principio de inercia térmica.

## Arquitectura de Hardware y Conexiones

El sistema de recolección utiliza un microcontrolador **Arduino UNO**, que interactúa con
un módulo amplificador **MAX6675** y un **termopar Tipo K** mediante el bus SPI.

Para replicar el experimento, asegure las conexiones en los siguientes pines (definidos en
`CodeElectrónica.ino`):

| Módulo MAX6675 | Pin Arduino UNO | Función SPI |
| :---: | :---: | :---: |
| **VCC** | 5V | Alimentación |
| **GND** | GND | Tierra |
| **SCK** | D6 | Serial Clock |
| **CS**  | D5 | Chip Select |
| **SO**  | D4 | Serial Out (MISO) |

*(Nota: respete la polaridad de las terminales del termopar en las borneras del MAX6675).*

El firmware imprime únicamente el valor numérico de temperatura por el puerto serie a
**9600 baudios**, con un muestreo de 1 segundo entre lecturas.

## Estructura del Repositorio

- `CodeElectrónica.ino` — Sketch de Arduino para la lectura del termopar vía MAX6675.
- `PythonRandomRuns.py` — Genera el diseño factorial 2² y **aleatoriza** el orden de las
  8 corridas (requisito de la rúbrica).
- `Graficas.py` — Genera las visualizaciones: boxplot de tiempos de convergencia por
  volumen y superposición de curvas de calentamiento.
- `setsDatos/` — Capturas de datos crudos de cada réplica (un `.txt` por corrida) más
  `EXPLICACION_orden_obtenido.md`, que documenta las condiciones de cada set.

### Sets de datos

Cada archivo de `setsDatos/` contiene las lecturas de temperatura (°C) de una corrida:

| Archivo | Set-point | Volumen | Réplica | Tiempo registrado |
|---------|-----------|---------|---------|-------------------|
| `P1_40C_1-10min_200ml_replica1.txt`     | 40 °C | 200 ml | 1 | 1:10 min |
| `P2_40C_1-18.43min_200ml_replica2.txt`  | 40 °C | 200 ml | 2 | 1:18.43 min |
| `P3_40C_51.45seg_100ml_replica1.txt`    | 40 °C | 100 ml | 1 | 51.45 s |
| `P4_60C_2-05.12min_200ml_replica1.txt`  | 60 °C | 200 ml | 1 | 2:05.12 min |
| `P5_60C_1-30.55min_100ml_replica1.txt`  | 60 °C | 100 ml | 1 | 1:30.55 min |
| `P6_40C_48.34seg_100ml_replica2.txt`    | 40 °C | 100 ml | 2 | 48.34 s |
| `P7_60C_2-03.17min_200ml_replica1.txt`  | 60 °C | 200 ml | 1 | 2:03.17 min |
| `P8_60C_1-14.42min_100ml_replica2.txt`  | 60 °C | 100 ml | 2 | 1:14.42 min |

Consulte `setsDatos/EXPLICACION_orden_obtenido.md` para el detalle completo y notas.

## Instrucciones de Ejecución e Instalación

### 1. Preparación del Hardware

1. Ensamble el circuito conforme a la tabla de conexiones SPI.
2. Conecte el Arduino UNO a la computadora por USB.
3. Use el *Arduino IDE* para compilar y cargar `CodeElectrónica.ino` en la placa. Verifique
   que el Monitor Serie esté configurado a **9600 baudios**.

### 2. Configuración del Entorno Python

Se requiere Python 3.x. Instale las dependencias de análisis y visualización:

```bash
pip install pandas numpy matplotlib
```

### 3. Generación del Orden Aleatorizado

Antes de tomar datos en el laboratorio, obtenga el orden de las corridas:

```bash
python PythonRandomRuns.py
```

### 4. Visualización de Resultados

Para generar el boxplot y las curvas de calentamiento a partir de los tiempos registrados:

```bash
python Graficas.py
```

El script exporta `boxplot_anova.png` y `curvas_calentamiento.png`.
