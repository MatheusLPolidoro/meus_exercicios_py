from utilidadesCeV import dado, moeda
import formatos


formatos.entrada(112)

valor = dado.leiaDinheiro('Informe um valor: ')
moeda.resumo(valor, 35, 22)

formatos.saida(112)
