Esta es una pequeña recreación del juego del snake elaborado en el lenguaje de programación de python con la ayuda de la librería PyGame.

- Para la ejecución del código basta con descargarlo y colocarlo en alguna ruta que desees.
- Una vez hecho eso navegamos hasta la ruta y abrimos una terminal.
- Dentro de la terminal escribimos el siguiente comando:
- python3 snake_v2.py

En ese momento el programa comenzará a ejecutarse

Para lograr que la serpiente se mueva podemos valernos de las flechitas.


El juego va guardando las coordenadas de la cabeza, fruta y puntuación del juego, estos datos son guardados en un archivo
en formato json, así, cuando el juego se cierra por accidente es posible restaurar el estado actual del juego.

Ahora en esta actualización del código, se hace la implementación de hilos
- Se utiliza un hilo para manejar la lógica del juego y otro para estar dibujando la interfaz del usuario.

  Aquí un video de demostración del código en ejecución:
[Juego del snake](https://github.com/Dexne/Tolerante_a_fallas/blob/main/Snake_Game_threads/snake_v2.gif)
