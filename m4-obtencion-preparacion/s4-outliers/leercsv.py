import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv("base_ventas_inconsistente.csv")
dfLaptop=df[df["Producto"]=="Laptop"]

sns.boxplot(x=dfLaptop["Metodo_Pago"],y=dfLaptop["Precio_Total"],data=dfLaptop)
plt.title("Metodo_Pago vs Fecha")
plt.show()