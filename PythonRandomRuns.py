import pandas as pd
import numpy as np
# Definir los factores y niveles
factor_a = [40, 60]   # Set-point en °C
factor_b = [100, 200] # Volumen en ml
# Crear las 4 combinaciones base (Diseño 2^2)
combinaciones = []
for a in factor_a:
    for b in factor_b:
        combinaciones.append({'Set_Point_C': a, 'Volumen_ml': b})
# Convertir a DataFrame y duplicar para tener 2 réplicas (8 corridas)
df = pd.DataFrame(combinaciones)
df = pd.concat([df, df], ignore_index=True)
df['Replica'] = [1, 1, 1, 1, 2, 2, 2, 2]
# ALEATORIZAR el orden (Requisito de la rúbrica)
df_random = df.sample(frac=1, random_state=42).reset_index(drop=True)
df_random.index += 1 # Para que empiece en la corrida 1
print("--- ORDEN DEL EXPERIMENTO ALEATORIZADO ---")
print("Sigue estrictamente este orden en el laboratorio:")
print(df_random)
print("\nNota: Anota el 'Tiempo (segundos)' que tardas en llegar al Set-Point en cada corrida.")