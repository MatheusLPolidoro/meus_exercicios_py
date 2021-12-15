import formatos


formatos.entrada(73)

numeros_por_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    while True:
        n = int(input('Informe um número de 0 a 20: '))
        if 0 <= n <= 20:
            break
        print('Número inválido, tente novamente....')

    print(f'Você digitou o número {numeros_por_extenso[n]}')
    while True:
        op = str(input('Quer continuar? [S/N] ')).strip().upper()
        if op in 'SN':
            break
    if op == 'N':
        break

formatos.saida(73)
