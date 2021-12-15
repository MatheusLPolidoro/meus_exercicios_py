import formatos as ft


ft.entrada(38)

num1 = int(input('Informe um número inteiro: '))
num2 = int(input('Informe outro número inteiro: '))

if num1 > num2:
    print('O PRIMEIRO valor é maior.')
elif num2 > num1:
    print('O SEGUNDO valor é maior.')
else:
    print('Não existe valor maior, os números são iguais.')

ft.saida(38)
