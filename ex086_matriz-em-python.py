import formatos


formatos.entrada(86)

matriz = list()
linha = list()
for lin in range (0, 3):
    for col in range(0, 3):
        num = int(input(f'Digite um valor para [{lin}, {col}]: '))
        linha.append(num)
    matriz.append(linha[:])
    linha.clear()
for lin in matriz:
    for col in lin:
        print(f'[  {col}  ]', end='')
    print('')
    
formatos.saida(86)
