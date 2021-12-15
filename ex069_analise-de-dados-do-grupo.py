import formatos


formatos.entrada(69)
formatos.azul()
formatos.titulo('SISTEMA DE CADASTRO')
formatos.amarelo()

maior_idade = homens = mulheres_menos_20 = 0

while True:
    print('-'*35 + f'\n{"CADASTRE UMA PESSOA":^35}\n' + '-'*35)
    idade = int(input('Idade: '))
    while True:
        sexo = str(input('Sexo: [M/F] ')).strip().upper()
        if sexo in 'FM':
            break
    if idade > 18:
        maior_idade += 1
    if sexo[0] == 'M':
        homens += 1
    if sexo[0] == 'F':
        mulheres_menos_20 += 1
    while True:
        op = str(input('Quer continuar? [S/N]')).strip().upper()
        if op in 'SN':
            break
    if op[0] == 'N':
        break
formatos.azul()
print(f'{"FIM DO PROGRAMA":=^35}')
formatos.verde()
print(f'Total de pessoas com mais de 18 anos: {maior_idade}')
print(f'Ao todo temos {homens} homens cadastrados')
mulher = 'mulheres' if mulheres_menos_20 != 1 else 'mulher'
print(f'E temos {mulheres_menos_20} {mulher} com menos de 20 anos.')

formatos.saida(69)
