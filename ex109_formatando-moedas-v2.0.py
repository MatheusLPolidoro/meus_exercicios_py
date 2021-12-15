import moeda as md
import formatos


formatos.entrada(107)

valor = float(input('Informe um valor R$ '))
print(f'Aumentando 10%, temos {md.aumentar(valor, 10, True)}')
print(f'Diminuindo 13%, temos{md.diminuir(valor, 13, True)}')
print(f'O dobro de {md.moeda(valor)} é {md.dobro(valor, True)}')
print(f'A metade de {md.moeda(valor)} é {md.metade(valor, True)}')

formatos.saida(107)
