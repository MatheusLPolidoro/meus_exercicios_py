import formatos
from random import randint


formatos.entrada(68)
formatos.verde()
formatos.titulo('VAMOS JOGAR PAR OU ÍMPAR')
formatos.close()

vitorias = derrotas = 0

while not derrotas:
    maquina = randint(0, 10)
    jogador = int(input('Diga um valor: '))
    escolha = str(input('Par ou Ímpar [P/I]? ')).strip().upper()
    total = maquina + jogador
    if total % 2 == 0 and escolha == 'P' or total % 2 == 1 and escolha == 'I':
        resultado = 'PAR' if escolha == 'P' else 'ÍMPAR'
        vitorias += 1
    elif total % 2 == 1 and escolha == 'P' or total % 2 == 0 and escolha == 'I':
        resultado = 'ÍMPAR' if escolha == 'P' else 'PAR'
        derrotas += 1
    print(f'Você jogou {jogador} e a maquina {maquina}. TOTAL {total} é {resultado}')
    if not derrotas:
        print('Você VENCEU!!\nVamos jogar novamente...')
        print('-='*50)

print(f'Você PERDEU!!\n\n------SCORE------\nVITÓRIAS:{vitorias}\nDERROTAS:{derrotas}')

formatos.saida(68)
