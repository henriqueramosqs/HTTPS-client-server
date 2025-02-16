import requests

url = "https://localhost:5000/secure-data"
data = {"message": "Teste de comunicação segura"}

# Envia a requisição HTTPS com verificação SSL
response = requests.post(url, json=data, cert=("client.crt", "client.key"), verify="server.crt")

# Exibe a resposta do servidor
if response.status_code == 200:
    print("Resposta do servidor:", response.json())
else:
    print("Erro na comunicação:", response.status_code)

# Teste enviando sem mensagem
response2 = requests.post(url, json={}, cert=("client.crt", "client.key"), verify="server.crt")
print(response2.json(), '------------ SEM MENSAGEM')

# Teste sem certificado
response3 = requests.post(url, json=data, cert=("client.crt", "client.key"), verify=False)
print(response2.json(), '------------ SEM CERTIFICADO')