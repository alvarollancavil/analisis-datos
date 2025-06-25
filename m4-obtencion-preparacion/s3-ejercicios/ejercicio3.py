import pandas as pd
import numpy as np


# Ejercicio 3-1
print("="*80 + "\n Ejercicio 3-1 \n" + "="*80)
emisiones2016=pd.read_csv('emisiones-2016.csv',sep=';')
emisiones2017=pd.read_csv('emisiones-2017.csv',sep=';')
emisiones2018=pd.read_csv('emisiones-2018.csv',sep=';')
emisiones2019=pd.read_csv('emisiones-2019.csv',sep=';')
df= pd.concat([emisiones2016,emisiones2017,emisiones2018,emisiones2019], axis=0, ignore_index=True)

print(df.info())

# Ejercicio 3-2 
print("="*80 + "\n Ejercicio 3-2 \n" + "="*80)
df=df[[
    'ESTACION','MAGNITUD','ANO','MES',
    'D01','D02','D03','D04','D05','D06','D07','D08','D09','D10',
    'D11','D12','D13','D14','D15','D16','D17','D18','D19','D20',
    'D21','D22','D23','D24','D25','D26','D27','D28','D29','D30','D31'
    ]]

print(df.info())

# Ejercicio 3-3
print("="*80 + "\n Ejercicio 3-3 \n" + "="*80)
df = df.melt(id_vars=['ESTACION', 'MAGNITUD', 'ANO', 'MES'], var_name='DIA', value_name='VALOR')

print(df.info())
print(df.head(5))

# Ejercicio 3-4
print("="*80 + "\n Ejercicio 3-4 \n" + "="*80)

df["DIA"]=df['DIA'].str.replace('D', '').astype(int)
df["FECHA"]=df["ANO"].apply(str)+"-"+df["MES"].apply(str)+"-"+df["DIA"].apply(str)
df['FECHA'] = pd.to_datetime(df.FECHA, format='%Y-%m-%d', infer_datetime_format=True, errors='coerce')
print(df.info())
print(df.head(5))

# Ejercicio 3-5
print("="*80 + "\n Ejercicio 3-5 \n" + "="*80)
df=df.drop(df[np.isnat(df.FECHA)].index)
df=df.sort_values(by=['ESTACION','MAGNITUD','FECHA'])

print(df.info())
print(df.head(5))

# Ejercicio 3-6
print("="*80 + "\n Ejercicio 3-6 \n" + "="*80)
estacionesList=df['ESTACION'].unique()
contaminantesList=df['MAGNITUD'].unique()

print(f"Estaciones disponibles:\n{estacionesList}")
print(f"Contaminantes (Magnitud) disponibles:\n{contaminantesList}")

# Ejercicio 3-7
print("="*80 + "\n Ejercicio 3-7 \n" + "="*80)

def contaminantePorEstacionFecha(contaminante,estacion,fechaInicial,fechaFinal):
    inicio=pd.to_datetime(fechaInicial)
    fin=pd.to_datetime(fechaFinal)
    df_filt=df[(df['MAGNITUD']==contaminante) & (df['ESTACION']==estacion) & (df['FECHA']>=inicio) & (df['FECHA']<=fin)]
    return df_filt['VALOR'].to_list()

contaminante=12
estacion=18
fechaInicial='2016-02-01'
fechaFinal='2016-02-28'
print(f"contaminante: {contaminante}\nestacion: {estacion}\nfechaInicial: {fechaInicial}\nfechaFinal: {fechaFinal}")
print(contaminantePorEstacionFecha(contaminante,estacion,fechaInicial,fechaFinal))