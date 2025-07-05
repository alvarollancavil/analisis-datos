import pandas as pd
from sklearn.linear_model  import LinearRegression

# Datos
df=pd.read_csv("casas.csv")

# Modelo
x=df[['metros_cuadrados','habitaciones','edad']]
y=df['precio']

modelo=LinearRegression()
modelo.fit(x,y)

print(f"Coeficientes: {modelo.coef_}")
print(f"Interseccion: {modelo.intercept_}")

# Prediccion
nueva_casa=pd.DataFrame({
    'metros_cuadrados':[100],
    'habitaciones':[4],
    'edad':[11],
})
print(f"Precio estimado: {modelo.predict(nueva_casa)}")