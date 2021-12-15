import formatos


def linha(tamanho=42) -> str:
    """
    -> Monta uma linha com um tamanho.
    :param tamanho: (opcional) Tamanho da linha.
    :return: Linha formada por '-'.
    """
    return '-' * tamanho


def cabecalho(texto: str, /,tamanho=42) -> str:
    """
    -> Print de cabecalho no terminal.
    :param texto: (obrigatório) Titulo do cabecalho.
    :param tamanho: (opcional) Tamanho do alinhamento geral.
    :return: Nao retorna valor.
    """
    print(f'{linha(tamanho)}\n{texto.center(tamanho)}\n{linha(tamanho)}')


def leiaInt(msg: str, /) -> int:
    """
    -> Ler a entrada de um numero inteiro.
    :param msg: (posicional) Mensagem exibida ao usuario.
    :return: Valor inteiro.
    """
    while True:
        try:
            return int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0


def menu(lista: list, /) -> int:
    """
    -> Print de menu de opcoes.
    :param lista: (obrigatorio) Lista com todas as opcoes do menu.
    :return: Numero inteiro da opção do menu.
    """
    cabecalho('MENU PRINCIPAL')
    for i, item in enumerate(lista, 1):
        formatos.amarelo()
        print(f'{i} - {item}')
        formatos.close()
    print(linha())
    op = leiaInt('\033[32m Sua Opção: \033[m')
    return op
