import os


def EntradaNum(msg):
    # Receber um número do usuário
    while True:
        dig = input(msg)
        try:
            dig = int(dig)
            break
        except ValueError:
            print('O valor "' + dig + '" é invalido!! ', end="", flush=True)
    return dig

def decomposicao(num):
    total = 0
    for i in range (0, len(num)):
        print(num[-i-1])
        total = total + int(num[i])
    return total

num = str(EntradaNum('Informe um número qualquer: '))
sair = False

while sair == False:
    total = decomposicao(num)
    print(total)
    num = str(total)
    if total <= 10:
        sair = True
os.system('pause')
