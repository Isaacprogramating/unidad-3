def caso3():
    # Crear arreglo [10][4] simulando un bus
    bus = []
    num_asiento = 1
    
    for i in range(10):
        fila = []
        for j in range(4):
            fila.append(num_asiento)
            num_asiento += 1
        bus.append(fila)
    
    # Mostrar el bus por pantalla
    for fila in bus:
        for asiento in fila:
            print(asiento, end=" ")
        print()  # Salto de línea entre filas

# Ejecutar el caso 3
caso3()
 