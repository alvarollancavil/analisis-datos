import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 8. Stripplot (Gráfico de dispersión por categorías) 
# Dataset: tips 
# Objetivo: Visualizar propinas por tipo de cliente 
# (fumador/no fumador). 
# Gráfica: sns.stripplot 

df=pd.read_csv("datos_propinas.csv")
print(df.sample(5))

sns.stripplot(x='smoker',y='tip',data=df)
plt.show()