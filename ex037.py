import formatos
formatos.entrada(37)
formatos.amarelo()
n = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para a conversão:\n[ 1 ] converter para BINÁRIO\n[ 2 ] converter para OCTAL\n[ 3 ] converter para HEXADECIMAL')
formatos.verde()
escolha = int(input('Sua opção: '))
while True:
 if escolha == 1:
  r = bin(n)
  break
 elif escolha == 2:
  r = oct(n)
  break
 elif escolha == 3:
  r = hex(n)
  break
 else:
  formatos.vermelho()
  print('Opção invalida!')
  formatos.verde()
  escolha = int(input('Nova opção: '))
formatos.azul()
print(f'{n} Convertido para BINÁRIO é igual a {r[2:]}')
input()
formatos.saida(37)