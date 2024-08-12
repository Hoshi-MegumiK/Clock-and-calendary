import scipy.stats as stats

# Datos observados
observed = [8, 10, 12, 9, 11, 10]

# Datos esperados (dado justo)
expected = [10, 10, 10, 10, 10, 10]

# Cálculo del estadístico chi cuadrado y el p-valor
chi2_stat, p_val = stats.chisquare(f_obs=observed, f_exp=expected)

print(f'Estadístico chi cuadrado: {chi2_stat}')
print(f'P-valor: {p_val}')
