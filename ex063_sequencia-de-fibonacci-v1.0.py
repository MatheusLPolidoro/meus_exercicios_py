import formatos


formatos.entrada(63)

n = int(input('Quantos números da sequencia FIBONACCI você que mostrar: '))

resultado = anterior = 0
atual = 1

while n:  
    print(f'{resultado}', end=' → ')
    resultado = atual + anterior
    atual = anterior
    anterior = resultado
    if n < 0:
        n += 1
    elif n > 0:
        n -= 1
print('Acabou')    

formatos.saida(63)
