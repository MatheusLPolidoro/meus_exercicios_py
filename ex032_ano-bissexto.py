import formatos
import datetime


formatos.entrada(32)

formatos.amarelo()
ano = int(input('Digite um ano qualquer para seber se é bissexto: '))
if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'Ano {ano} é bissexto\n')
else:
    print(f'Ano {ano} não é bissexto\n')
    
formatos.saida(32)
