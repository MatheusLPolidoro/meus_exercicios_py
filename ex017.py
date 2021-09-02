from math import hypot as h
print('{:=^100}'.format(' DESAFIO 17 '))
cateto_oposto = float(input('\nQual é o comprimento do cateto oposto? '))
cateto_adjacente = float(input('Qual é o comprimento do cateto adjacente? '))
print('\nO comprimento da hipotenusa é de {:.2f}.\n'.format(h(cateto_oposto, cateto_adjacente)))
print('{:=^100}'.format(' FIM DESAFIO 17 '))