import formatos
from random import randint
from time import sleep


formatos.entrada(88)
formatos.titulo('JOGA DA MEGA SENA', '-', 50)

sorteios = list()
jogo = list()
qtd_jogos = int(input('Quantos jogos você quer sortear? '))
print('-='*8, f'SORTEANDO {qtd_jogos} JOGOS', '-='*8)
for i in range(0, qtd_jogos):
    while True:
        num = randint(1, 60)
        if not num in jogo:
            jogo.append(num)
        if len(jogo) == 6:
            break
    sorteios.append(sorted(jogo[:]))
    print(f'Jogo {i + 1}: {" ► ".join(map(str, (sorteios[i])))}')
    sleep(1)
    jogo.clear()
print('-='*9, f'◄ BOA SORTE ►', '-='*9)

formatos.saida(88)
