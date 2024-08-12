import numpy as np
import scipy.stats as stats

# Datos observados
observed = np.array([[30, 20], [10, 40]])

# Prueba de chi cuadrada para tabla de contingencia
chi2_stat, p_val, dof, expected = stats.chi2_contingency(observed)

print(f'Estadístico chi cuadrado: {chi2_stat}')
print(f'P-valor: {p_val}')
print(f'Grados de libertad: {dof}')
print('Frecuencias esperadas:')
print(expected)
