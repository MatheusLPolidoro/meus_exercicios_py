import re
import formatos

def leiaDinheiro(msg: str) -> float:
    """
    -> Validar entrada monetaria
    :param msg: (opcional) Mensagem que sera exibida para o usuario
    :return: Valor float
    """
    while True:
        entrada = str(input(msg)).strip()
        pattern = {'pInt': r'^\d+$',
                   'pNacional': r'^\d+,\d+$|^\d{1,3}(\.\d{3})*,\d+$|^\d{1,3}(\.\d{3})*$',
                   'pInternacional': r'^\d+\.\d+$|^\d{1,3}(,\d{3})*\.\d+$|^\d{1,3}(,\d{3})*$',
                   }
        for k, v in pattern.items():
            match = re.search(v, entrada)
            if match:
                if k == 'pNacional':
                    entrada = entrada.replace('.', '')
                    entrada = entrada.replace(',', '.')
                elif k == 'pInternacional':
                    entrada = entrada.replace(',', '')
                return float(entrada)
        formatos.vermelho()
        print(f'Erro: "{entrada}" é um preço inválido!')
        formatos.close()


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
