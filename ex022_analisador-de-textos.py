import formatos


formatos.entrada(22)

name = str(input('\nDigite seu nome completo: ')).strip() #recebe o nome completo
name_mai = name.upper()     #deixar a caidea de caracteres em maiuscolas
name_min = name.lower()     #deixar a caidea de caracteres em minusculas
name_count = len(name) - name.count(' ')  #tamamnho da cadeia - quantidade de epaços
name_first = name.find(' ')            #localiza o índice da string passada como parametro
name_last = len(name) - 1 - name.rfind(' ')   #localiza o índice da string passada como parametro
name_mid = name_count - (name_first + name_last) #para localizar os nome do meio
print(f"""\nO nome com todas as letras maiúsculas: {name_mai}
O nome com todas as letras minúsculas: {name_min}
O nome possui ao todo {name_count} letras.
O primeiro nome tem {name_first} letras.
O(s) nome(s) do meio tem {name_mid} letras.
O último nome tem {name_last} letras.\n""")

formatos.saida(22)
