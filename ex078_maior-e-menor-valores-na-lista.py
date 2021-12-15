import formatos


def plural(qtd: int) -> str:
    if qtd > 2:
        return 'ões'
    else:
        return 'ão'


formatos.entrada(78)

lista = [int(input(f'Informe um numero na {i}ª posição: ')) for i in range(0, 5)]
maior = " e ".join([str(i) + 'ª' for i, n in enumerate(lista) if n == max(lista)])
menor = " e ".join([str(i) + 'ª' for i, n in enumerate(lista) if n == min(lista)])
print(f'O maior valor é {max(lista)} na {maior} posiç{plural(len(maior))}')
print(f'O menor valor é {min(lista)} na {menor} posiç{plural(len(menor))}')

formatos.saida(78)
