from random import shuffle
print('{:=^100}'.format(' DESAFIO 20 '))
alunos = []
for a in range(1, 5):
    alunos.append(str(input('Digite o nome do aluno: ')))
shuffle(alunos)
for a in range (0, 4):
    print('{}{:.<10}{:.>20}'.format(a + 1, '° aluno', alunos[a]))
print('{:=^100}'.format(' FIM DESAFIO 20 '))
