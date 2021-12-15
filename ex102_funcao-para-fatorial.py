import formatos


def fatorial(num=0, show=False):
    """
    -> Calcula o fatorial de um numero.
    :param num: O numero a ser calculado.
    :param show: (opcional) Mostrar ou nao a conta.
    :return: O valor do fatorial de um numero num.
    """
    f = 1
    seq = [i for i in range(num, 0, -1)]
    for n in seq:
        f *= n
    if show == True:
        return f'{num}! = {" X ".join(map(str, seq))} = {f}'
    else:
        return f


formatos.entrada(102)

num = int(input('Digite um valor: '))
print(fatorial(num, show=True))

formatos.saida(102)
