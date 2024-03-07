# capa de transporte/comunicación con otras interfaces o sistemas externos.

import requests
from ...config import config

# comunicación con la REST API de la NASA.
def getAllImages(input=None):
    if input is None:
        json_response = requests.get(config.NASA_REST_API_DEFAULT_SEARCH).json()
    else:
        json_response = requests.get(config.NASA_REST_API + input).json()

    json_collection = []
    for object in json_response['collection']['items']:
        try:
            if 'links' in object:  # verificar si la clave 'links' está presente en el objeto (sin 'links' NO nos sirve, ya que no mostrará las imágenes).
                json_collection.append(object)
            else:
                print("[Capa de transporte --> transport.py]: se encontró un objeto sin clave 'links', omitiendo...")

        except KeyError: # puede ocurrir que no todos los objetos tenga la info. completa, en ese caso descartamos dicho objeto y seguimos con el siguiente en la próxima iteración.
            pass

    return json_collection