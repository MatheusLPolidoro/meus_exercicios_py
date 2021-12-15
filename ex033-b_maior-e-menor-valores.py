import formatos


formatos.entrada('33-a')

formatos.amarelo()
listnum = list()
print('Iniciando comparação de maior menor, para enviar os dados para processamento coloque o valor zero.')
formatos.azul()
cont = 1
while True:
    n = int(input(f'Digite o {cont}° para comparação: '))
    if n:
        listnum.append(n)
        cont += 1
    else:
        break
menor = maior = listnum[0]
for valor in listnum:
        if valor < menor and valor != 0:
            menor = valor
        if valor > maior:
            maior = valor
formatos.verde()
print(f'Entre os números digitados o MAIOR é {maior} e o MENOR é {menor}.')

formatos.saida('33-a')
