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

print(val_int)
print(val_float)
print(val_str)
print(val_bool)
print(val_list)
print(val_dict)
print(val_set)

# 2) Haz una función que reciba una lista de números y retorne la suma y el promedio.

lista_num = [5, 9, 8, 3, 4, 57, 234, 12, 254, 48, 165]


def sumaypromedio(val):
    suma = sum(val)
    print(f"suma: {suma}")
    promedio = sum(val) / len(val)
    print(f"Promedio: {promedio}")


sumaypromedio(lista_num)

# 3) Escribe un bucle que imprima los números del 1 al 10.

for i in range(11):
    if i == 0:
        continue  # Omite el 1
    print(i)

# 4) Crea un diccionario de 3 amigos con su ciudad, y escribe una función que,
#    dado un nombre, retorne la ciudad.

lista_amigos = {"carlos": "maracay", "juan": "caracas", "pedro": "valencia"}
amigo = input("escribe el nombre de tu amigo: ").strip()


def retornar_ciudad(nombre):
    if amigo in lista_amigos:
        print(f"{nombre} vive en {lista_amigos[nombre]}")
    else:
        print(f"{nombre} no es tu amigo")


retornar_ciudad(amigo)


# 5) Escribe una función que reciba una cadena de texto y cuente cuántas
#    veces aparece cada palabra. Devuelve un diccionario tipo {"palabra": cantidad}.

cadena = "En programación, una cadena de texto, también conocida como cadena de caracteres o simplemente cadena, es una secuencia de caracteres (letras, números, símbolos, espacios, etc.) que se utiliza para representar texto. Las cadenas se suelen representar entre comillas (dobles o simples) para diferenciarlas de otros tipos de datos. "


def contar_palabras(cadena):
    # 1. Convertir a minúsculas y dividir la cadena en palabras
    palabras = cadena.lower().split()

    # 2. Crear un diccionario para almacenar los conteos
    frecuencia = {}

    # 3. Contar cada palabra
    for palabra in palabras:
        # Eliminar signos de puntuación alrededor de la palabra (opcional)
        palabra = palabra.strip(".,!?¡¿\"'()[]{}")

        if palabra:  # Solo contar si la palabra no está vacía después de limpiar
            frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

    return frecuencia


resultado = (contar_palabras(cadena))
print(resultado)
