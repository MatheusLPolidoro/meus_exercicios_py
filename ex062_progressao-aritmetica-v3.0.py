import formatos 


formatos.entrada(61)

termo = int(input('Primeiro termo da progressão aritimética: '))
razao = int(input('Razão da progressão: '))
qtd_termos = 10


while qtd_termos:
    print(f'{termo} ', end=' → ')
    termo = termo + razao
    qtd_termos -= 1
    if not qtd_termos:
        qtd_termos = int(input('Deseja ver mais quantos termos? '))
print('Acabou')

formatos.saida(61)
