import formatos


formatos.entrada(8)

dist = float(input('\nUma distância em metros: '))
print('\nA medida de {} m corresponde a\n\n{} km\n{} hm\n{} dam\n{} dm \n{} cm\n{} mm\n'.format(dist, dist / 1000, dist / 100, dist / 10, dist * 10, dist * 100, dist * 1000))

formatos.saida(8)
