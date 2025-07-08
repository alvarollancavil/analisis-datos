import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 9. Gráfico de barras agrupado 
# Dataset: titanic 
# Objetivo: Comparar supervivencia por clase. 
# Gráfica: sns.barplot 

df=pd.read_csv("titanic.csv")
print(df.sample(5))

sns.barplot(x='Pclass',y='Survived',estimator='sum',data=df)
plt.show()