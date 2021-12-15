import moeda as md
import formatos


formatos.entrada(107)

valor = float(input('Informe um valor R$ '))
print(f'Aumentando 10%, temos {md.moeda(md.aumentar(valor))}')
print(f'Diminuindo 13%, temos{md.moeda(md.diminuir(valor, 13))}')
print(f'O dobro de {md.moeda(valor)} é {md.moeda(md.dobro(valor))}')
print(f'A metade de {md.moeda(valor)} é {md.moeda(md.metade(valor))}')

formatos.saida(107)