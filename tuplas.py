# Ejercicio 1: Información Personal
def ejercicio1():
    # 1. Crear la tupla `informacion` con nombre, edad y ciudad:
    informacion = ("Juan", 30, "Puerto Montt")
    
    # 2. Acceder e imprimir cada elemento de la tupla utilizando índices:
    print("Nombre:", informacion[0])
    print("Edad:", informacion[1])
    print("Ciudad:", informacion[2])
    
    # 3. Utilizar desempaquetado de tuplas para asignar valores a variables individuales:
    nombre, edad, ciudad = informacion
    print("Nombre:", nombre)
    print("Edad:", edad)
    print("Ciudad:", ciudad)

# Ejercicio 2: Operaciones con Tuplas Numéricas
def ejercicio2():
    # 1. Crear la tupla `numeros` con los números del 1 al 10:
    numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    
    # 2. Calcular la suma de los elementos de la tupla usando `sum()`:
    suma_numeros = sum(numeros)
    print("Suma de los números:", suma_numeros)
    
    # 3. Encontrar el valor máximo y mínimo en la tupla usando `max()` y `min()`:
    maximo = max(numeros)
    minimo = min(numeros)
    print("Máximo valor:", maximo)
    print("Mínimo valor:", minimo)
    
    # 4. Contar cuántas veces aparece el número 5 en la tupla usando `count()`:
    veces_numero_5 = numeros.count(5)
    print("Número de veces que aparece el 5:", veces_numero_5)

# Ejercicio 3: Rebanado de Tuplas
def ejercicio3():
    # 1. Crear la tupla `letras` con las letras del alfabeto de 'a' a 'j':
    letras = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
    
    # 2. Obtener e imprimir la sub-tupla con las primeras 5 letras:
    primeras_cinco = letras[:5]
    print("Primeras cinco letras:", primeras_cinco)
    
    # 3. Obtener e imprimir la sub-tupla con las últimas 3 letras:
    ultimas_tres = letras[-3:]
    print("Últimas tres letras:", ultimas_tres)
    
    # 4. Obtener e imprimir la sub-tupla con cada segunda letra:
    cada_segunda = letras[::2]
    print("Cada segunda letra:", cada_segunda)

# Función principal para ejecutar todos los ejercicios
def main():
    print("--- Ejercicio 1: Información Personal ---")
    ejercicio1()
    
    print("\n--- Ejercicio 2: Operaciones con Tuplas Numéricas ---")
    ejercicio2()
    
    print("\n--- Ejercicio 3: Rebanado de Tuplas ---")
    ejercicio3()

# Ejecutar la función principal
if __name__ == "__main__":
    main()
