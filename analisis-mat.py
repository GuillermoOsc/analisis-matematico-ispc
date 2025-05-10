
# Replica en Python de la logica aplicada en Pseint

import matplotlib.pyplot as plt
import numpy as np

# Datos reales (en millones de $)
trimestres = [1, 2, 3, 4, 5, 6, 7, 8]
facturacion = [299316.4, 402474.4, 578164.6, 829789.3, 1320339.5, 1717379.4, 2169572.4, 2281137.9]

# Ajuste lineal
coef = np.polyfit(trimestres, facturacion, 1)
m, b = coef
print(f"Función ajustada: y = {m:.2f} * x + {b:.2f}")

# Predicción para próximos 4 trimestres
trimestres_futuros = list(range(9, 13))
prediccion = [m * x + b for x in trimestres_futuros]

# Gráfico
plt.figure(figsize=(10, 6))
plt.plot(trimestres, facturacion, marker='o', label='Datos reales')
plt.plot(trimestres_futuros, prediccion, linestyle='--', color='orange', label='Predicción')
plt.xlabel('Trimestre (desde 2023-T1)')
plt.ylabel('Facturación (millones de $)')
plt.title('Evolución de la facturación farmacéutica (INDEC)')
plt.legend()
plt.grid(True)
plt.show()
