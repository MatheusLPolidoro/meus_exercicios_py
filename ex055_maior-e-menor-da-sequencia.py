import formatos


formatos.entrada(55)

maior = menor = 0

for i in range(0, 5):
    peso_atual = float(input(f'Informe o {i + 1}ª peso: '))
    if i == 0:
        menor = maior = peso_atual
    if peso_atual > maior:
        maior = peso_atual
    if peso_atual < menor:
        menor = peso_atual

print(f'O MAIOR peso lido foi de {maior:.1}kg\nO MENOR peso lido foi de {menor:.1f}kg')

formatos.saida(55)
