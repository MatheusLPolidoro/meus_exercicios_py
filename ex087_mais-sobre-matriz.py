import formatos


formatos.entrada(87)

matriz = list()
linha = list()
par = soma_coluna = maior_linha = 0
for lin in range(0, 3):
    for col in range(0, 3):
        num = int(input(f'Digite um valor para [{lin}, {col}]: '))
        if num % 2 == 0:
            par += num
        if col == 2:
            soma_coluna += num
        linha.append(num)
    if lin == 1:
        maior_linha = max(linha)
    matriz.append(linha[:])
    linha.clear()
print('-='*30)
for lin in matriz:
    for col in lin:
        print(f'[  {col}  ]', end='')
    print('')
print('-='*30)
print(f'A soma de todos os valores pares é de {par}')
print(f'A soma dos valores da tereira coluna é {soma_coluna}')
print(f'O maior valor da segunda linha é {maior_linha}')

formatos.saida(87)
