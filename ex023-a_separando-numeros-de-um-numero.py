import formatos


formatos.entrada('23-a')

n = str(input('\nDigite um númeoro de 0 a 9999: '))
n = '{:0>4}'.format(n[:4])
unidade = n[3]
dezena = n[2]
centena = n[1]
milhar = n[0]
print('\nUnidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}\n'.format(unidade, dezena, centena, milhar))

formatos.saida('23-a')
