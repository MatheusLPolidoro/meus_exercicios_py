import formatos


formatos.entrada(93)

dados = dict()
dados['nome'] = str(input('Nome do jogador: '))
qtd_partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
gols = [int(input(f'Quantos gols na partida {p}? ')) for p in  range(1, qtd_partidas + 1)]
dados['gols'] = gols
dados['total'] = sum(gols)
print('-=' * 30)
print(dados)
print('-=' * 30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {dados["nome"]} jogou {qtd_partidas} partidas.')
for i, gols in enumerate(gols):
    print(f'\t→ Na partida {i + 1}, fez {gols} gols.')
print(f'Foi um total de {dados["total"]} gols.')

formatos.saida(93)
