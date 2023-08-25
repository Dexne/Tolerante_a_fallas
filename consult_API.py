import requests


def fetch_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Genera una excepción si hay un error en la respuesta
        data = response.json()
        return data
    except requests.RequestException as e:
        print("Error al hacer la solicitud:", e)
        return None

api_url = "https://api.example.com/data"
data = fetch_data(api_url)
if data:
    print("Datos de la API:", data)
