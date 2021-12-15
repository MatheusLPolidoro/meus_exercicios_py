import os


def decompor(num):
    total = 0
    modulo = 1
    for index in str(num):
        algarismo = (int(num) // modulo % 10)
        modulo = modulo * 10
        total = total + algarismo
        print(algarismo)
    return total

sair = False
num = input('Informe um número qualquer: ')
while sair == False:
    total = decompor(num)
    num = total
    print(total)
    if total < 10:
        sair = True
os.system('pause')
