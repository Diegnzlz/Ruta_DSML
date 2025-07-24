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
    total_palabras = sum(frecuencia.values())
    veces_python = frecuencia.get('python', 0)
    return frecuencia, total_palabras, veces_python


ruta = 'Fase1_Data_Scientist_Junior/Python/archivo.txt'
conteo, total, python_veces = contar_palabras_en_archivo(ruta)
print(f"Palabras distintas: {len(conteo)}")
print(f"Palabras totales: {total}")
print(f"Veces que aparece 'python': {python_veces}")
ordenar_palabras = sorted(
    conteo.items(), key=lambda item: item[1], reverse=True)
print(ordenar_palabras)
