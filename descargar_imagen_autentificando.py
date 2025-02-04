from Codigo.libs import *
from Funciones.base64_encode import base64_encode


# Función para descargar imágenes de FLEX y SERVIDOR para guardar en una carpeta
def descargar_imagen_autentificando(url1, url2, output_folder, username, password, file_name='imagen'):
    """
    Descarga una imagen desde la primera URL que esté disponible (url1 o url2) y la guarda en la carpeta especificada.
    """

    # Crear el encabezado de autenticación
    credentials = f"{username}:{password}"
    auth_header = f"Basic {base64_encode(credentials)}"
    headers = {
        "Authorization": auth_header,
        "User-Agent": "Python-requests/2.31",  # Ajusta si el servidor requiere un User-Agent específico
    }

    for url in [url1, url2]:
        try:
            # Intentar descargar la imagen desde la URL actual
            response = requests.get(url, headers=headers, stream=True)
            if response.status_code == 200:
                original_name = os.path.basename(url)
                punto = [i for i, char in enumerate(original_name) if char == "."]
                extension = original_name[max(punto):]
                image_path = os.path.join(output_folder, file_name + extension)
                with open(image_path, 'wb') as file:
                    for chunk in response.iter_content(chunk_size=8192):
                        file.write(chunk)
                print(f"Imagen guardada en: {image_path}")
                return image_path  # Salir después de guardar la imagen correctamente
            else:
                print(f"No se pudo descargar la imagen desde {url}. Código de estado: {response.status_code}")
        except Exception as e:
            print(f"Error al intentar descargar desde {url}: {e}")

    print("No se pudo descargar la imagen desde ninguna de las URLs.")
    return None