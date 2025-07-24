# Variables y tipos
nombre = "Diego"
edad = 33
es_estudiante = True
notas = [16, 19, 15]

# Imprimir info
print(f"Hola {nombre}, edad: {edad}, estudiante: {es_estudiante}")

# Promedio de notas
promedio = sum(notas) / len(notas)
print(f"Promedio: {promedio}")

# Diccionario
persona = {"nombre": nombre, "edad": edad, "notas": notas}
print("Diccionario persona:", persona)

# Bucle for
for nota in notas:
    print("Nota:", nota)

# Función simple


def saludar(nombre):
    return f"Hola, {nombre}!"


print(saludar("Diego"))
