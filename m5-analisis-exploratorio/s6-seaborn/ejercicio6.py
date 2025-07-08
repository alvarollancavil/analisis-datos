import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 6. Countplot (conteo de categorías) 
# Dataset: titanic 
# Objetivo: Mostrar cantidad de pasajeros por clase. 
# Gráfica: sns.countplot 

df=pd.read_csv("titanic.csv")
print(df.sample(5))

sns.countplot(x='Pclass',data=df)
plt.show()