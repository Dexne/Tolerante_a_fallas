# Ejemplo basico para conocer el funcionamiento

import prefect
from prefect import Flow, task


@task
def obtener_mensaje():
    mensaje = "Hola, mundo"
    return mensaje

@task
def imprimir_mensaje(mensaje):
    print(mensaje)

@Flow
def flujo_principal():
    mensaje = obtener_mensaje()
    imprimir_mensaje(mensaje)

if __name__ == '__main__':
    flujo_principal()
