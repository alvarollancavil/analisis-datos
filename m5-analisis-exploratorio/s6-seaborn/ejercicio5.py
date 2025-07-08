import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 5. Heatmap de correlación 
# Dataset: iris 
# Objetivo: Visualizar las correlaciones entre variables 
# numéricas. 
# Gráfica: sns.heatmap 

df=pd.read_csv("datos_iris.csv")
print(df.sample(5))

correlacion=df[['sepal_length','sepal_width','petal_length','petal_width']].corr()
print(correlacion)

sns.heatmap(correlacion, annot=True, cmap='coolwarm', fmt='.2f')

plt.title('Matriz de correlación')
plt.show()

