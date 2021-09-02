print('{:=^100}'.format(' DESAFIO 27 '))
name = str(input('\nDigite seu nome completo: ')).title().strip().split()
first_name = name[0] #atribui a variavel o primeiro ítem da lista
last_name = name[len(name) - 1]
print(f'\nPrimeiro nome: {first_name}\nÚltimo nome: {last_name}\n')
print('{:=^100}'.format(' FIM DESAFIO 27 '))
