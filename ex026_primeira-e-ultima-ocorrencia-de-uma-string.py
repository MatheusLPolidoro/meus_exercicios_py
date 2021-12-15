import formatos


formatos.entrada(26)

frase = str(input('\nDigite qualquer frase: ')).strip().upper()
qtd_a = frase.count('A')
first_a = frase.find('A')
last_a = len(frase) - 1 - frase[::-1].find('A')
print(f'\nQuantidade de "A" no texto: {qtd_a}\nPosição do primeiro "A": {first_a + 1}\nPosição do último "A": {last_a + 1}\n')

formatos.saida(26)
