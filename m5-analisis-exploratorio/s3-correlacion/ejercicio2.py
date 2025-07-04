import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Analicemos la relación entre la temperatura (en grados 
# Celsius) y el consumo de ropa de invierno en una tienda. 
# Datos 
# Temperatura (0C): [5, 10, 15, 20, 25, 30, 35, 40, 45, 50] 
# Consumo de Ropa de Invierno: [200, 180, 160, 140, 120, 100, 80, 60, 40, 20] 

df=pd.DataFrame({
    'Temperatura': [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],
    'Consumo de Ropa de Invierno': [200, 180, 160, 140, 120, 100, 80, 60, 40, 20]
})

# Grafica de dispersion
plt.figure(figsize=(8,6))
sns.scatterplot(x='Temperatura',y='Consumo de Ropa de Invierno',data=df)
plt.title("Correlacion Temperatura vs Consumo de Ropa de Invierno")
plt.xlabel("Temperatura")
plt.ylabel("Consumo de Ropa de Invierno")
plt.show()

# Coeficiente de correlacion
correlacion=df.corr()
print(f"Correlacion entre Temperatura y Consumo de Ropa de Invierno: {correlacion}")