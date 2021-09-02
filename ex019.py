from random import choice
print('{:=^100}'.format(' DESAFIO 19 '))
alunos = []
for a in range(1, 5):
    alunos.append(str(input('{}° aluno: '.format(a))))
print('\nO aluno escolhido para apagar o quadro foi: {}.\n'.format(choice(alunos)))
print('{:=^100}'.format(' FIM DESAFIO 19 '))
