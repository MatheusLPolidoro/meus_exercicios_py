import formatos
from time import sleep
from random import randint


def sorteia(qtd_numeros: int, inicio=0, fim=10) -> list:
    print(f'Sorteando {qtd_numeros} valores da lista: ', end='', flush=True)
    num = [(randint(inicio, fim)) for i in range(0, qtd_numeros)]
    for n in num:
        sleep(.5)
        print(n, end=' ', flush=True)
    print()
    return num


def somaPar(num=0):
    soma = 0
    if num:
        for n in num:
            if n % 2 == 0:
                soma += n
        print(f'Somando os valores pares de {", ".join(map(str, num))} temos {soma}')
        return soma


formatos.entrada(100)

num = sorteia(5)
somaPar(num)

formatos.saida(100)
