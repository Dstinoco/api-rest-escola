import jsonpath
import requests


avaliacoes = requests.get(url= 'http://127.0.0.1:8000/api/v2/avaliacoes/')

busca = jsonpath.jsonpath(avaliacoes.json(), 'results[*].email')[0]

print(busca)