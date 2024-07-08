import csv
import json

# Función para determinar si una persona es mayor de edad (mayor o igual a 18 años)
def es_mayor_de_edad(edad):
    return edad >= 18

# Lista para almacenar las personas mayores o iguales a 25 años
mayores = []

# Lectura del archivo CSV 'datos.csv'
with open('datos.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        nombre = row['Nombre']
        edad = int(row['Edad'])
        comuna = row['Comuna']
        
        # Determinar si la persona es mayor de edad
        if es_mayor_de_edad(edad):
            estado_edad = 'Mayor de edad'
            # Agregar a la lista de mayores si tiene 25 años o más
            if edad >= 25:
                mayores.append({
                    'nombre': nombre,
                    'edad': edad,
                    'comuna': comuna
                })
        else:
            estado_edad = 'Menor de edad'
        
        # Imprimir la información de la persona en la consola
        print(f"Nombre: {nombre}, Edad: {edad}, Comuna: {comuna}, Estado: {estado_edad}")

# Guardar la lista 'mayores' en un archivo JSON 'mayores.json'
with open('mayores.json', 'w') as jsonfile:
    json.dump(mayores, jsonfile, indent=4)

print("Archivo 'mayores.json' creado satisfactoriamente.")
