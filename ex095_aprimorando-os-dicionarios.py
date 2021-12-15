import formatos


formatos.entrada(95)

jogador = dict()
time = list()
cod = 0
while True:
    jogador['cod'] = cod
    jogador['nome'] = str(input('Nome do jogador: '))
    qtd_partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    gols = [int(input(f'Quantos gols na partida {p}? ')) for p in  range(0, qtd_partidas)]
    jogador['gols'] = gols
    jogador['total'] = sum(gols)
    cod += 1
    time.append(jogador.copy())
    while True:
        op = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if '' != op in 'SN':
            break
    if op == 'N':
        break
print('-=' * 40 + '\n' + ''.join([f'{k:<20}' for k in jogador.keys()]) + '\n' + '-' * 80)
print('\n'.join([''.join([f'{str(v):<20}' for v in jogador.values()]) for jogador in time]))
print('-' * 80)
while True:
    while True:
        cod_consulta = int(input('Mostrar dados de qual jogador? (999 para parar) '))
        if 0 <= cod_consulta < cod or cod_consulta == 999:
            break
        print(f'Não existe jogador com código {cod_consulta}!')
    if cod_consulta == 999:
        break
    print(f'LEVANTAMENTO DO JOGADOR {time[cod_consulta]["nome"]}:')
    for i, gols in enumerate(time[cod_consulta]['gols']):
        print(f'\t→ Na partida {i + 1 }, fez {gols} gols.')

formatos.saida(95)
