# 4. Gráfico de barras 
# Usa los siguientes datos para crear un gráfico de 
# barras que muestre las ventas semanales: 
# productos = ['A', 'B', 'C', 'D'] 
# ventas = [120, 300, 150, 90] 

import matplotlib.pyplot as plt

productos = ['A', 'B', 'C', 'D'] 
ventas = [120, 300, 150, 90] 

plt.bar(productos, ventas, color='skyblue')
plt.title('Ventas Semanales por Producto')
plt.xlabel('Producto')
plt.ylabel('Ventas')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

