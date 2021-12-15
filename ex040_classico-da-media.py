import formatos


formatos.entrada(40)

nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
media = (nota1 + nota2) / 2
print(f'Tirando {nota1} e {nota2}, a média do aluno é {media:.1f}')
if media < 5:
    print('O aluno foi REPROVADO.')
elif 7 > media >= 5:
    print('O aluno está de RECUPERAÇÃO')
elif media >= 7:
    print('O aluno foi APROVADO')

formatos.saida(40)
