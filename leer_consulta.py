from Codigo.libs import *


def leer_consulta(ruta_archivo):
    with open(ruta_archivo, 'r', encoding='utf-8') as file:
        query = file.read()
    return query