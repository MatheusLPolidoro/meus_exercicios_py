import formatos


formatos.entrada(6)

n = int(input('\nDigite um número: '))
print('\nO dobro de {} vale {}.\nO triplo de {} vale {}.\nA raiz quadrada de {} é igual a {:.2f}.\n'.format(n, n * 2, n, n * 3, n, n ** (1 / 2)))

formatos.saida(6)
