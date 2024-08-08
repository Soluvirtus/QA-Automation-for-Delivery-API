import copy

user_data = {
    "firstName": "Max",
    "phone": "+10005553535",
    "address": "8042 Lancaster Ave.Hamburg, NY"
}

kit_data = {
    "name": "Mi conjunto"
}

def get_kit_body(name):
    """
    Función para obtener el cuerpo de la solicitud del kit con un nombre específico.
    Parámetros:
    - name: Nombre del kit.
    """
    kit_body = copy.deepcopy(kit_data)
    kit_body["name"] = name
    return kit_body
