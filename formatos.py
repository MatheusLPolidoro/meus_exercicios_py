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
def entrada(x):
    print('\033[36m{:=^100}'.format(' DESAFIO ' + str(x) + ' '))
    print('\033[m')
def saida(y):
    print('\n\033[36m{:=^100}'.format(' FIM DESAFIO ' + str(y) + ' '))
    print('\033[m')