import formatos


formatos.entrada(89)

lista = list()
while True:
    aluno = [str(input('Nome: ')), [float(input(f'Nota {i}: ')) for i in range(1, 3)]]
    aluno.append(sum(aluno[1]) / len(aluno[1]))
    lista.append(aluno.copy())
    aluno.clear()
    while True:
        op = str(input('Quer continuar? [S/N] ')).strip().upper()
        if '' != op in 'SN':
            break
    if op == 'N':
        break
print('-='*15 + '\nN°.\tNOME\t\tMÉDIA\n' + '-'*30)
for i, aluno in enumerate(lista):
    print(f'{i}\t{aluno[0]}\t\t{aluno[2]:.1f}')
print('-'*30)
while True:
    indice = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if indice == 999:
        break
    if 0 <= indice < len(lista):
        print(f'Notas de {lista[indice][0]} são {lista[indice][1]}')
    else:
        print(f'Não tem aluno na posição {indice}ª')

formatos.saida(89)
