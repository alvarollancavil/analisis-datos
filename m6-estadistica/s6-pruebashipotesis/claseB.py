# EJEMPLO PRÁCTICO 
# Una compañía de celulares afirma que el 70% de sus clientes están "muy 
# satisfechos" con el servicio al cliente. Un consultor independiente sospecha que 
# esta proporción es en realidad menor. Para investigar, realiza una encuesta a una 
# muestra aleatoria de 150 clientes y encuentra que 95 de ellos están "muy 
# satisfechos" 
# Pregunta: ¿Hay suficiente evidencia para refutar la afirmación de la compañía a u 
# nivel de significancia del 1%? 

import statsmodels.api as sm
import numpy as np

hipotesisNula=0.7
nivelSignificancia=0.01

numeroExitos=95
tamañoMuestra=150
proporcionMuestral=numeroExitos/tamañoMuestra

print(f"Proporcion muestral: {proporcionMuestral:.3f}")

z_statistic,p_value=sm.stats.proportions_ztest(count=numeroExitos,nobs=tamañoMuestra,value=hipotesisNula,alternative='smaller')

print(f"z_statistic: {z_statistic:.3f}")
print(f"Valor-p: {p_value:.4f}")
print(f"Nivel de significancia: {nivelSignificancia:.3f}")

if p_value<nivelSignificancia:
    print(f"Se rechaza la hipotesis nula.") 
    # Hay evidencia estadistica para afirmar que la proporcion de clientes muy satisfechos es menor al 0.7
else:
    print(f"No se rechaza la hipotesis nula.") 
    # No hay suficiente evidencia para afirmar que la proporcion de clientes satisfechos es menor al 0.7 a un nivel de significnacia de 0.01
    # La diferencvia encotrada podria deberse al azar
    
    # a menor significancia se requieren mas datos para determinar si H0 es correcta o no