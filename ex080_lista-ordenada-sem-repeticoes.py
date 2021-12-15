import formatos


formatos.entrada(80)

lista = list()
for numeros in range(0, 5):
    num = int(input(f'Digite um valor: '))
    if not len(lista) or num > lista[-1]:
        pos = len(lista)
        lista.append(num)
    else:
        for i, item in enumerate(lista):
            if num <= item:
                lista.insert(i, num)
                pos = i
                break
    print(f'O valor {num} foi inserido na posição {pos}ª')
print(f'Os valores digitados em ordem são {lista}')

formatos.saida(80)
