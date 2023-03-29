import matplotlib.pyplot as plt

va_means_1 = [
  0.9999798932951873,
  0.9449017057942487,
  0.7820070098509515,
  0.538331665555285,
  0.21613425515286033,
  0.06092494914459747
]
va_stds_1 = [
  0.0002983797792557562,
  0.007613776377758785,
  0.030135470666813616,
  0.05690834422656224,
  0.08308397575407427,
  0.03132194562181293
]

va_means_2 = [
  1.0000000000000016,
  0.9520751967007376,
  0.8151190632739866,
  0.6047947831433816,
  0.31691557598444453,
  0.12067987570462257
]
va_stds_2 = [
  2.220446049250313e-16,
  0.006486395417682998,
  0.024494211428824665,
  0.05509430073005713,
  0.0987183012414929,
  0.06083092105959983
]

# Crear un arreglo de posiciones para los datos en el eje X
eta_values = [0, 1, 2, 3, 4, 5]

# Crear el gráfico de puntos con los promedios y errores para el primer set de datos
plt.errorbar(eta_values, va_means_1, yerr=va_stds_1, fmt='o', capsize=5, color='blue', label='N=400, L=10')

# Crear el gráfico de puntos con los promedios y errores para el segundo set de datos
plt.errorbar(eta_values, va_means_2, yerr=va_stds_2, fmt='o', capsize=5, color='orange', label='N=100, L=5')

# Configurar el eje X
plt.xlabel('noise (η)', fontsize=20)

# Configurar el eje Y
plt.ylabel('vₐ', fontsize=20)

plt.legend()

plt.grid()

# Mostrar el gráfico
plt.show()
