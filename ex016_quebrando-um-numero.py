from math import floor as m
import formatos


formatos.entrada(16)

n = float(input('\nDigite um número: '))
print('O número {} tem sua porção inteira {}.\n'.format(n, m(n)))

formatos.saida(16)
