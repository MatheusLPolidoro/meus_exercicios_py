import formatos


formatos.entrada(60)

num = int(input('Informe um número inteiro: '))
i = num - 1
print(f'{num}! = {num} X ', end='')
while i != 0:
    num *= i
    print(f'{i}', end='')
    if i != 1:
        print(' X ', end='')
    i -= 1
print(f' = {num}')

formatos.saida(60)
