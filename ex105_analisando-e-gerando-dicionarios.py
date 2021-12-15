import formatos


def notas(*n: float, sit=False) -> dict:
    """
    -> Analisa notas e situacoes de varios alunos.
    :param n: Aceita uma ou mais notas dos alunos.
    :param sit: (opcional) Indica se deve ou nao adicionar a situacao
    :return: Dicionario com informacoes sobre a situacao da turma.
    """
    turma = dict()
    turma['total'] = sum(n)
    turma['maior'] = max(n)
    turma['menor'] = min(n)
    turma['media'] = sum(n) / len(n)
    if sit:
        if turma['media'] > 7:
            turma['situação'] = 'BOA'
        elif turma['media'] > 5:
            turma['situação'] = 'RAZOÁVEL'
        else:
            turma['situação'] = 'RUIM'
    return turma


formatos.entrada(105)

resp = notas(3.5, 2, 6.5, 2, 7, 4)
print(resp)

formatos.saida(105)
