# By: Dexne
# Servicio de consulta del clima en diferentes paises con ayuda de un API y Docker
# API usada de https://www.weatherapi.com/

# Importa la biblioteca Flask y las solicitudes (requests) como en la respuesta anterior
import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

# Ruta para obtener el clima en un país específico
@app.route('/clima', methods=['GET'])
def obtener_clima():
    pais = request.args.get('pais')
    if not pais:
        return "Por favor, proporciona un país como parámetro.", 400
    
    # Reemplaza API de WeatherAPI
    api_key = '768e7af08e804515816190005231810'
    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={pais}'

    response = requests.get(url)
    data = response.json()

    if 'current' in data:
        clima = data['current']['condition']['text']
        temperatura = data['current']['temp_c']
        return f"El clima en {pais} es {clima} y la temperatura actual es {temperatura}°C."
    else:
        return "No se pudo obtener información del clima para este país.", 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
