import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 4. Gráfico de violín 
# Dataset: tips 
# Objetivo: Comparar distribución de propinas por 
# género. 
# Gráfica: sns.violinplot 

df=pd.read_csv("datos_propinas.csv")
print(df.sample(5))

sns.violinplot(x='sex',y='tip',data=df)
plt.show()