import moeda
import formatos


formatos.entrada(107)

valor = float(input('Informe um valor R$ '))
print(f'Aumentando 10%, temos {moeda.aumentar(valor)}')
print(f'Diminuindo 13%, temos{moeda.diminuir(valor, 13)}')
print(f'O dobro de {valor} é {moeda.dobro(valor)}')
print(f'A metade de {valor} é {moeda.metade(valor)}')

formatos.saida(107)
