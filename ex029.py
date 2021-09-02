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
print('{:=^100}'.format(' DESAFIO 29 '))
verde()
km = int(input('\nQual é sua velocidade nesta pista? '))
azul()
if km <= 80 and km >= 60:
    print(f'Velocidade {km}km, está dentro do permitido. Continue assim!')
elif km < 60:
    vermelho()
    multa = (60 - km) * 7
    print(f'Velocidade {km}Km, abaixo do permitido, multa devida de R$ {multa:.2f}')
else:
    multa = (km - 80) * 7
    print(f'Velocidade {km}Km, acima do permitido, multa devida de R$ {multa:.2f}')
azul()
print('\n{:=^100}'.format(' FIM DESAFIO 29 '))
close()
