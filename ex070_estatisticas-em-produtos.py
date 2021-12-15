import formatos


formatos.entrada(70)

print('-'*35 + f'\n{"LOJA PYTHONYCA":^35}\n' + '-'*35)
menor = total = valor_acima = 0

while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    total += preco
    if preco > 1000:
        valor_acima += 1
    if not menor:
        nome_menor = nome
        menor = preco
    if preco < menor:
        nome_menor = nome
        menor = preco
    while True:
        op = str(input('Quer continuar? [S/N] ')).strip().upper()
        if op in 'SN':
            break
    if op[0] == 'N':
        break
    print('-'*35)
print(f'{"SALDO":=^35}')
print(f'O total da compra foi R${total}')
print(f'Temos {valor_acima} compras acima de R$1000.00')
print(f'O produto mais barato foi {nome_menor} que custa R${menor}')

formatos.saida(70)
