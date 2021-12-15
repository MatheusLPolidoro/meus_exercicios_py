import formatos


formatos.entrada(84)

pessoa = list()
dado = list()
total_maior = list()
total_menor = list()
maior = menor = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Peso: ')))
    if not maior + menor:
        maior = menor = dado[1]
    if dado[1] > maior:
        maior = dado[1]
    if dado[1] < menor:
        menor = dado[1]
    pessoa.append(dado.copy())
    dado.clear()
    while True:
        op = str(input('Quer continuar? [S/N]')).strip().upper()
        if op in 'SN':
            break
    if op == 'N':
        break
total_maior = ', '.join([p[0] for p in pessoa if p[1] == maior])
total_menor = ', '.join([p[0] for p in pessoa if p[1] == menor])
print(f'Ao todo você cadastrou {len(pessoa)} pessoas.')
print(f'O maior peso foi de {maior:.1f}Kg.Peso de {total_maior} ')
print(f'O menor peso foi de {menor:.1f}Kg.Peso de {total_menor} ')

formatos.saida(84)
