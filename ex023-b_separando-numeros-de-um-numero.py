import formatos


formatos.entrada('23-b')

n = int(input('\nDigite um número de 0 a 9999: '))
unidade = n // 1 % 10
dezena = n // 10 % 10
centena = n // 100 % 10
milhar = n // 1000 % 10
print(f'\nUnidade: {int(unidade)}\nDezena: {int(dezena)}\nCentena: {int(centena)}\nmilhar: {int(milhar)}\n')

formatos.saida('23-b')
