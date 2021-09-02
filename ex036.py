import formatos
formatos.entrada(36)
formatos.azul()
vlr_casa = float(input('Valor total do ímovel (R$): '))
salario = float(input('Salário do comprador: '))
anos = int(input('Quantos anos deseja pagar: '))
qtd_p = anos * 12
if vlr_casa / qtd_p > 0.30 * salario:
 formatos.vermelho()
 print(f'De acordo com o valor do ímovel R${vlr_casa:.2f} em {qtd_p} parcelas, o financiamento foi negado!')
 formatos.amarelo()
 print('\nVocê pode tentar com mais parcelas...')
else:
 formatos.verde()
 print(f'Parábens, seu empréstimo foi aprovado!')
 formatos.amarelo()
 print('\nSegue relação:\n')
 formatos.azul()
 print(f'Valor total do ímovel: R$ {vlr_casa:.2f}\nQuantidades de parcelas {qtd_p}\nFinaciamento previsto em {anos} anos\nValor da parcela R$ {vlr_casa / qtd_p:.2f}')
formatos.saida(36)