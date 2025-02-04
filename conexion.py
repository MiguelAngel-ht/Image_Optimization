from Codigo.libs import *

def crear_conexion():

    # Leer archivo
    ruta_actual = os.path.dirname(os.path.abspath(__file__))
    with open(ruta_actual + '\\credenciales.txt', 'r', encoding='utf-8') as archivo:
        lineas = [linea.replace('\n', ' ').replace('\t', ' ').replace(' ', '') for linea in archivo]

    # Parámetros
    server = lineas[0]
    database = lineas[1]
    username = lineas[2]
    password = lineas[3]

    # Conexión
    engine = create_engine(f'mssql+pymssql://{username}:{password}@{server}/{database}')

    return engine
