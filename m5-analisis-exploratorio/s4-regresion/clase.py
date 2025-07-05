import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model  import LinearRegression

x=np.array([1,2,3,4,5]).reshape(-1,1)
y=np.array([2,4,5,4,5])

modelo=LinearRegression()
modelo.fit(x,y)

print(f"Pendiente: {modelo.coef_[0]:.2f}")
print(f"Interseccion: {modelo.intercept_:.2f}")

y_predict=modelo.predict(x)

plt.scatter(x,y,color='blue',label='Datos reales')
plt.plot(x,y_predict,color='red',label='Linea de regresion')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()