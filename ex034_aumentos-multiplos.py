import formatos


formatos.entrada(34)

formatos.azul()
salario = float(input('Qual o seu salário atual? '))
formatos.amarelo()
if salario > 1250:
    aumento = 0.1 * salario
    print(F'Seu salário de R${salario} com aumento de 10% ficou R${salario + aumento}')
else:
    aumento = 0.15 * salario
    print(F'Seu salário de R${salario} com aumento de 15% ficou R${salario + aumento}')

formatos.saida(34)
