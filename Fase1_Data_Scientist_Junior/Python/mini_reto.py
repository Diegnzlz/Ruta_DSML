# Haz un programa en Python que lea un texto desde un archivo .txt,
# cuente las palabras más usadas, y las imprima en orden descendente.

def contar_palabras_en_archivo(ruta_archivo):
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()

    palabras = contenido.lower().split()
    frecuencia = {}

    for palabra in palabras:
        palabra = palabra.strip(".,!?¡¿\"'()[]{}")
        if palabra:
            frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    return frecuencia


resultado = contar_palabras_en_archivo(
    'Fase1_Data_Scientist_Junior/Python/archivo.txt')

palabras_ordenadas = sorted(
    resultado.items(), key=lambda item: item[1], reverse=True)
print(palabras_ordenadas)
