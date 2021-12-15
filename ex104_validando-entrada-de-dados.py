import formatos


def leiaInt(msg: str) -> int:
    """
    -> Validacao de entrada de valores numericos
    :param msg: Mensagem mostrada ao usuario na leitura do valor.
    :return: Valor numerico inteiro.
    """
    while True:
        entrada = input(msg)
        if entrada.isnumeric():
            return entrada
        formatos.vermelho()
        print(f'ERRO! Digite um número inteiro válido.')
        formatos.close()


formatos.entrada(104)

n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')

formatos.saida(104)
