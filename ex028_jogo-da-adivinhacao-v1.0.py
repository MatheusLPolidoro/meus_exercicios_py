from random import randint
from time import sleep
import formatos


def azul():
    print('\033[36m')


def amarelo():
    print('\033[33m')


def vermelho():
    print('\033[31m'),


def verde():
    print('\033[32m')


def close():
    print('\033[m')


formatos.entrada(28)

azul()
amarelo()
num_input = int(input('Vou processar um número de 0 a 5, tente advinhar: '))
while num_input < 0 or num_input > 5:
    num_input = int(input('O número não é de 0 a 5, tente de novo: '))
vermelho()
print('Processando...')
sleep(2)
num_random = randint(0, 5)
if num_input == num_random:
    verde()
    print(f'Parabéns! Você acertou o número processado foi {num_input}.')
else:
    vermelho()
    print(f'Você errou!!O número processado foi {num_random}.\n')
azul()
close()

formatos.saida(28)
