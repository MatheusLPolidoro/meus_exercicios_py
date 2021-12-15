import formatos


formatos.entrada(5)

n = int(input('\nDigite um número!\n'))
print('\nAnalisando o valor {} ......\n\nAnalisado! Seu antecessor é {} e o sucessor é {}\n'.format(n, n-1, n+1))

formatos.saida(5)
