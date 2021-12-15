from random import randint
from time import sleep
import formatos


formatos.entrada(45)

print('''Suas opções:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA
''')
opcoes = {
    1: 'PEDRA',
    2: 'PAPEL',
    3: 'TESOURA'
}
escolha_humano = int(input('Sua jogada: '))

if escolha_humano in (1, 2, 3):
    print('JO')
    sleep(.7)
    print('KEN')
    sleep(.7)
    print('PO!!!')
    sleep(.7)

    escolha_maquina = randint(1, 3)
    print('=-'*30)
    print(f'Maquina jogou {opcoes[escolha_maquina]}')
    print(f'Jogador jogou {opcoes[escolha_humano]}')
    print('=-'*30)

    if escolha_humano == escolha_maquina:
        print('EMPATE')
    elif escolha_humano == 1 and escolha_maquina == 3 or escolha_humano == 2 and escolha_maquina == 1 or escolha_humano == 3 and escolha_maquina == 2:
        print(f'JOGADOR VENCE')
    else:
        print(f'MAQUINA VENCE')
else:
    print('Escolha INVÁLIDA.')

formatos.saida(45)
