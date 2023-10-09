import json

data = {}

data["clientes"] = []

data['clientes'].append({
    'first_name': 'Sigrid',
    'last_name': 'Mannock',
    'age': 27,
    'amount': 7.17})

data['clientes'].append({
    'first_name': 'Facundo',
    'last_name': 'Rodriguez',
    'age': 29,
    'amount': [9.17, 5.50]})

data['clientes'].append({
    'first_name': 'Sergio',
    'last_name': 'Carolo',
    'age': 47,
    'amount': 5.17})

# Escribir los datos en el archivo JSON
with open("miarchivojson.json", "w") as file:
    json.dump(data, file, indent=4)

# Leer los datos desde el archivo JSON
with open("miarchivojson.json", "r") as file:
    data_lectura = json.load(file)

# Iterar y mostrar los datos
for client in data_lectura['clientes']:
    print('First name:', client['first_name'])
    print('Last name:', client['last_name'])
    print('Age:', client['age'])
    print('Amount:', client['amount'])
    print('')
