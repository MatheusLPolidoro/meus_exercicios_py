print('{:=^100}'.format(' DESAFIO 4 '))
key = input('\nDigite qualquer coisa no teclado!\n')
print('\nO tipo primitivo desse valor é {}\nSó tem espaços? {}\nÉ alfabético? {}\nÉ alfanumérico? {}\nEstá em maiúsculas? {}\nEstá em minúsculas? {}\nEstá capitalizada? {}\n'.format(type(key), key.isspace(), key.isalpha(), key.isalnum(), key.isupper(), key.islower(), key.istitle()))
print('{:=^100}'.format(' FIM DESAFIO 4 '))