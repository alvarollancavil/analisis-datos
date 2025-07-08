import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 7. Pairplot 
# bataset: iris 
# Objetivo: Explorar relaciones entre múltiples 
# variables. 
# Gráfica: sns.pairplot 

df=pd.read_csv("datos_iris.csv")
print(df.sample(5))

sns.pairplot(data=df, hue='species')

plt.show()
