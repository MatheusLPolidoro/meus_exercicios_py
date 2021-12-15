import formatos


formatos.entrada(76)

formatos.titulo('LISTAGEM DE PREÇOS', '-', 40)

estoque = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor',
           4.20, 'Comprasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livros', 34.90)

for produto in estoque:
    if str(produto).isalpha():
        print(f'{produto:.<30}R$', end='')
    else:
        print(f'{produto:>7.2f}')

formatos.saida(76)
