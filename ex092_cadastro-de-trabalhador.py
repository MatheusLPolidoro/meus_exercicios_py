import formatos
from datetime import date


formatos.entrada(92)

dados = dict()
dados['nome'] = str(input('Nome: '))
dados['idade'] = date.today().year - int(input('Ano de nascimeno: '))
dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if dados['ctps']: 
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$ '))
    dados['aposentadoria'] = dados['idade'] + (dados['contratação'] + 35) - date.today().year
print('-=' * 30)
for k, v in dados.items():
    print(f'\t - {k} tem o valor {v}')

formatos.saida(92)
