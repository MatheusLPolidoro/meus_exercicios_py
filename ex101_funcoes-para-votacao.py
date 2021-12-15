import formatos
from datetime import date


def voto(ano_nasc: int) -> str:
    """
    -> Informa se a pessoa deve votar ou nao
    :param ano_nasc: Valor inteiro do ano de nascimento.
    """
    idade = date.today().year - ano_nasc
    msg = f'Com {idade} anos: '
    if 65 > idade > 17:
        msg += 'VOTO OBRIGATÓRIO.'
    elif idade >= 65:
        msg += 'VOTO OPCIONAL.'
    else:
        msg += 'NÃO VOTA.'
    return msg


formatos.entrada(101)

print(voto(int(input('Em que ano você nasceu? '))))

formatos.saida(101)
