import formatos


formatos.entrada(43)

peso = float(input('Informe seu peso (kg): '))
altura = float(input('Informe sua altura (m): '))
imc = peso / (altura ** 2)
print(f'O IMC é de {imc:.1f}')
if imc < 18.5:
    print('Você esta ABAIXO DO PESO normal.')
elif imc <= 25:
    print('Você esta com o PESO IDEAL.')
elif imc <= 30:
    print('Você está com SOBREPESO.')
elif imc <= 40:
    print('Você está com OBSIDADE!')
elif imc > 40:
    print('Você esta com OBSIDADE MÓRBIDA, cuidado!')

formatos.saida(43)
