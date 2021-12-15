import formatos


formatos.entrada(50)
total = 0
for i in range(1,7):
    num = int(input(f'Informe o {i}ª número: '))
    if num % 2 == 0:
        total += num

print(f'A soma dos números pares é igual: {total}')

formatos.saida(50)
