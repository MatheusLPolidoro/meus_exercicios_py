import formatos
from time import sleep


formatos.entrada(59)

op = -1
num1 = float(input('1ª valor: '))
num2 = float(input('2ª valor: '))

while op != 5:
    print('''---OPÇÕES---
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR
    ''')
    op = int(input('Qual sua opção: '))
    if op == 1:
        resultado = num1 + num2
        opstr = 'SOMA'
    elif op == 2:
        resultado = num1 * num2
        opstr = 'MULTIPLICAÇÃO'
    elif op == 3:
        if num1 == num2:
            resultado = 'Números iguais.'
        elif num1 > num2:
            resultado = 'O MAIOR é ' + str(num1)
        elif num2 > num1:
            resultado = 'O MAIOR é ' + str(num2)
        opstr = 'MAIOR'
    elif op == 4:
        num1 = float(input('1ª valor: '))
        num2 = float(input('2ª valor: '))
    elif op == 5:
        print('Saindo...')
        sleep(1)
    else:
        print('Opção inválida!Digite novamente.\n')

    if str(op) in '123':
        print(f'Você escolheu {opstr}\nRESPOSTA: {resultado}\n')
        sleep(1)

formatos.saida(59)
