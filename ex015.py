print('{:=^100}'.format(' DESAFIO 15 '))
dia = int(input('\nQuantos dias alugado? '))
km = float(input('Quantos Km rodados? '))
print('São {} dias e {:.2f}Km rodados, o valor total do aluguel é de R$ {:.2f}!\n'.format(dia, km, (dia * 60) + (km * 0.15) ))
print('{:=^100}'.format(' FIM DESAFIO 15 '))