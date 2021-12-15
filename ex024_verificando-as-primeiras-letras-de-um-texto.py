import formatos


formatos.entrada(24)

cidade = str(input('\nQual é o nome da sua cidade? ')).strip().upper()
print('O nome da sua cidade começa com Santo [True / False] >>> {}\n '.format(cidade[:5] == 'SANTO'))

formatos.saida(24)
