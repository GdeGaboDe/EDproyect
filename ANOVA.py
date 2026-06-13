"""
ANOVA de un factor — Efecto del volumen de agua sobre el tiempo de
calentamiento hasta 40 C.

Factor (variable independiente): Volumen de agua (100 ml vs 200 ml).
Respuesta (variable dependiente): Tiempo de convergencia termica en segundos.

Solo se analizan las corridas a 40 C:
    100 ml -> P3 (replica 1), P6 (replica 2)
    200 ml -> P1 (replica 1), P2 (replica 2)
"""

from scipy import stats

# Tiempos de convergencia a 40 C, en segundos (coinciden con Graficas.py).
# P1 = 1:10 min = 70.00 s ; P2 = 1:18.43 min = 78.43 s
tiempos_100ml = [51.45, 48.34]   # P3, P6
tiempos_200ml = [70.00, 78.43]   # P1, P2

# --- Estadistica descriptiva ---
print("=== ANOVA de un factor: Volumen vs Tiempo de calentamiento a 40 C ===\n")
for nombre, datos in (("100 ml", tiempos_100ml), ("200 ml", tiempos_200ml)):
    media = sum(datos) / len(datos)
    print(f"{nombre}: datos={datos}  media={media:.2f} s  n={len(datos)}")

# --- Prueba F (ANOVA de un factor) ---
f_stat, p_value = stats.f_oneway(tiempos_100ml, tiempos_200ml)

print("\n--- Resultados de la prueba F ---")
print(f"Estadistico F : {f_stat:.4f}")
print(f"p-valor       : {p_value:.4f}")

alpha = 0.05
print(f"\nNivel de significancia (alpha): {alpha}")
if p_value < alpha:
    print("Decision: se RECHAZA H0.")
    print("El volumen de agua tiene un efecto estadisticamente significativo")
    print("sobre el tiempo de calentamiento hasta 40 C.")
else:
    print("Decision: NO se rechaza H0.")
    print("No hay evidencia estadistica suficiente de que el volumen afecte")
    print("el tiempo de calentamiento hasta 40 C (con n=2 por grupo, la potencia")
    print("de la prueba es muy limitada).")