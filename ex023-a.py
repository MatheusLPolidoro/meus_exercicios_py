print('{:=^100}'.format(' DESAFIO 23-A '))
n = str(input('\nDigite um númeoro de 0 a 9999: '))
n = '{:0>4}'.format(n[:4])
unidade = n[3]
dezena = n[2]
centena = n[1]
milhar = n[0]
print('\nUnidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}\n'.format(unidade, dezena, centena, milhar))
print('{:=^100}'.format(' FIM DESAFIO 23-A '))