def caso2():
    # Crear matriz [3][3][3] manualmente con valores predefinidos
    matriz = [
        [["amarillo", "rojo", "naranja"], ["verde", "blanco", "amarillo"], ["rojo", "amarillo", "naranja"]],
        [["verde", "blanco", "naranja"], ["blanco", "verde", "rojo"], ["amarillo", "naranja", "verde"]],
        [["blanco", "rojo", "amarillo"], ["naranja", "verde", "rojo"], ["amarillo", "rojo", "blanco"]]
    ]
    
    # Inicializar contadores para contar elementos
    contador_amarillo = 0
    contador_rojo = 0
    contador_naranja = 0
    contador_verde = 0
    contador_blanco = 0
    
    # Recorrer la matriz y contar elementos
    for capa in matriz:
        for fila in capa:
            for elemento in fila:
                if elemento == "amarillo":
                    contador_amarillo += 1
                elif elemento == "rojo":
                    contador_rojo += 1
                elif elemento == "naranja":
                    contador_naranja += 1
                elif elemento == "verde":
                    contador_verde += 1
                elif elemento == "blanco":
                    contador_blanco += 1
    
    # Mostrar la información de cantidad de elementos
    print(f"Número de elementos 'amarillo': {contador_amarillo}")
    print(f"Número de elementos 'rojo': {contador_rojo}")
    print(f"Número de elementos 'Naranja': {contador_naranja}")
    print(f"Número de elementos 'Verde': {contador_verde}")
    print(f"Número de elementos 'Blanco': {contador_blanco}")

# Ejecutar el caso 2
caso2()
