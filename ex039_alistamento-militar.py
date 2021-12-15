from datetime import date
import formatos


formatos.entrada(39)

ano_nascimento = int(input('Informe o ano de seu nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

print(f'Quem nasceu em {ano_nascimento} tem {idade} anos.')

sexo = str(input('Qual seu sexo? [m] ou [f]: ')).lower().strip()

if sexo[0] == 'm':
    if idade > 18:
        print(f'Já passou {idade - 18} anos do tempo de alistamento.')
        print(f'Seu alistamento deve ter acontecido em {ano_atual-(idade - 18)}.')
    elif idade == 18:
        print('Você tem que se alistar IMEDIATAMENTE!')
    elif idade < 18:
        print(f'Faltam {18 - idade} anos para se alistar.')
        print(f'Seu alistamento será em {ano_atual + (18 - idade)}')

formatos.saida(39)
