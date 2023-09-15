import requests
from requests.auth import HTTPBasicAuth

usuario =  'douglas.tinoco.dev'
senha = 'dell.1234'
cabecalho = {'Authorization': 'Token aa72792863257ab2006eb2cb146a3ebf6796ee04'}

url_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
url_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'


corpo_novo_curso = {
    "titulo": "Teste Sistema",
    "url": "http://testesistema.test.com"
}

corpo_nova_avaliacoes = {
    "curso": 3,
    "nome": "Teste API",
    "email": "teste_api@api.com",
    "comentario": "testando API ",
    "avaliacao": 5
    
}


resultado_curso = requests.post(url=url_cursos, headers=cabecalho, auth=HTTPBasicAuth(usuario, senha), data=corpo_novo_curso)
resultado_avaliacoes = requests.post(url=url_avaliacoes, headers=cabecalho, auth=HTTPBasicAuth(usuario, senha), data=corpo_nova_avaliacoes)

resultado_avaliacoes_get = requests.get(url=url_avaliacoes, headers=cabecalho, auth=HTTPBasicAuth(usuario, senha), data=corpo_nova_avaliacoes)
resultado_curso_get = requests.get(url=url_cursos, headers=cabecalho, auth=HTTPBasicAuth(usuario, senha), data=corpo_novo_curso)

#assert resultado_curso.status_code == 201
#assert resultado_curso.json()["titulo"] == corpo_novo_curso["titulo"]

assert resultado_avaliacoes.status_code == 201
assert resultado_avaliacoes.json()["nome"] == corpo_nova_avaliacoes["nome"]