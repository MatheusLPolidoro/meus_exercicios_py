import formatos


def escreva(texto: str, separador='~', tamanho=0) -> str:
    ''' Por padrão cria um título com o caracter ~, mas você pode passar qual é p separador e o tamanho do título'''
    if not tamanho:
        tamanho = len(texto) + 4
    print(separador*tamanho + f'\n{texto:^{tamanho}}\n' + separador*tamanho)


formatos.entrada(97)

escreva('Matheus Polidoro', '▬', 50)
escreva('Curso de Python no YouTube')
escreva('Dev')

formatos.saida(97)
