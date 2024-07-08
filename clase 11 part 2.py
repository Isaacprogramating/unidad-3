# Función para validar y convertir a número flotante
def ingresar_numero(mensaje):
    while True:
        try:
            num = float(input(mensaje))
            return num
        except ValueError:
            print("Error: Debe ingresar un número válido.")

# Función para sumar dos números
def sumar(a, b):
    return a + b

# Función para restar dos números
def restar(a, b):
    return a - b

# Función para multiplicar dos números
def multiplicar(a, b):
    return a * b

# Función para dividir dos números
def dividir(a, b):
    if b != 0:
        return a / b
    else:
        print("Error: No se puede dividir por cero.")
        return None

# Función principal para ejecutar la calculadora mejorada
def calculadora_mejorada():
    # Solicitar y validar el primer número
    num1 = ingresar_numero("Ingrese el primer número: ")

    # Solicitar y validar el segundo número
    num2 = ingresar_numero("Ingrese el segundo número: ")

    # Mostrar menú de operaciones
    print("\nSeleccione la operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    # Solicitar opción al usuario
    while True:
        try:
            opcion = int(input("Ingrese el número de la operación deseada (1/2/3/4): "))
            if opcion in [1, 2, 3, 4]:
                break
            else:
                print("Opción inválida. Ingrese 1, 2, 3 o 4.")
        except ValueError:
            print("Error: Debe ingresar un número.")

    # Realizar la operación seleccionada
    if opcion == 1:
        resultado = sumar(num1, num2)
        print(f"\nResultado de la suma: {resultado}")
    elif opcion == 2:
        resultado = restar(num1, num2)
        print(f"\nResultado de la resta: {resultado}")
    elif opcion == 3:
        resultado = multiplicar(num1, num2)
        print(f"\nResultado de la multiplicación: {resultado}")
    elif opcion == 4:
        resultado = dividir(num1, num2)
        if resultado is not None:
            print(f"\nResultado de la división: {resultado}")

# Ejecutar la calculadora mejorada
calculadora_mejorada()
