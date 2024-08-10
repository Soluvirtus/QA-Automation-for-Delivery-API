import pytest
from sender_stand_request import create_user, post_new_client_kit
from configuration import URL_SERVICE, CREATE_USER_PATH, KITS_PATH
from data import get_kit_body

def get_new_user_token():
    """
    Función para obtener un nuevo token de usuario.
    """
    url = f"{URL_SERVICE}{CREATE_USER_PATH}"
    user_data = {
        "firstName": "Max",
        "phone": "+10005553535",
        "address": "8042 Lancaster Ave.Hamburg, NY"
    }
    response = create_user(url, user_data)
    #print(f"New user token: {response['authToken']}")
    return response["authToken"]

@pytest.fixture
def auth_token():
    return get_new_user_token()

def positive_assert(kit_body, auth_token):
    """
    Función para realizar una aserción positiva.
    """
    kit_url = f"{URL_SERVICE}{KITS_PATH}"
    response = post_new_client_kit(kit_url, kit_body, auth_token=auth_token)
    #print(f"Positive assert response: {response}")
    assert response["name"] == kit_body["name"]

def negative_assert_code_400(kit_body, auth_token):
    """
    Función para realizar una aserción negativa (código 400).
    """
    kit_url = f"{URL_SERVICE}{KITS_PATH}"
    response = post_new_client_kit(kit_url, kit_body, auth_token=auth_token)
    assert response.get("code") == 400, f"Expected code 400, but got {response.get('code', response)}"

def test_create_kit_with_min_length_name(auth_token):
    """
    Prueba para crear un kit con el nombre de longitud mínima permitida.
    """
    kit_body = get_kit_body("a")
    positive_assert(kit_body, auth_token)

def test_create_kit_with_max_length_name(auth_token):
    """
    Prueba para crear un kit con el nombre de longitud máxima permitida.
    """
    kit_body = get_kit_body("Abcd" * 127 + "abC")
    positive_assert(kit_body, auth_token)

def test_create_kit_with_empty_name(auth_token):
    """
    Prueba para crear un kit con un nombre vacío.
    """
    kit_body = get_kit_body("")
    negative_assert_code_400(kit_body, auth_token)

def test_create_kit_with_name_too_long(auth_token):
    """
    Prueba para crear un kit con un nombre que excede la longitud máxima permitida.
    """
    kit_body = get_kit_body("Abcd" * 127 + "abcD")
    negative_assert_code_400(kit_body, auth_token)

def test_create_kit_with_special_characters(auth_token):
    """
    Prueba para crear un kit con caracteres especiales en el nombre.
    """
    kit_body = get_kit_body("№%@")
    positive_assert(kit_body, auth_token)

def test_create_kit_with_spaces_in_name(auth_token):
    """
    Prueba para crear un kit con espacios en el nombre.
    """
    kit_body = get_kit_body(" A Aaa ")
    positive_assert(kit_body, auth_token)

def test_create_kit_with_numbers_in_name(auth_token):
    """
    Prueba para crear un kit con números en el nombre.
    """
    kit_body = get_kit_body("123")
    positive_assert(kit_body, auth_token)

def test_create_kit_without_name(auth_token):
    """
    Prueba para crear un kit sin el parámetro 'name'.
    """
    kit_body = get_kit_body("")
    negative_assert_code_400(kit_body, auth_token)

def test_create_kit_with_invalid_name_type(auth_token):
    """
    Prueba para crear un kit con un nombre de tipo incorrecto (número en lugar de cadena).
    """
    kit_body = get_kit_body(123)
    negative_assert_code_400(kit_body, auth_token)
