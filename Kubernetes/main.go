// By: Dexne

// Declaramos el paquete principal donde se encuentra la función main.
package main

// Importamos los paquetes necesarios.
import (
	"fmt"      // Este paquete proporciona funciones para el formato de entrada/salida.
	"net/http" // Este paquete proporciona funciones HTTP.
)

// Declaramos la función homePage que se activará cuando se acceda a la ruta "/".
// Toma dos argumentos: un ResponseWriter para enviar la respuesta HTTP, y un Request que representa la solicitud HTTP.
func homePage(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "My Awesome Go App")
}

// Declaramos la función setupRoutes que configura la ruta que activará la función homePage.
func setupRoutes() {
	// HandleFunc registra la función homePage para ser llamada cuando se acceda a la ruta "/".
	http.HandleFunc("/", homePage)
}

// Declaramos la función main que será la primera en ejecutarse cuando se inicie el programa.
func main() {
	fmt.Println("Go Web App Started on port 3000")
	// Llamamos a la función setupRoutes para configurar nuestras rutas.
	setupRoutes()
	// ListenAndServe comienza a escuchar las solicitudes HTTP en el puerto 3000.
	http.ListenAndServe(":3000", nil)
}
