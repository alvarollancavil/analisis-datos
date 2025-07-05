import pandas as pd
from sklearn.linear_model  import LinearRegression

df=pd.DataFrame({
    'Horas de estudio':[10,8,15,5,12],
    'Asistencia':[90,85,95,60,85],
    'Participacion':[8,7,9,6,8],
    'Nota final':[85,75,95,60,88]
})

x=df[['Horas de estudio','Asistencia','Participacion']]
y=df['Nota final']

modelo=LinearRegression()
modelo.fit(x,y)

print(f"Coeficientes: {modelo.coef_}")
print(f"Interseccion: {modelo.intercept_}")

#nuevo_estudiante=[[11,88,9]]
nuevo_estudiante=pd.DataFrame({
    'Horas de estudio':[11],
    'Asistencia':[88],
    'Participacion':[9],
})
print(f"Nota estimada: {modelo.predict(nuevo_estudiante)[0]:.2f}")
