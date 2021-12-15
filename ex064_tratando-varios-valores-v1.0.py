import formatos


formatos.entrada(64)
i = total = num = 0
print('Digite 999 para sair...')
while num != 999:
    num = int(input(f'informe o {i + 1}ª número inteiro: '))
    if num != 999:
        total += num
        i += 1
print(f'Foram digitados {i} números\nA soma é {total}')

formatos.saida(64)
