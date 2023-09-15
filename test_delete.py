import requests
from requests.auth import HTTPBasicAuth

usuario =  'douglas.tinoco.dev'
senha = 'dell.1234'
cabecalho = {'Authorization': 'Token aa72792863257ab2006eb2cb146a3ebf6796ee04'}

url_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
url_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'


delete_avaliacoes = requests.delete(url=f'{url_avaliacoes}11/', headers=cabecalho, auth=HTTPBasicAuth(usuario, senha))


assert delete_avaliacoes.status_code == 204

assert len(delete_avaliacoes.text) == 0