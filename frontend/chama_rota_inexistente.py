import requests

# Frontend simulando chamada para uma rota inexistente
response = requests.get('http://localhost:5000/rota-inexistente')

if response.status_code == 404:
    print('Erro: Rota não encontrada no backend!')
else:
    print('Resposta:', response.text)
