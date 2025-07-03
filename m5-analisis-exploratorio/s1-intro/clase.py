import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("base_ventas_inconsistente.csv")
print(df.sample(5))

#df.hist()
#sns.boxplot(x=df['Precio_Total'])
df_plt=df.filter(items=['Precio_Total','Moneda'])
sns.pairplot(df_plt,hue='Moneda')

plt.show()