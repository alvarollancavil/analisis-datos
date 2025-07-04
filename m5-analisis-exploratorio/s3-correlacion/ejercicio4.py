# Un estudio pretende analizar si existe una correlación lineal 
# positiva entre la altura y el peso de las personas. Los datos 
# utilizados en este ejemplo se han obtenido del libro Statlstical 
# Rethinking by Richard McElreath. El set de datos contiene 
# información recogida por Nancy Howell a finales de la década 
# de 1960 sobre el pueblo !Kung San, que viven en el desierto 
# de Kalahari entre Botsuana, Namibia y Angola.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url="https://raw.githubusercontent.com/JoaquinAmatRodrigo/Estadistica-machine-learning-python/master/data/Howell1.csv"
df=pd.read_csv(url)
print(df.sample(5))

# Coeficiente de correlacion
correlacion=df.corr()
print(f"\nCorrelacion entre height y weight:\n{correlacion}")

# Grafica de dispersion
plt.figure(figsize=(8,6))
sns.scatterplot(x='height',y='weight',data=df)
plt.title("Correlacion height vs weight")
plt.xlabel("height")
plt.ylabel("weight")
plt.show()

