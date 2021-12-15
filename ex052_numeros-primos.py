import formatos


formatos.entrada(52)

num = int(input('Informe um número inteiro: '))
qtd_dividido = 0

for i in range(1, num + 1):
    formatos.vermelho()
    if num % i == 0:
        formatos.amarelo()
        qtd_dividido += 1
    print(f'{i}', end=' ') 

formatos.close()

print(f'\nO número {num} foi dividido {qtd_dividido} vezes')
if qtd_dividido == 2:
    formatos.verde()
    print(f'E por isso é primo.')
else:
    formatos.vermelho()
    print(f'E por isso não é primo.')

formatos.saida(52)
