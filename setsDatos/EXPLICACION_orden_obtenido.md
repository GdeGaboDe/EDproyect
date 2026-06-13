# Orden y explicación de los sets de datos

Cada archivo `.txt` de esta carpeta contiene un set de datos obtenido durante la práctica.
A continuación se detallan las condiciones experimentales de cada prueba (P) y la cantidad
de datos registrados.

| Archivo | Temperatura | Tiempo | Volumen | Réplica | N° datos |
|---------|-------------|--------|---------|---------|----------|
| `P1_40C_1-10min_200ml_replica1.txt` | 40 °C | 1:10 min | 200 ml | Réplica 1 | 165 |
| `P2_40C_1-18.43min_200ml_replica2.txt` | 40 °C | 1:18.43 min | 200 ml | Réplica 2 | 172 |
| `P3_40C_51.45seg_100ml_replica1.txt` | 40 °C | 51.45 s | 100 ml | Réplica 1 | 98 |
| `P4_60C_2-05.12min_200ml_replica1.txt` | 60 °C | 2:05.12 min | 200 ml | Réplica 1 | 188 |
| `P5_60C_1-30.55min_100ml_replica1.txt` | 60 °C | 1:30.55 min | 100 ml | Réplica 1 | 758 |
| `P6_40C_48.34seg_100ml_replica2.txt` | 40 °C | 48.34 s | 100 ml | Réplica 2 | 168 |
| `P7_60C_2-03.17min_200ml_replica2.txt` | 60 °C | 2:03.17 min | 200 ml | Réplica 2 | 224 |
| `P8_60C_1-14.42min_100ml_replica2.txt` | 60 °C | 1:14.42 min | 100 ml | Réplica 2 | 175 |

## Notas

- En **P1** el primer valor (`28.00`) venía precedido de una `x`, interpretada como
  encabezado de columna. Dicho valor se incluyó en el archivo; si correspondía descartarlo,
  debe eliminarse.
- **P7** se corrigió a **Réplica 2**: la combinación 60 °C / 200 ml ya tiene su Réplica 1
  en **P4**, por lo que P7 corresponde necesariamente a la segunda réplica de ese tratamiento.
