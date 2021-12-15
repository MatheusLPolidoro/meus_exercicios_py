import formatos


def azul():
    print('\033[36m')


def amarelo():
    print('\033[33m')


def vermelho():
    print('\033[31m')


def verde():
    print('\033[32m')


def close():
    print('\033[m')


formatos.entrada(30)

azul()
amarelo()
num = int(input('\nDigite um número para saber se ele é PAR ou ÍMPAR: '))
if num % 2 != 0:
    resp = 'Ímpar'
else:
    resp = 'Par'
verde()
print(f'O número {num} é {resp}.\n')
azul()
close()

formatos.saida(30)
