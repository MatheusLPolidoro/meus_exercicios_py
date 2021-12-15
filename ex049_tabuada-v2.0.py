import formatos


formatos.entrada(49)

num = int(input('Tabuado do: '))
for i in range(1, 11):
    print(f'{num:2} X {i:2} = {num * i:2}')

formatos.saida(49)
