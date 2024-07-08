import csv
import json

# Función para determinar si un run es ganador
def es_run_ganador(run):
    # Obtenemos los últimos dos dígitos antes del dígito verificador
    ultimos_digitos = run[-3:-1]
    # Revisamos si los últimos dígitos son 92, 95 o 84
    return ultimos_digitos in ['92', '95', '84']

# Lista para almacenar los run ganadores
ganadores = []

# Lectura del archivo CSV 'listadoRun.csv'
with open('listadoRun.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        run = row['run']
        nombre = row['nombre']
        
        # Determinar si el run es ganador
        if es_run_ganador(run):
            ganadores.append({
                'run': run,
                'nombre': nombre
            })

# Guardar la lista 'ganadores' en un archivo JSON 'ganadores.json'
with open('ganadores.json', 'w') as jsonfile:
    json.dump(ganadores, jsonfile, indent=4)

print("Archivo 'ganadores.json' creado satisfactoriamente.")
