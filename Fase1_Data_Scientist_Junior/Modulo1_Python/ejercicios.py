from collections import Counter
# Ejercicios para ti (obligatorio, pega tus respuestas aquí):
# 1) Crea una variable de cada tipo: int, float, str, bool, list, dict, set y
#    muestra cada una con print().

val_int = 69
val_float = 6.65
val_str = "Hola"
val_bool = True
val_list = [1, 2, 3, 4, 5]
val_dict = {"nombre": "job", "animal": "·perro", "raza": "mierdero", "edad": 5}
val_set = {1, 2, 3, 4, 5}

print(type(val_int))
print(val_int)
print(type(val_float))
print(val_float)
print(type(val_str))
print(val_str)
print(type(val_bool))
print(val_bool)
print(type(val_list))
print(val_list)
print(type(val_dict))
print(val_dict)
print(type(val_set))
print(val_set)
# 2) Haz una función que reciba una lista de números y retorne la suma y el promedio.

lista_num = [5, 9, 8, 3, 4, 57, 234, 12, 254, 48, 165]


def sumaypromedio(val):
    if len(val) == 0:
        return 0, 0
    suma = sum(val)
    promedio = suma / len(val)
    return suma, promedio


suma, promedio = sumaypromedio(lista_num)
print(f"Suma: {suma}, Promedio: {promedio}")

# 3) Escribe un bucle que imprima los números del 1 al 10.

for i in range(1, 11):
    print(i)

# 4) Crea un diccionario de 3 amigos con su ciudad, y escribe una función que,
#    dado un nombre, retorne la ciudad.

lista_amigos = {"carlos": "maracay", "juan": "caracas", "pedro": "valencia"}


def retornar_ciudad(nombre):
    if nombre in lista_amigos:
        print(f"{nombre} vive en {lista_amigos[nombre]}")
    else:
        print(f"{nombre} no es tu amigo")


amigo = input("escribe el nombre de tu amigo: ").strip()
retornar_ciudad(amigo)


# 5) Escribe una función que reciba una cadena de texto y cuente cuántas
#    veces aparece cada palabra. Devuelve un diccionario tipo {"palabra": cantidad}.

cadena = "En programación, una cadena de texto, también conocida como cadena de caracteres o simplemente cadena, es una secuencia de caracteres (letras, números, símbolos, espacios, etc.) que se utiliza para representar texto. Las cadenas se suelen representar entre comillas (dobles o simples) para diferenciarlas de otros tipos de datos. "


def contar_palabras(cadena):
    palabras = cadena.lower().split()
    palabras = [p.strip(".,!?¡¿\"'()[]{}") for p in palabras if p]
    return Counter(palabras)


print(contar_palabras(cadena).most_common(10))  # Muestra las 10 más frecuentes
