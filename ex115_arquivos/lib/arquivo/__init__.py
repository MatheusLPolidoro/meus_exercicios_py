from lib.interface import *


def arquivoExiste(nome: str, /) -> bool:
    """
    -> Valida se um arquivo existe.
    :param nome: (obrigatorio) Nome completo do aquivo.
    :return: Verdadeiro ou falso para a existencia do arquivo.
    """
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome: str, /) -> bool:
    """
    -> Cria um arquivo.
    :param nome: (obrigatorio) Nome completo do arquivo.
    :return: Não retorna valores.
    """
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucessso!')


def lerArquivo(nome: str, /):
    """
    -> Ler um arquivo.
    :param nome: (obrigatorio) Nome completo do arquivo.
    :return: Não retorna valores.
    """
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]} anos')
    finally:
        a.close


def cadastrar(nome, /, nomepessoa='desconhecido', idade=0):
    """
    -> Cadastrar uma nova pessoa no arquivo.
    :param nome: (obrigatorio) Nome completo do arquivo.
    :param nomepessoa: (opcional) Nome da pessoa.
    :param idade: (opcional) Idade da pessoa.
    :return: Não retorna valor.
    """
    try:
        a = open(nome, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nomepessoa};{idade}\n')
        except:
            print('Houve um ERRO na abertura do arquivo!')
        else:
            print(f'Novo registro de {nomepessoa} adicionado.')
            a.close()
