# Se quiere estudiar la relación entre las variables precio y peso 
# de los automóviles. Se sospecha que esta relación podría 
# estar influenciada por la variable potencia del motor, ya que a 
# mayor peso del vehículo se r€quiere mayor potencia y, a su 
# vez, motores más potentes son más caros. 

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url="https://raw.githubusercontent.com/JoaquinAmatRodrigo/Estadistica-machine-learning-python/master/data/Cars93.csv"
df=pd.read_csv(url)
print(df.sample(5))

# Coeficiente de correlacion
correlacion=df[['Price','Weight']].corr()
print(f"\nCorrelacion entre Price y Weight:\n{correlacion}")

# Grafica de dispersion
plt.figure(figsize=(8,6))
sns.scatterplot(x='Price',y='Weight',data=df)
plt.title("Correlacion Price vs Weight")
plt.xlabel("Price")
plt.ylabel("Weight")
plt.show()