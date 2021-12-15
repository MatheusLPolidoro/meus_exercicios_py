import formatos
from time import sleep


cores = (
    '\033[m',         # sem cor
    '\033[0;30;41m',  # vermelho
    '\033[0;30;42m',  # verde
    '\033[0;30;43m',  # amarelo
    '\033[0;30;44m',  # azul
    '\033[0;30;45m',  # roxo
)


def titulo(texto: str, separador='▬', tamanho=0, cor=0) -> str:
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
    sleep(.5)
    print(cores[cor], flush=True)
    print(separador*tamanho + f'\n{texto:^{tamanho}}\n' + separador*tamanho)
    print(cores[0], flush=True)


def pyHelp():
    while True:
        titulo('SISTEMA DE AJUDA PyHELP', tamanho=50, cor=2)
        op = str(input('Função ou Biblioteca > '))
        if op.upper() == 'FIM':
            titulo('ATÉ LOGO!', tamanho=50, cor=1)
            break
        titulo(f'Acessando o manual do comando \'{op}\'', tamanho=50, cor=4)
        help(op)
        sleep(1)


formatos.entrada(106)

pyHelp()

formatos.saida(106)
