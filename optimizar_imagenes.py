from Codigo.libs import *


def optimizar_imagenes(folder_path, max_width = 132, max_height = 102, max_size_kb = 5):
    """
    Recorre las imágenes en una carpeta y reduce la calidad de las imágenes de alta calidad manteniendo la proporción.

    :param folder_path: Ruta de la carpeta que contiene las imágenes.
    :param max_width: Ancho máximo permitido para las imágenes redimensionadas.
    :param max_height: Altura máxima permitida para las imágenes redimensionadas.
    :param max_size_kb: Tamaño máximo en KB permitido para las imágenes redimensionadas.
    """
    for file_name in os.listdir(folder_path):

        # OBTENER ARCHIVO NOMBRE
        file_path = os.path.join(folder_path, file_name)

        try:
            with Image.open(file_path) as img:

                # CREAR COPIA TEMPORAL AUXILIAR
                temp_path = os.path.join(folder_path, f"temp_{file_name}")
                img = img.convert('RGB')
                img.save(temp_path)

                # OBTENIENDO TAMAÑO Y DIMENSIÓN
                width, height = img.size
                file_size_kb = os.path.getsize(file_path) / 1024

                # CRITERIO DE CALIDAD ALTA
                if  file_size_kb > max_size_kb:
                    print(f"Procesando {file_name}: {width}x{height}, {file_size_kb:.2f} KB")

                    # Redimensionar manteniendo la proporción
                    img.thumbnail((max_width, max_height))

                    # GUARDAR COPIA REDIMENCIONADA según el formato original
                    img_format = img.format if img.format in ["JPEG", "PNG", "GIF", "BMP"] else "JPEG"
                    img.save(temp_path, format=img_format, quality=85 if img_format == "JPEG" else None, optimize=True)

                    # REMPLAZAR CON EL TEMPORAL PARA TENER EL MISMO NOMBRE 
                    os.replace(temp_path, file_path)

                    # VERIFICAR TAMAÑO
                    # optimized_size_kb = os.path.getsize(file_path) / 1024
                    # print(f"Imagen optimizada guardada en {file_path}: {optimized_size_kb:.2f} KB")

                    print(f"Imagen {file_name} optimizada")
                else:
                    print(f"{file_name} ya es de baja calidad: {width}x{height}, {file_size_kb:.2f} KB")
                    os.remove(temp_path)  # Eliminar el archivo temporal si no se necesita

        except Image.UnidentifiedImageError:
            print(f"No se pudo procesar {file_name}: El archivo no es una imagen o está corrupto.")
        except Exception as e:
            print(f"No se pudo procesar {file_name}: {e}")
