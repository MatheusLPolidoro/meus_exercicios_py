import formatos


formatos.entrada(10)

din = float(input('\nQuanto dinheiro você tem na sua carteira?\nR$ '))
print('Com R$ {:.2f} você pode comprar U$ {:.2f}\n'.format(din, din / 5.30))

formatos.saida(10)
