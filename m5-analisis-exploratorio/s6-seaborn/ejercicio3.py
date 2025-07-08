import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 3. Boxplot para comparación de categorías 
# Dataset: tips 
# Objetivo: Comparar el total de la cuenta por día de la 
# semana. 
# Gráfica: sns.boxplot 

df=pd.read_csv("datos_propinas.csv")
print(df.sample(5))

sns.boxplot(x='day',y='total_bill',data=df)
plt.show()