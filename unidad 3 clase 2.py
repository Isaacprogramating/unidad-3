usuarios = {}

productos = {
    "1": {"nombre": "Leche", "precio": 2.50},
    "2": {"nombre": "Pan", "precio": 1.50},
    "3": {"nombre": "Huevos", "precio": 3.00},
    "4": {"nombre": "Arroz", "precio": 2.00},
    "5": {"nombre": "Manzanas", "precio": 1.00}
}

carrito = []

def encontrar_nombre_mas_largo():
    nombres = []
    for i in range(3):
        nombre = input(f"Ingrese el nombre {i+1}: ")
        nombres.append(nombre)
    
    nombre_mas_largo = max(nombres, key=len)
    
    print(f"El nombre con mayor cantidad de caracteres es: {nombre_mas_largo}")

def mostrar_nombres_apellidos():
    nombres = []
    apellidos = []
    
    for i in range(3):
        nombre = input(f"Ingrese el nombre {i+1}: ")
        apellido = input(f"Ingrese el apellido {i+1}: ")
        nombres.append(nombre)
        apellidos.append(apellido)
    
    for nombre, apellido in zip(nombres, apellidos):
        print(f"Nombre: {nombre} - Apellido: {apellido}")

def agregar_y_eliminar_nombres():
    nombres = []
    continuar = True
    
    while continuar:
        nombre = input("Ingrese un nombre: ")
        nombres.append(nombre)
        
        respuesta = input("¿Desea agregar otro nombre? (Sí/No): ").lower()
        if respuesta != "sí" and respuesta != "si":
            continuar = False
    
    nombre_mas_corto = min(nombres, key=len)
    nombres.remove(nombre_mas_corto)
    
    print(f"Lista de nombres final: {nombres}")

def registrar_usuario():
    nombre_usuario = input("Ingrese nombre de usuario: ")
    if nombre_usuario in usuarios:
        print("El usuario ya existe.")
    else:
        password = input("Ingrese contraseña: ")
        usuarios[nombre_usuario] = password
        print("Usuario registrado correctamente.")

def iniciar_sesion():
    nombre_usuario = input("Ingrese nombre de usuario: ")
    password = input("Ingrese contraseña: ")
    
    if nombre_usuario in usuarios and usuarios[nombre_usuario] == password:
        print("Inicio de sesión exitoso.")
    else:
        print("Nombre de usuario o contraseña incorrectos.")

def eliminar_usuario():
    nombre_usuario = input("Ingrese nombre de usuario a eliminar: ")
    if nombre_usuario in usuarios:
        password = input("Ingrese contraseña para confirmar la eliminación: ")
        if usuarios[nombre_usuario] == password:
            del usuarios[nombre_usuario]
            print(f"Usuario {nombre_usuario} eliminado correctamente.")
        else:
            print("Contraseña incorrecta, eliminación cancelada.")
    else:
        print("El usuario no existe.")

def agregar_producto():
    print("Productos disponibles:")
    for clave, producto in productos.items():
        print(f"{clave}: {producto['nombre']} - ${producto['precio']}")
    
    seleccion = input("Seleccione el número del producto que desea agregar al carrito: ")
    
    if seleccion in productos:
        carrito.append(productos[seleccion])
        print(f"Producto '{productos[seleccion]['nombre']}' agregado al carrito.")
    else:
        print("Producto no válido. Intente nuevamente.")

def ver_canasta():
    if carrito:
        print("Productos en el carrito:")
        for producto in carrito:
            print(f"{producto['nombre']} - ${producto['precio']}")
    else:
        print("El carrito está vacío.")

def ver_total():
    total = sum(producto['precio'] for producto in carrito)
    print(f"Total a pagar: ${total}")

def menu_principal():
    while True:
        print("\nMenú Principal:")
        print("1. Encontrar nombre más largo")
        print("2. Mostrar nombres y apellidos")
        print("3. Agregar y eliminar nombres")
        print("4. Gestión de usuarios")
        print("5. Sistema de ventas de supermercado")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            encontrar_nombre_mas_largo()
        elif opcion == "2":
            mostrar_nombres_apellidos()
        elif opcion == "3":
            agregar_y_eliminar_nombres()
        elif opcion == "4":
            menu_usuarios()
        elif opcion == "5":
            menu_supermercado()
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

def menu_usuarios():
    while True:
        print("\nMenú de usuarios:")
        print("1. Iniciar sesión")
        print("2. Registrar usuario")
        print("3. Eliminar usuario")
        print("4. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            iniciar_sesion()
        elif opcion == "2":
            registrar_usuario()
        elif opcion == "3":
            eliminar_usuario()
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intente nuevamente.")

def menu_supermercado():
    while True:
        print("\nMenú de supermercado:")
        print("1. Agregar productos")
        print("2. Ver canasta")
        print("3. Ver total")
        print("4. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            ver_canasta()
        elif opcion == "3":
            ver_total()
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecutar el programa principal
menu_principal()
