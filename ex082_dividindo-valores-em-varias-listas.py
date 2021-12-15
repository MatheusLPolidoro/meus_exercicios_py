import formatos


formatos.entrada(82)

lista = []
while True:
    num = int(input('Informe um valor: '))
    lista.append(num)
    while True:
        op = str(input('Deseja continuar? [S/N] ')).strip().upper()
        if op in 'SN':
            break
    if op == 'N':
        break
par = [p for p in lista if p % 2 == 0]
impar = [p for p in lista if p % 2 == 1]
print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')

formatos.saida(82)
