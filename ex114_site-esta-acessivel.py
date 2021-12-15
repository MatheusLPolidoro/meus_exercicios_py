import formatos
import urllib.request


formatos.entrada(114)

try:
    site = urllib.request.urlopen('https://www.bcb.gov.br/')
except urllib.error.URLError:
    print('Erro! Site do banco central não acessado.')
else:
    print('Acessado com sucesso o site do banco central!')

formatos.saida(114)
