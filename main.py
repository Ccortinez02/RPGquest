from jugadores import Jugador
from mundo import Mundo
from personaje import Personaje

def crear_personaje():
    # Crea un nuevo objeto Jugador
    nombre = input("Ingrese su nombre: ")
    personaje = Jugador(nombre)
    return personaje

def iniciar_juego():
    # Crea un mundo y un jugador
    personaje = crear_personaje()
    mundo = Mundo()

    # Bucle principal del juego
while True:
    # Muestra las opciones al jugador
    print("¿Qué quieres hacer?")
    print("1. Explorar el mundo")
    print("2. Revisar inventario")
    print("3. Equipar equipo")
    print("4. Usar habilidad")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    # Ejecuta la acción correspondiente
    if opcion == "1":
        Mundo.explorar(Personaje)
    elif opcion == "2":
        Personaje.mostrar_inventario()
    elif opcion == "3":
        Personaje.equipar_equipo()
    elif opcion == "4":
        Personaje.usar_habilidad()
    elif opcion == "5":
        break
    else:
        print("Opción inválida.")

if __name__ == "__main__":
    iniciar_juego()
