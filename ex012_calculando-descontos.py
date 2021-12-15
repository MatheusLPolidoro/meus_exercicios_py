import formatos


formatos.entrada(12)

preço_produto = float(input('\nQual é o preço do produto?\nR$ '))
print('\nO produto custava R$ {:.2f}, com desconto de 5% vai custar R$ {:.2f}\n'.format(preço_produto, preço_produto * 0.95))

formatos.saida(12)
