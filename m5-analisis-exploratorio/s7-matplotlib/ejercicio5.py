# 5. Gráfico de pastel (pie chart) 
# Representa visualmente la distribución porcentual de 
# usuarios por navegador: 
# navegadores = ['Chrome', 'Firefox', 'Edge', 'Safari'] 
# usuarios=[150, 200, 100] 

import matplotlib.pyplot as plt

navegadores = ['Chrome', 'Firefox', 'Edge']
usuarios = [150, 200, 100]

plt.pie(usuarios, labels=navegadores, autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff','#99ff99'])
plt.title('Distribución porcentual de usuarios por navegador')
plt.axis('equal')
plt.show()