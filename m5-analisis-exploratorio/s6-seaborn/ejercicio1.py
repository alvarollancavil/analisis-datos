import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 1. Gráfico de dispersión (Scatter Plot) 
# Dataset: iris 
# Objetivo: Graficar la relación entre el largo y el ancho 
# de los pétalos. 
# Gráfica: sns.scatterplot

df=pd.read_csv("datos_iris.csv")
print(df.sample(5))

sns.scatterplot(x='petal_length',y='petal_width',data=df)
plt.show()