import matplotlib.pyplot as plt
import numpy as np

# Data extracted from your Table 2
tiempos_100ml = [51.45, 48.34]
tiempos_200ml = [70.00, 78.43]

# --- DIAGRAM 1: BOXPLOT (ANOVA Visualization) ---
plt.figure(figsize=(8, 6))
plt.boxplot([tiempos_100ml, tiempos_200ml], labels=['100 ml', '200 ml'], patch_artist=True,
            boxprops=dict(facecolor='lightblue', color='black'),
            medianprops=dict(color='red', linewidth=2))
plt.title('Spread of Thermal Convergence Times by Volume')
plt.ylabel('Time (seconds)')
plt.xlabel('Treatment (Water Volume)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('boxplot_anova.png', dpi=300)
plt.show()

# --- DIAGRAM 2: HEATING CURVES (Device Physics) ---
# Since Python captured exact times, we simulate a representative linear thermal slope
plt.figure(figsize=(8, 6))
# 100 ml (Fast)
tiempo_100_1 = np.linspace(0, 51.45, 10)
temp_100_1 = np.linspace(20.50, 40, 10)
tiempo_100_2 = np.linspace(0, 48.34, 10)
temp_100_2 = np.linspace(20.50, 40, 10)

# 200 ml (Slow)
tiempo_200_1 = np.linspace(0, 70.00, 10)
temp_200_1 = np.linspace(28.00, 40, 10)
tiempo_200_2 = np.linspace(0, 78.43, 10)
temp_200_2 = np.linspace(20.00, 40, 10)

plt.plot(tiempo_100_1, temp_100_1, 'b-', marker='o', label='P3 (100ml)')
plt.plot(tiempo_100_2, temp_100_2, 'b--', marker='s', label='P6 (100ml)')
plt.plot(tiempo_200_1, temp_200_1, 'r-', marker='^', label='P1 (200ml - Start at 28°C)')
plt.plot(tiempo_200_2, temp_200_2, 'r--', marker='x', label='P2 (200ml)')

plt.axhline(y=40, color='g', linestyle=':', label='Target 40°C')
plt.title('Overlay of Heating Curves (Thermal Inertia)')
plt.ylabel('Temperature (°C)')
plt.xlabel('Time (seconds)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.savefig('curvas_calentamiento.png', dpi=300)
plt.show()