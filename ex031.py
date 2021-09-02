def azul():
    print('\033[36m')
def amarelo():
    print('\033[33m')
def vermelho():
    print('\033[31m')
def verde():
    print('\033[32m')
def close():
    print('\033[m')
azul()
print('{:=^100}'.format(' DESAFIO 31 '))
verde()
dist = input('\nDiga a distância (Km) da viagem: ').strip()
while not dist.isnumeric() or float(dist) <= 0:
    dist = input('Digite uma distância (Km) valida: ')
amarelo()
if float(dist) > 200:
    p = float(dist) * 0.45
else:
    p = float(dist) * 0.50
print(f'O custo da viagem de {dist} Km é de R$ {p:.2f}')
azul()
print('{:=^100}'.format(' FIM DESAFIO 31 '))
close()
