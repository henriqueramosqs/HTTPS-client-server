import requests

url = "https://localhost:5000/secure-data"
data = {"message": "Teste de comunicação segura HTTPS"}

try:
    # Envia a requisição HTTPS com verificação SSL
    response = requests.post(url, json=data, cert=("client.crt", "client.key"), verify="server.crt")
    print(response.json(), '------------ RETORNO DO SERVIDOR')

    # Teste enviando sem mensagem
    response2 = requests.post(url, json={}, cert=("client.crt", "client.key"), verify="server.crt")
    print(response2.json(), '------------ SEM MENSAGEM')

    # Teste sem certificado cliente
    response4 = requests.post(url, json=data, cert=(""), verify="server.crt")
    print(response4.json(), '------------ SEM CERTIFICADO CLIENTE')
except requests.exceptions.SSLError as e:
    print(f"Erro de SSL: {e}")
except requests.exceptions.RequestException as e:
    print(f"Erro na requisição: {e}")