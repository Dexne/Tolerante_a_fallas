# Valor del dollar

Made of By Dexne

Codigo para estar consultando el valor del dollar
Valores obtenidos de ExchangeRate-API

Para convertirlo en un servicio debemos de agregarlo como un nuev servicio
para esto podemos ayudarnos de nado

[Agregado como servicio](https://github.com/Dexne/Tolerante_a_fallas/blob/main/Exchange_rate_service/assets/AgregarComoServicio.jpeg)

sudo nano /etc/systemd/system/exchange_rate.service

Dentro del nano escribimos los siguiente:

[Unit]
Description=USD to MXN Exchange Rate Service
After=network.target

[Service]
ExecStart=/usr/bin/python3 /home/dexne/Desktop/fault-tolerant/Daemon/Dollar.py >> /home/dexne/Desktop/fault-tolerant/Daemon/logfile.txt 2>&1
WorkingDirectory=/home/dexne/Desktop/fault-tolerant/Daemon
Restart=always

[Install]
WantedBy=multi-user.target

[Verificacion de la escritura](https://github.com/Dexne/Tolerante_a_fallas/blob/main/Exchange_rate_service/assets/VerificacionDeAgregado.jpeg)

Recargamos para que se detecte el nuevo servicio:

sudo systemctl daemon-reload

Habilitamos el servicio y lo activamos:

sudo systemctl enable exchange_rate.service

sudo systemctl start exchange_rate.service

verificamos el estado del servicio:

sudo systemctl status exchange_rate.service

[Estatus](https://github.com/Dexne/Tolerante_a_fallas/blob/main/Exchange_rate_service/assets/DamosDeAlta.jpeg)


[Resultado](https://github.com/Dexne/Tolerante_a_fallas/blob/main/Exchange_rate_service/assets/Resultados.jpeg)

Listo.
