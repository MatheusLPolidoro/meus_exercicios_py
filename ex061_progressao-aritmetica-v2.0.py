import formatos 


formatos.entrada(61)

termo = int(input('Primeiro termo da progressão aritimética: '))
razao = int(input('Razão da progressão: '))
qtd_termos = 10


while qtd_termos:
    print(f'{termo} ', end=' → ')
    termo = termo + razao
    qtd_termos -= 1
print('Acabou')

formatos.saida(61)
