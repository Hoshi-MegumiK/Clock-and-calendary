import scipy.stats as stats

alpha = 0.05
n = 10
df = n - 1
s2 = 20

# Valores críticos de chi cuadrada
chi2_lower = stats.chi2.ppf(alpha / 2, df)
chi2_upper = stats.chi2.ppf(1 - alpha / 2, df)

# Intervalo de confianza para la varianza
ci_lower = (n - 1) * s2 / chi2_upper
ci_upper = (n - 1) * s2 / chi2_lower

print(f'Valor crítico chi cuadrada inferior (α/2): {chi2_lower}')
print(f'Valor crítico chi cuadrada superior (1-α/2): {chi2_upper}')
print(f'Intervalo de confianza para la varianza: ({ci_lower}, {ci_upper})')
