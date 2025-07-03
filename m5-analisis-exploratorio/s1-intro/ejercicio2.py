import pandas as pd
import matplotlib.pyplot as plt

# Escribir una función que reciba una diccionario con 
# las notas de las asignaturas de un curso y una 
# cadena con el nombre de un color y devuelva un 
# diagrama de barras de las notas en el color dado.

def graficar_notas(notas,color):
    df=pd.DataFrame(notas.items(),columns=['Asignatura','Nota'])
    df.plot(kind='bar',x='Asignatura',y='Nota',color=color,title='Notas del Curso',xlabel='Asignatura', ylabel='Nota')
    plt.show()

# Main
notas={
    'Lenguaje':6.5,
    'Matematicas':6.1,
    'Historia':6.5,
    'Futbol':7.0,
    'Ingles':5.5
}
color=input("Ingresar color: ")
graficar_notas(notas,color)