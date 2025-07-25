import numpy as np

# Crear un array desde una lista
arr = np.array([1, 2, 3, 4, 5])
print("Array:", arr)

# Operaciones básicas
print("Suma:", arr.sum())
print("Promedio:", arr.mean())
print("Máximo:", arr.max())
print("Array al cuadrado:", arr ** 2)

# Array bidimensional (matriz)
matriz = np.array([[1, 2, 3], [4, 5, 6]])
print("Matriz:\n", matriz)
print("Suma por filas:", matriz.sum(axis=1))
