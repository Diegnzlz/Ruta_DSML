# 1. Función de números pares
# Crea una función que reciba una lista de números y devuelva una nueva

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


def num_pares(lista_par):
    return [n for n in lista_par if n % 2 == 0]


pares = num_pares(lista)
print(pares)

# 2. Filtrar mayores de edad en diccionario
# Dado un diccionario de personas y su edad, escribe una función que retorne una lista
# con los nombres de las personas que tienen más de 18 años.

lista_personas = {"Ana": 21, "Beto": 17,
                  "Clara": 34, "juana": 15, "marcelo": 25}


def mayores_de_edad(personas, edad_minima=18):
    return [nombre for nombre, edad in personas.items() if edad > edad_minima]


print(mayores_de_edad(lista_personas))
