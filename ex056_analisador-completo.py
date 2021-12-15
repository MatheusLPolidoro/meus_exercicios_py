import formatos


formatos.entrada(56)

qtd_pessoas = 4
qtd_mulheres_menores = soma_idade = maior_idade = 0

for i in range(0, qtd_pessoas):
    print('-'*5 + f'{i + 1}ª PESSOA' + '-'*5)
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    soma_idade += idade
    if sexo[0] == 'M' and idade > maior_idade:
        mais_velho = nome
        maior_idade = idade
    elif sexo[0] == 'F' and idade < 20:
        qtd_mulheres_menores += 1

media = soma_idade / qtd_pessoas

print(f'A média de idade do grupo é {media:.1f}')
print(f'O homem mais velho é o {mais_velho} com {maior_idade} anos')
print(f'O número de mulheres abaixo de 20 anos é de {qtd_mulheres_menores}')

formatos.saida(56)
