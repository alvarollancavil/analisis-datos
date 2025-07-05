import pandas as pd
from sklearn.linear_model  import LinearRegression

# Datos
df=pd.read_csv("publicidad.csv")

# Modelo
x=df[['tv','radio','internet']]
y=df['ventas']

modelo=LinearRegression()
modelo.fit(x,y)

print(f"Coeficientes: {modelo.coef_}")
print(f"Interseccion: {modelo.intercept_}")

# Prediccion
nueva_camp=pd.DataFrame({
    'tv':[50.5],
    'radio':[20.5],
    'internet':[90],
})
print(f"Ventas estimadas: {modelo.predict(nueva_camp)}")