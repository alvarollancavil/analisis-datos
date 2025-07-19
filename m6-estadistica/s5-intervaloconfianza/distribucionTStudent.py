import scipy.stats as stats

mediaMuestral=52
desvEstandarMuestra=4
n=10

mediaHipotetica=50

# Estadistico t
t_stat=(mediaMuestral-mediaHipotetica)/(desvEstandarMuestra/(n**0.5))
# Grados de libertad
df=n-1
# probabilidad acumulada
p_value=2*(1-stats.t.cdf(abs(t_stat),df=df))

print(f"t= {t_stat}")
print(f"Grados libertad= {df}")
print(f"p-value= {p_value}")