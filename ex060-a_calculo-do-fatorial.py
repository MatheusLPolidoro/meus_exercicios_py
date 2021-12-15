import formatos


formatos.entrada(60)

num = int(input('Entre com um número inteiro: '))
print(f'{num}! = ', end='')
for i in range(num, 0, -1):
    print(f'{i} ', end='')
    if i != 1:
        num *= (i - 1)
        print('X ', end='')
print(f'= {num}')

formatos.saida(60)
