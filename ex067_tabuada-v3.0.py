import formatos


formatos.entrada(67)

while True:
    num = int(input('Qual tabuada você deseja exibir? '))
    if num < 0:
        break
    for i in range(1, 11):
        resultado = num * i
        print(f'{num:>2} X {i:>2} = {resultado:>2}')

formatos.saida(67)
