# Ejemplo Practico: 
# Una empresa de refrescos afirma que sus botellas contienen un promedio de 
# 500 ml de líquido. Un grupo de consumidores sospecha que el contenido 
# promedio real es menor. Deciden realizar una prueba de hipótesis para verificar 
# esta afirmación. 

from scipy import stats
import numpy as np

muestra=np.array([497.1,499.0,498.5,496.8,500.2,497.9,498.8,497.5,499.3,498.0,
                  497.6,499.1,498.3,496.5,500.5,497.2,498.6,497.8,499.5,498.1,
                  497.0,498.9,497.4,499.2,498.7,497.3,496.9,500.0,498.4,497.7,])

mediaPoblacionalH0=500
nivelSignificancia=0.05 # alpha

mediaMuestral=np.mean(muestra)
desviacionStdMuestra=np.std(muestra,ddof=1)
tamañoMuestra=len(muestra)

print(f"Media muestra: {mediaMuestral:.2f}")
print(f"DesviacionStd muestra: {desviacionStdMuestra:.2f}")
print(f"Tamaño muestra: {tamañoMuestra:.2f}")
print(f"Nivel de significancia: {nivelSignificancia:.2f}")

estadistico_t,p_valor_bilateral=stats.ttest_1samp(muestra,popmean=mediaPoblacionalH0,alternative='less')

print(f"Estadistico t: {estadistico_t:.3f}")
print(f"P-valor (unilateral a la izquierda): {p_valor_bilateral:.3f}")

# Decision
# P-valor <= nivelSignificancia
# Se rechaza H0 (no hay evidencia suficiente para afirmar qu la mediaPobl es menor 500)