import numpy as np
import scipy.stats as stats

# Datos observados (tipo de incidente vs. resultado del incidente)
# Las filas representan tipos de incidentes: [malware, phishing, otros]
# Las columnas representan resultados: [sistema comprometido, intento fallido]
observed = np.array([
    [30, 10],  # malware
    [20, 25],  # phishing
    [15, 30]   # otros
])

# Prueba chi cuadrada de independencia
chi2_stat, p_val, dof, expected = stats.chi2_contingency(observed)

# Resultados
print(f'Estadístico chi cuadrada: {chi2_stat:.4f}')
print(f'P-valor: {p_val:.4f}')
print(f'Grados de libertad: {dof}')
print('Frecuencias esperadas:')
print(expected)

# Interpretación del p-valor
alpha = 0.05
if p_val < alpha:
    print(f'Como el p-valor ({p_val:.4f}) es menor que {alpha}, rechazamos la hipótesis nula.')
    print('Esto sugiere que hay una asociación entre el tipo de incidente y el resultado.')
else:
    print(f'Como el p-valor ({p_val:.4f}) es mayor que {alpha}, no podemos rechazar la hipótesis nula.')
    print('Esto sugiere que no hay suficiente evidencia para afirmar que hay una asociación entre el tipo de incidente y el resultado.')
