print('{:=^100}'.format(' DESAFIO 9 '))
n = int(input('\nDigite um  número para ver sua tabuada: '))
print('-'*15)
for value in range(1, 11):
    print('{} X  {:<2} = {:<2}'.format(n, value, n * value))
print('-'*20)
print('{:=^100}'.format(' FIM DESAFIO 9 '))