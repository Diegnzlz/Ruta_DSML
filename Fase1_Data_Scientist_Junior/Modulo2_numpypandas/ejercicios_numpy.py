# Numpy:
import numpy as np
# Crea un array de los números del 1 al 10 y calcula su suma y promedio.
arr = np.arange(1, 11)
print(arr)
print("Suma:", arr.sum())
print("Promedio:", arr.mean())


# Haz una matriz 3x3 con los números del 1 al 9, y saca la suma de cada fila.
m = np.arange(1, 10).reshape((3, 3))
print("Matriz:\n", m)
print("Suma por filas:", m.sum(axis=1))
