from random import shuffle
import formatos


formatos.entrada(20)

alunos = []
for a in range(1, 5):
    alunos.append(str(input('Digite o nome do aluno: ')))
shuffle(alunos)
for a in range(0, 4):
    print('{}{:.<10}{:.>20}'.format(a + 1, '° aluno', alunos[a]))

formatos.saida(20)
