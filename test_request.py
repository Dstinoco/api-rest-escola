import requests
from requests.auth import HTTPBasicAuth

titulo = 'HTML Básico'
url = "http://google.com/html"

corpo = {
    "titulo": titulo, 
    "url": url,
         }

corpo_nova_avaliacoes = {
    "curso": 1,
    "nome": "Teste API",
    "email": "teste_api@api.com",
    "comentario": "testando API",
    "avaliacao": 5
    
}


#get_avaliacoes = requests.get("http://127.0.0.1:8000/api/v2/avaliacoes")
#print(get_avaliacoes.json()['results'])

usuario =  'douglas.tinoco.dev'
senha = 'dell.1234'
cabecalho = {'Authorization': 'Token aa72792863257ab2006eb2cb146a3ebf6796ee04'}



#cursos = requests.post(url='http://127.0.0.1:8000/api/v2/cursos/',headers=cabecalho, data=corpo, auth=HTTPBasicAuth(usuario, senha))
cursos = requests.get(url='http://127.0.0.1:8000/api/v2/avaliacoes/',headers=cabecalho, auth=HTTPBasicAuth(usuario, senha))
print(cursos.status_code)
#print(cursos.json())


print(cursos.json()['results'][-1])
