# Escribir una función que reciba una serie de Pandas 
# con las notas de los alumnos de un curso y devuelva 
# un diagrama de cajas con las notas. El diagrama 
# debe tener el título "Distribución de notas". 

import pandas as pd
import matplotlib.pyplot as plt

def graficar_notas(serie_notas):
    serie_notas.plot(kind='box',title='Notas del Curso',xlabel='Alumnos',ylabel='Notas')
    plt.show()

# Main
alumnos = ['Ana', 'Benjamín', 'Camila', 'Diego', 'Elisa', 'Felipe', 'Gabriela']
notas = [6.5, 5.8, 4.2, 6.9, 5.5, 3.8, 7.0]
serie_notas = pd.Series(data=notas, index=alumnos, name='Notas')

print(serie_notas)
graficar_notas(serie_notas)

