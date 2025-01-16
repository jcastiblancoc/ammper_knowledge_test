import requests
from requests.auth import HTTPBasicAuth
from core.config import API_KEY_ID, API_KEY_SECRET, BASE_URL_GET_INSTITUTIONS, BASE_URL_ACCOUNT_ID 

def get_bank_list():
    # Parámetros opcionales (por ejemplo, paginación)
    params = {
        "page_size": 10  # Número de resultados por página
    }

    # Cabeceras
    headers = {
        "accept": "application/json"
    }

    # Hacer la solicitud GET
    try:
        response = requests.get(
            BASE_URL_GET_INSTITUTIONS,
            headers=headers,
            params=params,
            auth=HTTPBasicAuth(API_KEY_ID, API_KEY_SECRET)  # Autenticación básica
        )

        # Manejo de la respuesta
        if response.status_code == 200:
            return response.json()  # Devolver datos en formato JSON
        else:
            return {"error": response.status_code, "message": response.text}

    except Exception as e:
        return {"error": "exception", "message": str(e)}
    
    
def get_transactions(account_id):

    try:
        response = requests.get(
            BASE_URL_ACCOUNT_ID + account_id,
            auth=HTTPBasicAuth(API_KEY_ID, API_KEY_SECRET),
            headers={"accept": "application/json"}
        )

        if response.status_code == 200:
            return response.json()
        else:
            return {"error": response.status_code, "message": response.text}
    except Exception as e:
        return {"error": "exception", "message": str(e)}