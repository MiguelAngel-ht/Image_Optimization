from Codigo.libs import *



# Traducir para clave de buscador en navegador
def base64_encode(credentials):
    """
    Codifica las credenciales en Base64 para autenticación básica, imitando la lógica de VBA.
    """
    encoded_bytes = base64.b64encode(credentials.encode('utf-8'))
    return encoded_bytes.decode('utf-8')
    