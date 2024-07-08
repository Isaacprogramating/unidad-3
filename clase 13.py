import statistics
from collections import Counter

def calcular_estadisticas(archivo):
    try:
        # Abrir el archivo para lectura
        with open(archivo, 'r') as file:
            # Leer todas las líneas y convertirlas a números enteros
            numeros = [int(line.strip()) for line in file.readlines()]
            
            # Calcular el promedio
            promedio = sum(numeros) / len(numeros)
            
            # Calcular la mediana
            numeros.sort()
            if len(numeros) % 2 == 0:
                mediana = (numeros[len(numeros)//2 - 1] + numeros[len(numeros)//2]) / 2
            else:
                mediana = numeros[len(numeros)//2]
            
            # Calcular la moda
            moda = statistics.mode(numeros)
            
            # Encontrar todas las modas si hay más de una
            frecuencias = Counter(numeros)
            modas = [numero for numero, frecuencia in frecuencias.items() if frecuencia == frecuencias.most_common(1)[0][1]]
            
            # Imprimir resultados
            print(f"Promedio: {promedio}")
            print(f"Mediana: {mediana}")
            print(f"Moda: {', '.join(map(str, modas))}")
    
    except FileNotFoundError:
        print(f"Error: El archivo '{archivo}' no fue encontrado.")
    except ValueError:
        print(f"Error: El archivo '{archivo}' contiene datos no numéricos.")


