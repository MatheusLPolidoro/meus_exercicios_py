from datetime import date
import formatos


formatos.entrada(41)

idade = date.today().year - int(input('Informe o ano de seu nascimento: '))
print(f'O atleta tem {idade} anos.\nClassificação: ',end='')
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 25:
    print('SÊNIOR')
elif idade > 25:
    print('MASTER')

formatos.saida(41)
