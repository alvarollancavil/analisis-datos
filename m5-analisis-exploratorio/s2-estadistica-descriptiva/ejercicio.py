import pandas as pd
import matplotlib.pyplot as plt

# El fichero bancos.csv contiene las cotizaciones de los 
# principales bancos de España con : Empresa 
# (nombre de la empresa), Apertura (precio de la 
# acción a la apertura de bolsa), Máximo (precio 
# máximo de la acción durante la jornada), Mínimo 
# (precio mínimo de la acción durante la jornada), 
# Cierre (precio de la acción al cierre de bolsa), 
# Volumen (volumen al cierre de bolsa).
# Construir una función reciba el fichero bancos.csv y cree un 
# diagrama de líneas con las series temporales de las 
# cotizaciones de cierre de cada banco.
def graficar_cotizaciones_bancos(archivo):
    df = pd.read_csv(archivo)
    print(df.sample(5))
    df['Fecha'] = pd.to_datetime(df['Fecha'])
    
    for banco in df['Empresa'].unique():
        datos_banco = df[df['Empresa'] == banco]
        plt.plot(datos_banco['Fecha'].tolist(), datos_banco['Cierre'].tolist(), label=banco)

    plt.title('Cotizaciones de Cierre de Bancos')
    plt.xlabel('Fecha')
    plt.ylabel('Precio de Cierre')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

# Main
graficar_cotizaciones_bancos("bancos.csv")