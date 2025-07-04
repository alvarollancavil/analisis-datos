import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)

temperaturas=np.random.normal(loc=25,scale=5,size=30)
heladosVendidos=3*temperaturas+np.random.normal(loc=0,scale=10,size=30)

df=pd.DataFrame({
    'Temperatura':temperaturas,
    'Helados vendidos':heladosVendidos
})

# Grafica de dispersion
plt.figure(figsize=(8,6))
sns.scatterplot(x='Temperatura',y='Helados vendidos',data=df)
plt.title("Correlacion Temp vs Helados vendidos")
plt.xlabel("Temperatura °C")
plt.ylabel("Helados vendidos")
plt.show()

# Coeficiente de correlacion
correlacion=df.corr()
print(f"Correlacion entre Temperatura y Helados vendidos: {correlacion}")