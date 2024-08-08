
import requests

def create_user(url, user_data):
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=user_data, headers=headers)
    print(f"Request to {url} with data {user_data} returned {response.status_code}")
    return response.json()

def post_new_client_kit(url, kit_body, auth_token=None, card_id=None):
    """
    Función para crear un nuevo kit de producto.
    Parámetros:
    - url: URL del servicio.
    - kit_body: Cuerpo de la solicitud.
    - auth_token: Token de autenticación.
    - card_id: ID de la tarjeta (opcional).
    """
    headers = {
        "Content-Type": "application/json"
    }
    if auth_token:
        headers["Authorization"] = f"Bearer {auth_token}"
    if card_id:
        kit_body["cardId"] = card_id

    response = requests.post(url, json=kit_body, headers=headers)
    print(f"Request to {url} with data {kit_body} and headers {headers} returned {response.status_code}")
    return response.json()
