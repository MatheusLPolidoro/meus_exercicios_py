import formatos

formatos.entrada(9)

n = int(input('\nDigite um  número para ver sua tabuada: '))
print('-'*15)
for value in range(1, 11):
    print('{} X  {:<2} = {:<2}'.format(n, value, n * value))
print('-'*20)

formatos.saida(9)
