# Escribir una función que reciba una serie de Pandas 
# con el número de ventas de un producto por años y 
# una cadena con el tipo de gráfico a generar (lineas, 
# barras, sectores, areas) y devuelva un diagrama del 
# tipo indicado con la evolución de las ventas por años 
# y con el título "Evolución del número de ventas".

import pandas as pd
import matplotlib.pyplot as plt

def graficar_ventas(serie_ventas,tipo_grafico):
    if tipo_grafico not in ['line','bar','pie','area']:
        raise ValueError("Tipo de gráfico no válido.")
    serie_ventas.plot(kind=tipo_grafico,title='Evolución del número de ventas',xlabel='Año',ylabel='Ventas')
    plt.show()

# Main
anios = [2020, 2021, 2022, 2023, 2024]
ventas_anuales = [1200, 1350, 1600, 1500, 1700]
serie_ventas_anuales = pd.Series(data=ventas_anuales, index=anios, name='Ventas')
tipo_grafico=input("Ingresar tipo de grafico (line,bar,pie,area): ")
graficar_ventas(serie_ventas_anuales,tipo_grafico)
print(serie_ventas_anuales)

