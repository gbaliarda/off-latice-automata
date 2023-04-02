import matplotlib.pyplot as plt

va_means = [
  0.24706974783723484,
  0.39334908931554724,
  0.532420951016502,
  0.6522996175543535,
  0.69037800060667
]
va_stds = [
  0.11179151710204369,
  0.12383195361406994,
  0.09532073907399839,
  0.035305445994624644,
  0.018493727120027524
]

# Crear un arreglo de posiciones para los datos en el eje X
rho_values = [1, 2, 3, 5, 7]

# Crear el gráfico de puntos con los promedios y errores
plt.errorbar(rho_values, va_means, yerr=va_stds, fmt='o', capsize=5)

# Configurar el eje X
plt.xlabel('densidad', fontsize=20)
plt.subplots_adjust(bottom=0.15, left=0.12)

# Configurar el eje Y
plt.ylabel('vₐ', fontsize=20)

plt.grid()

# Mostrar el gráfico
plt.show()
