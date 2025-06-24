import pandas as pd

df=pd.read_csv("base_ventas_inconsistente.csv")
print(df.head(10))
print(df.info())

dfLaptop=df[df["Producto"]=="Laptop"]
print(dfLaptop.describe())
for index,row in dfLaptop.iterrows():
    if (pd.isnull(row["Precio_Total"])):
        dfLaptop.at[index,"Precio_Total"]=float(row["Cantidad"])*float(row["Precio_Unitario"])
print(dfLaptop.describe())

#print(dfLaptop.head(10))
#df.to_csv("base_modificada.csv",index=False)