from time import sleep
import formatos


def maior(*valor: int):
    print('-=' * 30)
    maior = 0
    print('Analisando os valores passado...')
    for i in valor:
        sleep(.5)
        print(i, end=' ', flush=True)
        if i > maior:
            maior = i
    print(f'Foram informados {len(valor)} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


formatos.entrada(99)

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

formatos.saida(99)
