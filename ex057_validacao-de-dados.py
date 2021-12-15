import formatos


formatos.entrada(57)

sexo = ' '
while not sexo in 'FM':
    sexo = str(input('Sexo: ')).strip().upper()
    if not sexo[0] in 'FM':
        print(f'O sexo {sexo} está inválido, digite novamente.')
print(f'O sexo é {sexo} válidado!')

formatos.saida(57)
