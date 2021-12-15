import formatos


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


def leiaFloat(msg: str, /) -> float:
    """
    -> Ler a entrada de um numero float.
    :param msg: (posicional) Mensagem exibida ao usuario.
    :return: Valor float.
    """
    while True:
        try:
            return float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número float válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0


formatos.entrada(113)

numInt = leiaInt('Informe um número inteiro: ')
numFloat = leiaFloat('Informe um número float: ')
print(f'O número inteiro digitado foi {numInt} e o número float digitado foi {numFloat}')

formatos.saida(113)
