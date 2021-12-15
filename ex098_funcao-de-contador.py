import formatos
from time import sleep


def contador(início: int, fim: int, /, passo=1) -> str:
    if not passo:
        passo = 1
    print('-=' * 30)
    if passo > 0:
        if início > fim:
            passo *= -1
    else:
        if início < fim:
            passo *= -1
    print(f'Contagem de {início} até {fim} de {passo} em {passo}')
    for i in range(início, fim + passo, passo):
        sleep(.3)
        print(i, end=' ', flush=True)
    print('FIM!')


formatos.entrada(98)

contador(1, 10)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
print('-=' * 30)
contador(int(input('Início: ')), int(
            input('Fim: ')), 
            passo=int(input('Passo: '))
        )

formatos.saida(98)
