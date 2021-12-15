import formatos


formatos.entrada(66)

i = total = 0
while True:
    num = int(input('Informe um número (999 para parar): '))
    if num == 999:
        break
    total += num
    i += 1
print(f'Foram digitados {i} números\nA soma deles é {total}.')

formatos.saida(66)
