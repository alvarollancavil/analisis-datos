import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Analizar la relación entre horas de estudio y calificaciones de 
# un grupo de estudiantes. 
# Datos 
# Horas de Estudio:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Calificaciones: [50, 55, 60, 65, 70, 75, 80, 85, 90, 95]

df=pd.DataFrame({
    'Horas de Estudio': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Calificaciones': [50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
})

# Grafica de dispersion
plt.figure(figsize=(8,6))
sns.scatterplot(x='Horas de Estudio',y='Calificaciones',data=df)
plt.title("Correlacion Horas de Estudio vs Calificacioness")
plt.xlabel("Horas de Estudio")
plt.ylabel("Calificaciones")
plt.show()

# Coeficiente de correlacion
correlacion=df.corr()
print(f"Correlacion entre Horas de Estudio y Calificaciones: {correlacion}")