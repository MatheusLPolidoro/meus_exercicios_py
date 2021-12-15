from random import randint
import formatos


formatos.entrada(58)

tentativa = 0
num_random = randint(0, 10)
num_jogador = -1
print('Vou processar um número de 0 a 5, advinhe o ', end='')
while num_random != num_jogador:
    num_jogador = int(input('número: '))
    tentativa += 1
    if num_random != num_jogador:
        print('ERROU.Tente novamente um ', end='')
print(f'ACERTOU, o número sorteado foi {num_random}\nVocê fez {tentativa} tentativas.')

formatos.saida(58)
