import formatos


formatos.entrada(75)

numeros = (int(input('Informe um número: ')),
           int(input('Informe outro número: ')),
           int(input('Informe mais um número: ')),
           int(input('Informe o último número: ')))
print('-='*30)
print(f'Os valores digitados foram {" ◄► ".join(map(str, numeros))}')
print(f'O valor 9 aparece {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O primero valor 3 apareceu na {numeros.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi digitado.')
print(f'Os números pares digitados foram: {" ◄► ".join(map(str, (n for n in numeros if n % 2 == 0)))}')

formatos.saida(75)
