import formatos
from random import randint
from time import sleep
from operator import itemgetter


formatos.entrada(91)

jogadores = dict()
for i in range(1, 5):
    jogadores[f'jogador{i}'] = randint(1, 6)
for k, v in jogadores.items():
    sleep(.5)    
    print(f'O {k} tirou {v}')
i = 1
formatos.titulo('RANKING DOS JOGADORES', '-=', 15)
for k, v in sorted(jogadores.items(), key=itemgetter(1), reverse=True):
    print(f'{i}ª lugar:{k} com {v}')
    i += 1

formatos.saida(91)
