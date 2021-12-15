import formatos


formatos.entrada(44)

preco_normal = float(input('Valor total da compra: R$'))

print('''FORMAS DE PAGAMENTO
[ 1 ] À vista Dinheiro/Cheque
[ 2 ] À vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão\n''')

condicao_pgto = int(input('Qual opção de pagamento? '))

if condicao_pgto == 1:
    preco_final = preco_normal * 0.90
elif condicao_pgto == 2:
    preco_final = preco_normal * 0.95
elif condicao_pgto == 3:
    preco_final = preco_normal
    qtd_parcela = 2
    preco_parcela = preco_final / qtd_parcela
    print(f'Sua compra será parcelada em {qtd_parcela}x de R${preco_parcela:.2f} SEM JUROS')
elif condicao_pgto == 4:
    qtd_parcela = int(input('Quantas parcelas? '))
    preco_final = preco_normal * 1.2
    preco_parcela = preco_final / qtd_parcela
    if 13 > qtd_parcela >= 3:
        print(f'Sua compra será parcelada em {qtd_parcela}x de R${preco_parcela:.2f} COM JUROS')
    else:
        print('Quantidade de PARCELAS INVÁLIDA.')
else:
    preco_final = preco_normal
    formatos.vermelho()
    print('OPÇÃO INVÁLIDA de pagamento.')

print(f'Sua compra de R${preco_normal:.2f} vai custar R${preco_final:.2f} no final.')

formatos.saida(44)
