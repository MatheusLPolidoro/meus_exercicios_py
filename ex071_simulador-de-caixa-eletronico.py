from datetime import datetime
import formatos


formatos.entrada(71)
formatos.titulo('SIMULADOR DE CAIXA ELETRÔNICO')

hora = datetime.today().hour
periodo = 'bom dia' if hora < 12 else 'boa tarde' if hora < 18 else 'boa noite'
saque = int(input(f'Olá, {periodo}!\nQue valor você quer sacar? '))
caixa = saque
i = cedulas = 0
valor = (100, 50, 20, 10, 5, 1)
while caixa:
    while caixa >= valor[i]:
        caixa -= valor[i]
        cedulas += 1
    if cedulas > 0:
        print(f'Total de {cedulas:>2} cédulas de R${valor[i]:>2}')
    cedulas = 0
    i += 1
print(f'{"="*30}\nVolte sempre! {periodo.capitalize()}!')
formatos.saida(71)
