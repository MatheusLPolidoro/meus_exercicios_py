import formatos


formatos.entrada('33-a')

formatos.amarelo()
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))
# localizar o menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
# localizar o maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f'Entre os números digitados o maior é {maior} e o menor é {menor}.')
formatos.verde()

formatos.saida('33-a')
