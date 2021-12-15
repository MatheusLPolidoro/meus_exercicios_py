import formatos


formatos.entrada(94)

pessoa = dict()
lista = list()
total = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: ')).strip().upper()[0]
        if '' != pessoa['sexo'] in 'MF':
            break
    pessoa['idade'] = int(input('Idade: '))
    total += pessoa['idade']
    lista.append(pessoa.copy())
    while True:
        op = str(input('Quer continuar? [S/N]')).strip().upper()
        if '' != op in 'SN':
            break
    if op == 'N':
        break 
print('-=' * 30)
mulheres = ', '.join([item['nome'] for item in lista if item['sexo'] in 'F'])
acima = ('\n\t\t'.join(['; '.join([f'{k} = {v}' for k, v in item.items()]) for item in lista if item['idade'] > total / len(lista)]))
print(f'\t - O grupo tem {len(lista)} pessoas.')
print(f'\t - A média de idade é de {total / len(lista):5.2f} anos.')
print(f'\t - As mulheres cadastradas são: {mulheres}')
print(f'\t - As pessoas que possuem idade acima da média são:\n\t\t{acima}')

formatos.saida(94)
