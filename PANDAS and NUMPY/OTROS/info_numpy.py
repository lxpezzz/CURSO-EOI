import numpy as np

datos = np.array([10, 20, 30, 40, 50])
print(datos.mean())  # media = 30.0
print(datos.sum())  # suma = 150
print(datos.max())  # máximo = 50
print(datos.min())  # mínimo = 10
print(datos.std())  # desviación típica = 14.14

# EJEMPLO:
ingresos = np.array([1200, 1500, 1800, 1300, 2000])
media = ingresos.mean()
print(media)  # = 1560.0

"""ARRAYS DE 2 DIMENSIONES"""
import numpy as np

matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# PARA VER LA FORMA :
print(matriz.shape) # (3, 3)

# PARA ACCEDER A VALORES CONCRETOS:
print(matriz[0][0]) # 1
