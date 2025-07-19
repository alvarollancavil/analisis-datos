# Una cadena de restaurantes de comida rápida afirma que el tiempo 
# promedio que un cliente espera en la fila para ser atendido es de 3 
# minutos. Un consultor de eficiencia sospecha que el tiempo de espera 
# promedio es en realidad mayor a 3 minutos debido a nuevos procesos. 
# Para verificar esto, el consultor registra los tiempos de espera de una 
# muestra aleatoria de 40 clientes durante las horas pico en varias 
# sucursales. Los datos recopilados son los siguientes: 
# Media muestral: 3.25 minutos 
# Desviación estándar muestral: 0.8 minutos 
# Tamaño de la muestra: 40 clientes 
# Pregunta: 
# Con un nivel de significancia (a) de 0.05 (5%), ¿hay suficiente 
# evidencia para apoyar la sospecha del consultor de que el tiempo 
# promedio de espera es mayor a 3 minutos?

import scipy.stats as stats

# Datos
mediaPoblacionalH0=3
nivelSignificancia=0.05

mediaMuestral=3.25
desviacionStdMuestra=0.8
tamañoMuestra=40

# Estadistico t
t_stat=(mediaMuestral-mediaPoblacionalH0)/(desviacionStdMuestra/(tamañoMuestra**0.5))
# Grados de libertad
df=tamañoMuestra-1
# Less
#p_value=stats.t.cdf(abs(t_stat),df=df)
# Greater
p_value=(1-stats.t.cdf(abs(t_stat),df=df))

print(f"Estadistico t: {t_stat:.3f}")
print(f"P-valor (): {p_value:.3f}")
print(f"Nivel de significancia: {nivelSignificancia:.3f}")


if p_value < nivelSignificancia:
    print("Decisión: Se rechaza la hipótesis nula.")
    print(f"Conclusión: Hay suficiente evidencia para afirmar que el tiempo de espera es mayor a 3 minutos")
else:
    print("Decisión: No se rechaza la hipótesis nula.")
    print(f"Conclusión: No hay suficiente evidencia para afirmar que el tiempo de espera es mayor a 3 minutos")

# p-valor > nivelSignificancia
# No hay suficiente evidencia para rechazar H0 (El promedio de espera es 3 minutos)
