import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 2. Histograma de distribución 
# Dataset: tips 
# Objetivo: Mostrar la distribución de los montos de 
# propinas. 
# Gráfica: sns.histplot 

df=pd.read_csv("datos_propinas.csv")
print(df.sample(5))

sns.histplot(x='tip', bins=9, kde=True, data=df, )
plt.show()
