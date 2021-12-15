import formatos


formatos.entrada(7)

pn = float(input('\nPrimeira nota do aluno: '))
sn = float(input('Seguda nota do aluno: '))
print('\nA média entre {} e {} é igual a {:.1f}\n'.format(pn, sn, (pn + sn) / 2))

formatos.saida(7)
