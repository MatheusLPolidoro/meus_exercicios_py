import formatos


def área(largura: float, altura: float) -> float:
    return largura * altura


formatos.entrada(96)

print('Controle de Terrenos\n' + '-' * 30)
largura = float(input('LARGURA (m): '))
altura = float(input('ALTURA (m): '))

print(f'A área de um terreno {largura:.1f}x{altura:.1f} é de {área(largura, altura):.1f}m².')

formatos.saida(96)
