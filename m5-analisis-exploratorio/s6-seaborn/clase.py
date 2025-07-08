import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data={''
'Categoria':['A','A','B','B','C','C','A','B','A','C'],
'valor':[10,12,15,13,18,16,11,14,17,18]
}
df=pd.DataFrame(data)

# Grafica de barras
sns.barplot(x='Categoria',y='valor',data=df)
plt.show()

# Grafico de conteo
sns.countplot(x='Categoria',data=df)
plt.show()

# Grafico de caja
sns.boxplot(x='Categoria',y='valor',data=df)
plt.show()

# Diagrama de violin
sns.violinplot(x='Categoria',y='valor',data=df)
plt.show()

# Grafica de enjambre
sns.swarmplot(x='Categoria',y='valor',data=df)
plt.show()

