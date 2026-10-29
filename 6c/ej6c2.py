"""
Enunciado:
Implementa un código capaz de leer archivos 'txt' para luego contar cuantas
veces se repite la palabra en el texto. Para ello se crean dos funciones.

La primera llamada 'read_txt_file(path)' que recibe como parámetro
'path' y retorna el texto del archivo que se encuentra en la ruta. El archivo
de texto se debe leer con decodificación "utf-8". Como sigue:
'open(path, "r", encoding="utf-8")'.

La segunda función llamada 'words_counter(text, word)' que recibe como
parametros 'text' y 'word' y retornará el número de palabras encontradas en
el texto.

Se debe leer el archivo que se encuentra en la ruta:
'files/ej6c2_data_engineer.txt'.

Función 'read_txt_file(path)'
    Parámetros:
        path (string): Representa la ruta al archivo.
    Retorna:
        str: Contenido del archivo tipo texto.

Función 'words_counter(text, word)'
    Parámetros:
        text (string): Representa el texto a procesar.
        word (string): Representa la palabra a buscar en el texto.
    Retorna:
        int: Número de ocurrencias de la palabra en el texto.

Ejemplo:
    Entrada:
        text = read_txt_file(path)
        print(words_counter(text, "data"))
    Salida:
        4

"""


def read_txt_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def words_counter(text: str, word: str) -> int:
    text = text.lower()
    word = word.lower()
    return text.count(word)
        


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
path = "6c/files/ej6c2_data_engineer.txt"
text = read_txt_file(path)
print(text[-25:])

word = "data"
count = words_counter(text, word)
print(f"The word '{word}' appears {count} times in the text.")
