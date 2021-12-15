import formatos


def ficha(nome='<desconhecido>', gols=0):
    """
    -> Mostra a ficha do jogador.
    :param nome: (opcional) O nome do jogador.
    :param gols: (opcional) O numero de gols do jogador.
    """
    if not len(nome.strip()):
        nome = '<desconhecido>'
    if not len(str(gols).strip()) or not str(gols).isnumeric():
        gols = 0
    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'


formatos.entrada(103)

nome = str(input('Nome do jogador: '))
gols = str(input('Número de Gols: '))
print(ficha(nome, gols))
 
formatos.saida(103)
