# Escribir una función que reciba un dataframe de 
# Pandas con los ingresos y gastos de una empresa 
# por meses y devuelva un diagrama de líneas con dos 
# líneas, una para los ingresos y otra para los gastos. 
# El diagrama debe tener una leyenda identificando la 
# línea de los ingresos y la de los gastos, un título con el
# nombre "Evolución de ingresos y gastos" y el eje y 
# debe empezar en 0

import pandas as pd
import matplotlib.pyplot as plt


def graficar_ingresos_gastos(df):
    df.plot(x='Mes',y=['Ingresos','Gastos'],kind='line')
    plt.title("Evolución de ingresos y gastos")
    plt.xlabel('Mes')
    plt.ylabel('Cantidad')
    plt.legend(['Ingresos','Gastos'])
    plt.ylim(0, df[['Ingresos', 'Gastos']].max().max() * 1.1) 
    plt.show()

# Main
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
         'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
ingresos = [12000, 11500, 13000, 12500, 14000, 13500, 15000, 14500, 13800, 14200, 14800, 15500]
gastos   = [8000, 8500, 7900, 8200, 8700, 9000, 8900, 9100, 8600, 8800, 8700, 9200]
df = pd.DataFrame({
    'Mes': meses,
    'Ingresos': ingresos,
    'Gastos': gastos
})

print(df)
graficar_ingresos_gastos(df)
