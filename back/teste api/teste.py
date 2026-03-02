import requests
cep = "08020150"
url = f"https://viacep.com.br/ws/{cep}/json/"
response = requests.get(url)

if response.status_code == 200:
    dados = response.json()
    print(f"Rua: {dados['logradouro']}")
    print(f"Bairro: {dados['bairro']}")
    print(f"Cidade: {dados['localidade']}")
else:
    print(f"erro ao buscar CEP: {response.status_code}")
    