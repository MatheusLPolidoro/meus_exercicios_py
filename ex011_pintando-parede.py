import formatos


formatos.entrada(11)

largura_parede = float(input('\nLargura da parede: '))
altura_parede = float(input('Altura da parede: '))
print('\nSua parede tem a dimensão de {} X {}.\nSua área é de {}m².\nPara pintar essa parede, você precisará de {} litros de tinta.\n'.format(largura_parede, altura_parede, largura_parede * altura_parede, (largura_parede * altura_parede) / 2))

formatos.saida(11)
