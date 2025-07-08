import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 10. Gráfico de líneas 
# Dataset: Datos generados 
# Objetivo: Mostrar la evolución de ventas mensuales. 
# Gráfica: sns.lineplot 

df=pd.read_csv("ventas_mensuales.csv")
print(df.sample(5))

sns.lineplot(x='mes',y='ventas',data=df)

plt.xticks(rotation=45)
plt.title('Ventas por mes')
plt.show()