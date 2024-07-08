# Función para validar que todos los elementos ingresados sean números enteros
def validar_lista_numeros():
    while True:
        numeros_str = input("Ingrese una lista de números enteros separados por espacios: ")
        numeros_lista = numeros_str.split()
        
        try:
            numeros_enteros = [int(num) for num in numeros_lista]
            return numeros_enteros
        except ValueError:
            print("Error: Por favor ingrese únicamente números enteros.")

# Función para identificar números pares e impares
def identificar_pares_impares(numeros):
    pares = []
    impares = []
    
    for num in numeros:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
    
    return pares, impares

# Función para mostrar los resultados
def mostrar_resultados(pares, impares):
    print("\nNúmeros pares:")
    if pares:
        print(", ".join(map(str, pares)))
    else:
        print("No hay números pares en la lista.")
    
    print("\nNúmeros impares:")
    if impares:
        print(", ".join(map(str, impares)))
    else:
        print("No hay números impares en la lista.")

# Función principal del programa
def main():
    print("Programa para identificar números pares e impares en una lista.")
    numeros = validar_lista_numeros()
    pares, impares = identificar_pares_impares(numeros)
    mostrar_resultados(pares, impares)

# Ejecutar el programa
if __name__ == "__main__":
    main()
