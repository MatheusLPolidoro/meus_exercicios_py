import formatos


formatos.entrada(85)

numeros = list()
par = list()
impar = list()
for i in range(1, 8):
    num = int(input(f'Informe o {i}ª valor: '))
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
numeros.append(sorted(par[:]))
numeros.append(sorted(impar[:]))
print(f'Os números pares são: {numeros[0]}')
print(f'Os números ímpares são: {numeros[1]}')

formatos.saida(85)
