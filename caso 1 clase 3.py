def caso1():
    # Crear matriz [3][4] y solicitar elementos numéricos por pantalla
    matriz = []
    for i in range(3):
        fila = []
        for j in range(4):
            elemento = int(input(f"Ingrese el elemento [{i}][{j}]: "))
            fila.append(elemento)
        matriz.append(fila)
    
    # Mostrar la matriz de forma ordenada
    for fila in matriz:
        for elemento in fila:
            print(elemento, end=" ")
        print()  # Salto de línea entre filas

# Ejecutar el caso 1
caso1()
