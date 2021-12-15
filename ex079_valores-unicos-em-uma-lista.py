import formatos


formatos.entrada(79)

lista = list()
while True:
    num = int(input('Digite um valor: '))
    if not num in lista:
        lista.append(num)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado, não vou adicionar...')
    while True:
        op = str(input('Quer continuar? [S/N] ')).strip().upper()
        if '' != op in 'SN':
            break
    if op == 'N':
        break
print('-='*30, f'\nVocê digitou os valores {sorted(lista)}')

formatos.saida(79)
