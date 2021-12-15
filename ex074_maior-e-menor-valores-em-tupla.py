import formatos
from random import randint


formatos.entrada(74)

numeros = (randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9))

print(f'Os números sorteados foram: {" - ".join(map(str, numeros))}')
print(f'O MENOR número é: {min(numeros)}')
print(f'O MAIOR número é: {max(numeros)}')

formatos.saida(74)
