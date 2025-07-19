# Un fabricante de baterías de litio afirma que la vida útil promedio de sus 
# baterías, en condiciones normales de uso, es de 500 horas. Un ingeniero de 
# control de calidad sospecha que esta afirmación es optimista y que la Vida 
# útil real podría ser diferente a 500 horas. Para verificarlo, decide tomar una 
# muestra aleatoria de baterías y probarlas hasta que se agoten. 
# Datos de la Muestra: 
# El ingeniero selecciona una muestra aleatoria de 25 baterías y registra sus 
# vidas útiles (en horas): 
# vidas_utiles = 
# Nivel de Significancia: 
# decide usar un nivel de significancia (a) de 0.01 (1%). 
# Tu Tarea: 
# Realiza una prueba de hipótesis en Python para determinar si la vida útil 
# promedio de las baterías es significativamente diferente de 500 horas. 

from scipy import stats
import numpy as np

muestra=[505,498,510,495,502,490,515,492,508,497,503,496,512,494,501,489,518,493,507,499,506,491,511,498,504]

mediaPoblacionalH0=500
nivelSignificancia=0.01

mediaMuestral=np.mean(muestra)
desviacionStdMuestra=np.std(muestra,ddof=1)
tamañoMuestra=len(muestra)

estadistico_t,p_value=stats.ttest_1samp(muestra,popmean=mediaPoblacionalH0,alternative='less')
print(f"Estadistico t: {estadistico_t:.3f}")
print(f"P-valor (): {p_value:.3f}")
print(f"Nivel de significancia: {nivelSignificancia:.3f}")


if p_value < nivelSignificancia:
    print("Decisión: Se rechaza la hipótesis nula.")
    print(f"Conclusión: Hay suficiente evidencia para afirmar que la vida útil promedio es menor a 500 horas")
else:
    print("Decisión: No se rechaza la hipótesis nula.")
    print(f"Conclusión: No hay suficiente evidencia para afirmar que la vida útil promedio es menor a 500 horas")

# p-valor > nivelSignificancia
# No hay suficiente evidencia para rechazar H0 (vida promedio baterias es de 500 hrs)