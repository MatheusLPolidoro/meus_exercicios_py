import formatos


formatos.entrada(65)
op = 'S'
i = total = maior = menor = 0
while op in 'S':
    num = int(input('Digite um número:'))
    if not i:
        maior = menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    total += num
    i += 1
    op = str(input('Deseja continuar [S/N]? ')).strip().upper()
media = total / i
print(f'A media entre os {i} números digitados é {media}')
print(f'O MAIOR valor digitado foi {maior}')
print(f'O MENOR valor digitado foi {menor}')

formatos.saida(65)
