from Codigo.libs import *
from Funciones import *
from Credenciales.conexion import crear_conexion
from Credenciales.conectar_flex import conectar_flex


# Conexión
engine = crear_conexion()

# Obtener Query
query = leer_consulta(os.getcwd() + '\\Consultas\\query.sql')

# Ejecutar Query
df = pd.read_sql_query(text(query), engine)

# Configuración
output_folder = 'C:\\Users\\miguel.hernandez\\Documents\\Python [Notebooks]\\11 - SAS Automatizaciones\\COMPLETAR IMÁGENES ALTERNATIVAS SAS\\AccuracyImagenes\\Imagenes'
username, password = conectar_flex()

# Reiniciar carpeta
resetear_folder(output_folder)
print('Carpeta Reseteada')

# Descargar Imágenes
for code, url_imagen in zip(df['prdCode'], df['flxImagen_Alternativa']):

    # Descargar imágenes
    descargar_imagen_autentificando('http://10.16.32.22/fotos/'+ code +'pm.jpg',        # PRIMERO INTENTA CON
                                    'http://flexplm.grupoandrea.com/' + url_imagen,     # LUEGO INTENTA CON
                                    output_folder, 
                                    username, 
                                    password, 
                                    code)
print('Imágenes Descargadas')
    
# Optimizar Imágenes
optimizar_imagenes(output_folder, max_size_kb=5)
print('Imágenes Optimizadas')
print('FIN')