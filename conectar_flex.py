from Codigo.libs import *

def conectar_flex():
    # Leer archivo
    ruta_actual = os.path.dirname(os.path.abspath(__file__))
    with open(ruta_actual + '\\credencialesFlex.txt', 'r', encoding='utf-8') as archivo:
        lineas = [linea.replace('\n', ' ').replace('\t', ' ').replace(' ', '') for linea in archivo]

    # Parámetros
    user = lineas[0]
    password = lineas[1]

    return user, password