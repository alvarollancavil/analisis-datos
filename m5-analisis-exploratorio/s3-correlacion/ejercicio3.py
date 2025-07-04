import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Evaluemos si existe alguna relación entre la edad de una 
# persona y el número de libros leídos al año. 
# Datos 
# Edad (años): [23, 30, 45, 22, 34, 29, 40, 28, 35, 31, 27, 38, 33, 26, 24] 
# Número de Libros Leídos al Año: [5, 3, 6, 6, 4, 3, 7, 2, 8, 3, 4, 6, 7, 3, 4]

df=pd.DataFrame({
    'Edad': [23, 30, 45, 22, 34, 29, 40, 28, 35, 31, 27, 38, 33, 26, 24],
    'Número de Libros Leídos al Año': [5, 3, 6, 6, 4, 3, 7, 2, 8, 3, 4, 6, 7, 3, 4]
})

# Grafica de dispersion
plt.figure(figsize=(8,6))
sns.scatterplot(x='Edad',y='Número de Libros Leídos al Año',data=df)
plt.title("Correlacion Edad vs Número de Libros Leídos al Año")
plt.xlabel("Edad")
plt.ylabel("Número de Libros Leídos al Año")
plt.show()

# Coeficiente de correlacion
correlacion=df.corr()
print(f"Correlacion entre Edad y Número de Libros Leídos al Año: {correlacion}")