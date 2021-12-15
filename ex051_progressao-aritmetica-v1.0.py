import formatos


formatos.entrada(51)

primeiro_termo = int(input('Primeiro termo da progressão aritimética: '))
razao = int(input('Razão da progressão: '))

for i in range(0, razao * 10, razao):
    print(f'{i + primeiro_termo}', end=' → ')
print('Acabou')

formatos.saida(51)
