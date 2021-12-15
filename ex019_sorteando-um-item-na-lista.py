from random import choice
import formatos


formatos.entrada(19)

alunos = []
for a in range(1, 5):
    alunos.append(str(input('{}° aluno: '.format(a))))
print('\nO aluno escolhido para apagar o quadro foi: {}.\n'.format(choice(alunos)))

formatos.saida(19)
