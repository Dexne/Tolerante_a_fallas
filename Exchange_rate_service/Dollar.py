# Made of By Dexne
# 
# Codigo para estar consultando el valor del dollar
# Valores obtenidos de ExchangeRate-API
# 
# Para convertirlo en un servicio debemos de agregarlo como un nuev servicio
# para esto podemos ayudarnos de nado
# sudo nano /etc/systemd/system/exchange_rate.service
# Dentro del nano escribimos los siguiente:
# 
# [Unit]
# Description=USD to MXN Exchange Rate Service
# After=network.target
# 
# [Service]
# ExecStart=/usr/bin/python3 /home/dexne/Desktop/fault-tolerant/Daemon/Dollar.py >> /home/dexne/Desktop/fault-tolerant/Daemon/logfile.txt 2>&1
# WorkingDirectory=/home/dexne/Desktop/fault-tolerant/Daemon
# Restart=always
# 
# [Install]
# WantedBy=multi-user.target
#
# Recargamos para que se detecte el nuevo servicio:
# sudo systemctl daemon-reload
# 
# Habilitamos el servicio y lo activamos:
# sudo systemctl enable exchange_rate.service
# sudo systemctl start exchange_rate.service
# 
# verificamos el estado del servicio:
# sudo systemctl status exchange_rate.service
# 
# Listo.


# Modulos necesarios para hacer las peticiones
import requests
import json
import time
import os

# API key from ExchangeRate-API
api_key = "c16c8d8d7db820ba7efd8718"

# API endpoint for USD exchange rate
api_endpoint = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"

# Log file path
log_file = "/home/dexne/Desktop/fault-tolerant/Daemon/logfile.txt"

def fetch_exchange_rate():
    try:
        response = requests.get(api_endpoint)
        if response.status_code == 200:
            data = json.loads(response.text)
            exchange_rate = data["conversion_rates"]["MXN"]  # MXN exchange rate
            return exchange_rate
        else:
            print(f"Failed to fetch exchange rate data. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

def show_notification(message):
    os.system(f'notify-send "Dollar Exchange Rate" "{message}"')

def main():
    while True:
        exchange_rate = fetch_exchange_rate()
        if exchange_rate is not None:
            message = f"1 USD is worth {exchange_rate} Mexican Pesos (MXN)"
            show_notification(message)
            with open(log_file, "a") as f:
                f.write(f"{message}\n")
        time.sleep(3600)  # Check every hour

if __name__ == "__main__":
    main()
