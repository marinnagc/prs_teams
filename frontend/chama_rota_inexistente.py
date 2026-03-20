import requests

# Frontend simulando chamada para uma rota existente
response = requests.get('http://localhost:5000/rota-existente')

if response.status_code == 404:
    print('Erro: Rota não encontrada no backend!')
else:
    print('Resposta:', response.text)
