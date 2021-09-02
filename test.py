import sys
import msvcrt
import formatos
formatos.entrada('TESTE')
palavra = ''
formatos.azul()
print('rodando.....')
formatos.verde()
while True:
    x = msvcrt.getch()
    if ord(x) == 13:
        break
    elif ord(x) == 8:
        sys.stdout.write('\b\b')
        sys.stdout.write(' \b')
        palavra = palavra[:len(palavra) - 1]
    elif ord(x) == 32:
        sys.stdout.write('  ')
        palavra += str(x)[2]
    else:
        sys.stdout.write('_ ')
        palavra += str(x)[2]
print('\n' + palavra)
formatos.saida('TESTE')