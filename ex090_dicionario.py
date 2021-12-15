import formatos


formatos.entrada(90)

aluno = dict()
aluno['nome'] = str(input('Nome:'))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situação'] = 'APROVADO'
elif aluno['media'] < 7:
    aluno['situação'] = 'RECUPERAÇÃO'
else:
    aluno['situação'] = 'REPROVADO'
print('-' * 40)
for k, v in aluno.items():
    print(f'\t- {k} é igual a {v}')

formatos.saida(90)
