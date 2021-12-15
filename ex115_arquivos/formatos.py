import os


def azul():
    """
    Cor azul para font no terminal
        => Modifica a cor para azul, cod (\\033[36m)
    """
    print('\033[36m', end='')


def amarelo():
    """
    Cor amarelo para font no terminal
        => Modifica a cor para amarelo, cod (\\033[33m)
    """
    print('\033[33m', end='')


def vermelho():
    """
    Cor vermelho para font no terminal
        => Modifica a cor para vermelho, cod (\\033[31m)
    """
    print('\033[31m', end='')


def verde():
    """
    Cor verde para font no terminal
        => Modifica a cor para verde, cod (\\033[32m)
    """
    print('\033[32m', end='')


def close():
    """
    fecha o estilo de font no terminal
        => cod (\\033[m)
    """
    print('\033[m', end='')


def entrada(x):
    """
    Entrada do desafio
        => Formatar uma mensagem de inicio dos desafios
    """
    os.system('cls')
    print('\033[36m{:▬^50}'.format(' DESAFIO ' + str(x) + ' '))
    print('\033[m')


def saida(y):
    """
    Saida do desafio
        => Formatar uma mensagem de saida dos desafios
    """
    print('\n\033[36m{:▬^50}'.format(' FIM DESAFIO ' + str(y) + ' '))
    print('\033[m')
    os.system('pause')
    os.system('cls')


def titulo(texto: str, separador='▬', tamanho=0) -> str:
    """
    Titulo personalizado
        -> Apresentar um titulo para uma tabela, formulario ou sistema (CLI)
        :param texto: Mensagem que o titulo contem.
        :param separador: (opcional) Separador do titulo.
        :param tamanho: (opcional) Tamanho do titulo.
        :param cor: (opcional) Cor do titulo
        :return: Nao retorna valores
    """
    if not tamanho:
        tamanho = len(texto) + 4
    print(separador*tamanho + f'\n{texto:^{tamanho}}\n' + separador*tamanho)
