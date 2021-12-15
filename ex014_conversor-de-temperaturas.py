import formatos


formatos.entrada(14)

cel = float(input('\nInforme a temperatura em °C: '))
print('A temperatura de {}°C corresponde a {}°F\n'.format(cel, 9 * cel / 5 + 32))

formatos.saida(14)
