from utilidadesCeV import moeda
import formatos


formatos.entrada(110)

valor = float(input('Digite um preço: R$'))
moeda.resumo(valor, 35, 22)

formatos.saida(110)