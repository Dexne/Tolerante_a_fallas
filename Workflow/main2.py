##################################################################
#
# By: Dexne
# 
# Workflows y Prefect
# 
# En este pequeño script se han implementados funciones que
# trasnformaremos en tareas con ayuda de los decoradores 
# para transformarlos en tareas y con ayuda de un flujo indicamos
# el orden en que se ejecutaran
#
###################################################################

import os

import cv2

import prefect
from prefect import Flow, task


@task
def convertir_a_escala_de_gris(imagen):
    return cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

@task
def obtener_imagenes(carpeta):
    imagenes = []
    for archivo in os.listdir(carpeta):
        if archivo.endswith(".jpg") or archivo.endswith(".png"):
            imagen = cv2.imread(os.path.join(carpeta, archivo))
            imagenes.append(imagen)
    return imagenes


@task
def procesar_imagenes(carpeta):
    imagenes = obtener_imagenes(carpeta)
    for imagen in imagenes:
        imagen_gris = convertir_a_escala_de_gris(imagen)
        cv2.imshow("Imagen en escala de grises", imagen_gris)
        cv2.waitKey(0)

@Flow
def flujo_principal():
    imagenes = obtener_imagenes(carpeta)
    for imagen in imagenes:
        imagen_gris = convertir_a_escala_de_gris(imagen)
        cv2.imshow("Imagen en escala de grises", imagen_gris)
        cv2.waitKey(0)


if __name__ == "__main__":
    carpeta = "src"
    flujo_principal()
