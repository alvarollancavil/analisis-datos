import pandas as pd

def estadisticas(df):
    df["Final"]=df['Final'].str.replace(',', '.').astype(float)
    df["Máximo"]=df['Máximo'].str.replace(',', '.').astype(float)
    df["Mínimo"]=df['Mínimo'].str.replace(',', '.').astype(float)
    df["Volumen"]=df['Volumen'].str.replace('.', '').astype(float)
    df["Efectivo"]=df['Efectivo'].str.replace(',', '.').astype(float)
    return df.describe().loc[['min', 'max','mean']]

df=pd.read_csv("cotizacion.csv",sep=";")
print(estadisticas(df))