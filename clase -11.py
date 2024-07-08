# Función para sumar dos números enteros
def sumar(a, b):
    return a + b

# Función para restar dos números enteros
def restar(a, b):
    return a - b

# Función para multiplicar dos números enteros
def multiplicar(a, b):
    return a * b

# Función para dividir dos números enteros
def dividir(a, b):
    if b != 0:
        return a / b
    else:
        print("Error: No se puede dividir por cero.")
        return None

# Función principal para ejecutar la calculadora
def calculadora():
    # Solicitar y validar el primer número
    while True:
        try:
            num1 = float(input("Ingrese el primer número: "))
            break
        except ValueError:
            print("Error: Debe ingresar un número válido.")

    # Solicitar y validar el segundo número
    while True:
        try:
            num2 = float(input("Ingrese el segundo número: "))
            break
        except ValueError:
            print("Error: Debe ingresar un número válido.")

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

# Ejecutar la calculadora
calculadora()
