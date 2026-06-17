# PANDAS SIRVE PARA TRABAJAR CON DATOS EN FORMA DE TABLA
# Python permite cargar, limpiar, filtrar, ordenar y analizar tablas de datos.
import pandas as pd

# DATAFRAME
# Es el elemento más importate de Pandas.
# Un Dataframe es básicamente una tabla.

datos = {
    "Nombre": ["Ana", "Luis", "Marta"],
    "Edad": [25, 30, 28],
    "Ciudad": ["Madrid", "Valencia", "Sevilla"],
    "Sueldo": [1800, 2200, 2000],
}
df = pd.DataFrame(datos)
print(df)
# RESULTADO:   Nombre  Edad    Ciudad  Sueldo
# 0    Ana    25    Madrid    1800
# 1   Luis    30  Valencia    2200
# 2  Marta    28   Sevilla    2000

# La columna de la izquierda, 0, 1, 2, es el índice. Es como el número de fila.

"""Ver las primeras filas"""
# Cuando tienes muchos datos no quieres imprimir todo.
df.head()  # Por defecto muestra las 5 primeras filas.
df.head(10)  # Se modifica el número de dentro de los paréntesis para mostrar
# las filas que quieras.

# Información general de una tabla
df.info()  # Te dice cuantas filas hay, columnas, que tipo de datos y si hay valores vacíos.
df.describe()  # Te muestra cosas como media, mínimo, máximo, percentiles, etc.

"""Para seleccionar columnas"""
df["Nombre"]
# Resultado:
# 0      Ana
# 1     Luis
# 2    Marta
# Name: Nombre, dtype: object

"""Filtrar datos"""
# si queremos un sueldo mayor de 1900:
df[df["Sueldo"] > 1900]
# Resultado:
# Nombre  Edad    Ciudad  Sueldo
# 1   Luis    30  Valencia    2200
# 2  Marta    28   Sevilla    2000

"""Ordenar datos"""
df.sort_values("Sueldo")
# Se ordena en orden ascendente
# Resultado:
#   Nombre  Edad    Ciudad  Sueldo
# 0    Ana    25    Madrid    1800
# 2  Marta    28   Sevilla    2000
# 1   Luis    30  Valencia    2200

# Para ordenar de mayor a menor:
df.sort_values("Sueldo", ascending=False)

"""Crear nuevas columnas"""
# Se pueden crear una nueva columna a partir de otras.
# Ejemplo: calcular sueldo anual:
df["Sueldo anual"] = df["Sueldo"] * 12
print(df)
# Resultado:
#   Nombre  Edad    Ciudad  Sueldo  Sueldo anual
# 0    Ana    25    Madrid    1800         21600
# 1   Luis    30  Valencia    2200         26400
# 2  Marta    28   Sevilla    2000         24000

# Esto es muy típico en análisis de datos.
