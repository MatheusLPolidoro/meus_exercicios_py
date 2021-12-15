import formatos


formatos.entrada(81)

lista = list()
while True:
    num = int(input('Informe um número: '))
    lista.append(num)
    while True:
        op = str(input('Deseja continuar? [S/N] ')).strip().upper()
        if op in 'SN':
            break
    if op == 'N':
        break
print(f'Foram digitados {len(lista)} números')
print(f'A lista em ordem decrescente {sorted(lista, reverse=True)}')
if 5 in lista:
    resultado = 'foi digitado e esta na lista.'
else:
    resultado = 'não foi encontrado na lista.'
print(f'O valor 5 {resultado}')

formatos.saida(81)
