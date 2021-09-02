import formatos
formatos.entrada(34)
formatos.azul()
salario = float(input('Qual o seu salário atual? '))
if salario > 1250:
    aumento = 0.1 * salario
else:
    aumento = 0.15 * salario
formatos.amarelo()
print(salario + aumento)
formatos.saida(34)
