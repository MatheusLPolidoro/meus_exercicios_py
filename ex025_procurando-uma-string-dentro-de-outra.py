import formatos


formatos.entrada(25)

name = str(input('\nDigite seu nome completo: ')).strip().upper()
print('\nVocê possui Silva no nome [True / False] >>> {}\n'.format('SILVA' in name))

formatos.saida(25)
