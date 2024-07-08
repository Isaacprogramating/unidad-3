# Funciones para el Sistema de Gestión de Torneos de Videojuegos

def registrar_inscripcion(inscripciones):
    print("\nRegistro de Inscripción")
    nombre = input("Nombre del jugador: ")
    apellido = input("Apellido del jugador: ")
    ciudad = input("Ciudad de origen: ")
    juego = input("Videojuego (Fortnite, League of Legends, Valorant): ")

    # Validar que el juego ingresado sea uno de los permitidos
    juegos_permitidos = ["Fortnite", "League of Legends", "Valorant"]
    if juego not in juegos_permitidos:
        print("Error: Videojuego no válido.")
        return

    # Crear diccionario con la inscripción
    inscripcion = {
        "nombre": nombre,
        "apellido": apellido,
        "ciudad": ciudad,
        "juego": juego
    }

    # Agregar la inscripción a la lista de inscripciones
    inscripciones.append(inscripcion)
    print("Inscripción registrada exitosamente.")


def listar_inscripciones(inscripciones):
    print("\nListado de Inscripciones")
    for index, inscripcion in enumerate(inscripciones, start=1):
        print(f"{index}. {inscripcion['nombre']} {inscripcion['apellido']} - {inscripcion['juego']}")
    if not inscripciones:
        print("No hay inscripciones registradas.")


def imprimir_detalle_por_juego(inscripciones):
    print("\nImpresión de Detalle por Videojuego")
    juego_seleccionado = input("Ingrese el videojuego (Fortnite, League of Legends, Valorant): ")

    # Validar que el juego ingresado sea uno de los permitidos
    juegos_permitidos = ["Fortnite", "League of Legends", "Valorant"]
    if juego_seleccionado not in juegos_permitidos:
        print("Error: Videojuego no válido.")
        return

    # Filtrar las inscripciones por el juego seleccionado
    inscripciones_por_juego = [inscripcion for inscripcion in inscripciones if inscripcion['juego'] == juego_seleccionado]

    # Si no hay inscripciones para el juego seleccionado
    if not inscripciones_por_juego:
        print(f"No hay inscripciones registradas para {juego_seleccionado}.")
        return

    # Nombre del archivo a generar
    nombre_archivo = f"inscripciones_{juego_seleccionado.lower()}.txt"

    # Escribir las inscripciones en el archivo
    with open(nombre_archivo, 'w') as file:
        file.write(f"Detalle de Inscripciones para {juego_seleccionado}\n")
        for index, inscripcion in enumerate(inscripciones_por_juego, start=1):
            file.write(f"{index}. {inscripcion['nombre']} {inscripcion['apellido']} - {inscripcion['ciudad']}\n")

    print(f"Archivo '{nombre_archivo}' generado exitosamente con el detalle de inscripciones.")


def salir():
    print("Saliendo del programa. ¡Hasta luego!")


def main():
    inscripciones = []
    while True:
        print("\nBienvenido al Sistema de Gestión de Torneos de Videojuegos")
        print("1. Registrar Inscripción")
        print("2. Listar Todas las Inscripciones")
        print("3. Imprimir Detalle de Inscripciones por Videojuego")
        print("4. Salir del Programa")

        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            registrar_inscripcion(inscripciones)
        elif opcion == "2":
            listar_inscripciones(inscripciones)
        elif opcion == "3":
            imprimir_detalle_por_juego(inscripciones)
        elif opcion == "4":
            salir()
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")

if __name__ == "__main__":
    main()
