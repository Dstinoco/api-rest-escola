import requests
from requests.auth import HTTPBasicAuth

usuario =  'douglas.tinoco.dev'
senha = 'dell.1234'
cabecalho = {'Authorization': 'Token aa72792863257ab2006eb2cb146a3ebf6796ee04'}

url_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
url_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'




resultado_curso = requests.get(url=url_cursos, headers=cabecalho, auth=HTTPBasicAuth(usuario, senha))

resultado_avaliacao = requests.get(url=url_avaliacoes, headers=cabecalho)


assert resultado_curso.status_code == 200
assert resultado_avaliacao.status_code == 200


assert resultado_curso.json()['count'] == 7
assert resultado_avaliacao.json()['count'] == 6




