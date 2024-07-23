import csv
import time
import requests

# Substitua 'seu_arquivo.csv' pelo caminho do seu arquivo CSV
csv_file_path = 'registro_passagens.csv'

# Usei o Mockoon para simular um endpoint
endpoint_url = 'http://localhost:3000'

# Abre o arquivo CSV e envia os dados para o endpoint
with open(csv_file_path, mode='r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Substitua os campos abaixo pelos nomes das colunas do seu CSV
        payload = {
            'Nome': row['Nome'],
            'Telefone': row['Telefone'],
            'NumeroPassagem': row['Numero da passagem'],
            'HorarioIda': row['Horario de ida'],
            'HorarioVolta': row['Horario de volta'],
            'Destino': row['Destino'],
            'Origem': row['Origem'],
        }

        time.sleep(1)

        response = requests.post(endpoint_url, json=payload)
        if response.status_code == 200:
            print(f"Registro com Nome {row['Nome']} enviado com sucesso.")
        else:
            print(f"Erro ao enviar registro com Id {row['Nome']}. Código de status: {response.status_code}")
