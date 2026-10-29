"""
Enunciado:
Implementa dos funciones: 'count_letters(names)' y 'create_log(names)'.
En primer lugar, utilizando la librería logging, implementa una función 
'count_letters(names)' que recibe como parámetro 'names' que es una lista de 
strings con nombres. La función debe contar cuántas veces aparece cada letra 
en todos los nombres de la lista. La función debe devolver un diccionario con 
la frecuencia de cada letra.

En segundo lugar, la función 'create_log(names)' recibe también una lista
de strings con nombres, llama a la función 'count_letters(names)' y almacena
el diccionario generado en el archivo 'production.log' en formato de 
registro de nivel DEBUG.

Una vez se tenga el diccionario de la función 'count_letters(names)', debes
guardarlo con el siguiente código:
logging.info(f'Letter counts: {letter_counts}')

Parámetro:
    names: lista de strings.

Ejemplo:
    Entrada:
        ["Juan", "Pedro", "Marta"]
    Salida:
        Existe un fichero "production.log" que contiene:
        DEBUG:root:Letter counts: {'J': 1, 'u': 1, 'a': 3, 'n': 1, 'P': 1, 'e': 1, 'd': 1, 'r': 2, 'o': 1, 'M': 1, 't': 1}

Nota: Verificar que el archivo de logs se haya creado.

"""
import logging

def count_letters(names):
    letter_count = {}
    for name in names:
        for letter in name:
            if letter not in letter_count:
                letter_count[letter] = 1
            else:
                letter_count[letter] += 1
    return letter_count


logging.basicConfig(
        level=logging.INFO,
        filename='production.log'
    )


def create_log(names):
    letter_counts = count_letters(names)
    logging.info(f'Letter counts: {letter_counts}')


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
create_log(["Juan", "Pedro", "Marta"])
