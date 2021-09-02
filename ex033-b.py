import formatos
formatos.entrada('33-a')
formatos.amarelo()
listnum = list()
print('Iniciando comparação de maior menor, para enviar os dados para processamento coloque o valor zero.')
formatos.amarelo()
cont = 1
while True:
    n = int(input(f'Digite o {cont}° para comparação: '))
    if n != 0:
        listnum.append(n)
        cont += 1
    else:
        break
#localizar o menor
menor = listnum[0]
for ind, valor in enumerate(listnum):
        if valor < menor and valor != 0:
            menor = valor
#localizar o maior
maior = listnum[0]
for ind, valor in enumerate(listnum):
        if valor > menor:
            maior = valor
formatos.verde()
print(f'Entre os números digitados o maior é {maior} e o menor é {menor}.')
formatos.saida('33-a')
