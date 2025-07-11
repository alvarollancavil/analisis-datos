# 9. Personalización avanzada y estilo 
# Usa diferentes estilos (plt.style.use("ggplot"), "seaborn", 
# etc.) para visualizar el mismo gráfico y comparar. 

import matplotlib.pyplot as plt

peso = [60, 72, 75, 80, 90, 100, 110]
altura = [1.60, 1.70, 1.75, 1.80, 1.85, 1.90, 2.00]

estilos = ['ggplot', 'seaborn-v0_8-darkgrid', 'classic']

for estilo in estilos:
    plt.style.use(estilo)
    plt.figure(figsize=(6, 4))
    plt.scatter(peso, altura, color='darkorange', marker='o')
    plt.title(f'Relación Peso vs. Altura - Estilo: {estilo}')
    plt.xlabel('Peso (kg)')
    plt.ylabel('Altura (m)')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()