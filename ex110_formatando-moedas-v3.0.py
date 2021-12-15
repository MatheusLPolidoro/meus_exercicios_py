import moeda
import formatos


formatos.entrada(110)

valor = float(input('Digite um preço: R$'))
moeda.resumo(valor, 80, 35)

formatos.saida(110)