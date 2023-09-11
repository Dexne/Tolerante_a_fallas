# Made of by Dexne
#
# Recreacion de una version del clasico juego del snake
# programa realizado 100% en python con ayuda de la libreria de PyGame
# 
# Para la ejecicion del programa basta con copiarlo y pegarlo en alguna ruta
# del computador y ejecutarlo

import json
import os
import random
import pygame
import threading

pygame.init() # Inicializar Pygame

# Configuración de la pantalla
WIDTH, HEIGHT = 400, 420
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = (HEIGHT - 20) // GRID_SIZE

# Colores
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Crear la ventana
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

font = pygame.font.Font(None, 36) # Fuente para el marcador

# Inicializar variables del juego
snake = [(0, 0)]
snake_direction = (1, 0)
fruit = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
score = 0
running = True

# Función para guardar el estado del juego en un archivo JSON
def guardar_estado(juego):
    with open("estado_juego.json", "w") as archivo:
        json.dump(juego, archivo)

# Función para cargar el estado del juego desde un archivo JSON
def cargar_estado():
    try: # Uso de try except
        with open("estado_juego.json", "r") as archivo: # Manera de restaurar el estado
            juego = json.load(archivo)
        return juego
    except FileNotFoundError: # Caso de fracaso, archivo no encontrado
        return None

# Obtener la ubicación del script actual
script_dir = os.path.dirname(os.path.realpath(__file__))

# Cambiar la ubicación de trabajo actual al directorio del script
os.chdir(script_dir)

# Al iniciar el juego
estado_previo = cargar_estado()
if estado_previo:
    snake = estado_previo["snake"]
    snake_direction = estado_previo["snake_direction"]
    score = estado_previo["score"]
else:
    # Generar una nueva fruta si no hay un estado previo
    fruit = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

# Función para dibujar la serpiente en la pantalla
def draw_snake():
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

# Función para mostrar la puntuación
def draw_score():
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

# Función para actualizar el juego en un hilo separado
def actualizar_juego():
    global snake, snake_direction, fruit, score, running
    while running:
        # Lógica del juego aquí
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and snake_direction != (0, 1):
            snake_direction = (0, -1)
        elif keys[pygame.K_DOWN] and snake_direction != (0, -1):
            snake_direction = (0, 1)
        elif keys[pygame.K_LEFT] and snake_direction != (1, 0):
            snake_direction = (-1, 0)
        elif keys[pygame.K_RIGHT] and snake_direction != (-1, 0):
            snake_direction = (1, 0)

        new_head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])
        snake.insert(0, new_head)

        if snake[0] == fruit:
            score += 1
            fruit = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        else:
            snake.pop()

        if (
            snake[0][0] < 0
            or snake[0][0] >= GRID_WIDTH
            or snake[0][1] < 0
            or snake[0][1] >= GRID_HEIGHT
        ):
            running = False

        # Controlar la velocidad del juego
        pygame.time.delay(150)

# Crear un hilo para la lógica del juego
juego_thread = threading.Thread(target=actualizar_juego)
juego_thread.start()

# Función para dibujar la interfaz de usuario en un bucle separado
def dibujar_interfaz():
    while running:
        screen.fill(BLACK)
        draw_snake()
        pygame.draw.rect(screen, RED, (fruit[0] * GRID_SIZE, fruit[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
        draw_score()
        pygame.display.update()

# Crear un hilo para la interfaz de usuario
interfaz_thread = threading.Thread(target=dibujar_interfaz)
interfaz_thread.start()

# Bucle principal del juego
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Al cerrar el juego (antes de salir), guardar el estado del juego
guardar_estado({
    "snake": snake.copy(),  # Usar una copia para evitar problemas de referencia
    "snake_direction": snake_direction,
    "score": score
})

# Cerrar Pygame
pygame.quit()
