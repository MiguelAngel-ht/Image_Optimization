from Codigo.libs import *


# Limpiar una carpeta
def resetear_folder(folder_path):
    """
    Limpia y reinicia la carpeta especificada.
    """
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)  # Elimina la carpeta y su contenido
    os.makedirs(folder_path)  # Crea una carpeta vacía

    