def aumentar(valor:float, /, porcentagem=10, formatar=False):
    """
    -> Calcula um aumento no valor recebido.
    :param valor: (posicional) Valor original.
    :param porcentagem: (opcional) Porcentagem do aumento.
    :param formatar: (opcional) Se o retorno deve ser formatado como moeda ou nao.
    :return: Valor com aumento definido ou 10%.
    """
    if porcentagem > 0:
        valor += valor * (porcentagem / 100)
        if formatar:
            valor = moeda(valor)
    return valor


def diminuir(valor:float, /, porcentagem=10, formatar=False):
    """
    -> Calcula um desconto no valor recebido.
    :param valor: (posicional) Valor original.
    :param porcentagem: (opcional) Porcentagem do desconto.
    :param formatar: (opcional) Se o retorno deve ser formatado como moeda ou nao.
    :return: Valor com desconto definido ou 10%.
    """
    if porcentagem > 0:
        valor -= valor * (porcentagem / 100)
        if formatar:
            valor = moeda(valor)
    return valor


def dobro(valor:float, /, formatar=False):
    """
    -> Calcula o dobro do valor recebido.
    :param valor: (posicional) Valor original.
    :param formatar: (opcional) Se o retorno deve ser formatado como moeda ou nao.
    :return: Valor dobrado.
    """
    valor *= 2
    if formatar:
        valor = moeda(valor)
    return valor


def metade(valor:float, /, formatar=False):
    """
    -> Calcula a metade do valor recebido.
    :param valor: (posicional) Valor original.
    :param formatar: (opcional) Se o retorno deve ser formatado como moeda ou nao.
    :return: Valor pela metade.
    """
    valor /= 2
    if formatar:
        valor = moeda(valor)
    return valor


def moeda(valor: float, /) -> str:
    """
    -> Formata o numero recebido em um texto
    :param valor: (posicional) Valor original.
    :return: Texto formatado em moeda R$.
    """
    valor = f'{valor:.2f}'
    return f'R${str(valor).replace(".", ","):}'


def resumo(valor: float, juros: float, desconto: float, /) -> str:
    """
    -> Demonstra um resumo das demais funcoes do modulo em formato de tabela.
    :param valor: (posicional) Valor original.
    :param juros: (posicional) Porcentagem do juros.
    :param desconto: (posicional) Porcentagem do desconto.
    :return: Texto com resumo formatado do valor.
    """
    tab = 25
    print(f'{"-"*40}\n{"RESUMO DO VALOR":^40}\n{"-"*40}')
    print(f'{"Preço analisado":{tab}}:  {moeda(valor)}')
    print(f'{"Dobro do preço":{tab}}:  {dobro(valor, True)}')
    print(f'{"Metade do preço":{tab}}:  {metade(valor,True)}')
    print(f'{f"{juros}% de aumento":{tab}}:  {aumentar(valor, juros, True)}')
    print(f'{f"{desconto}% de desconto":{tab}}:  {diminuir(valor, desconto, True)}')
    print('-'*40)