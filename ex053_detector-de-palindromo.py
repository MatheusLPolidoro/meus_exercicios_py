import formatos


formatos.entrada(53)

frase = str(input('Uma frase qualquer: ')).replace(' ', '').upper()
frase_invertida = frase[::-1]

# for letra in frase:
#     frase_invertida = letra + frase_invertida

print(f'O inverso de {frase} é {frase_invertida}')

if frase == frase_invertida:
    print('A frase é um PALÍNDROMO, os seja, é a mesma lida ao contrário sem os espaços.')
else:
    print('A frase não é um POLÍNDROMO.')

formatos.saida(53)
