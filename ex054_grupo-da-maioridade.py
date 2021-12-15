from datetime import date
import formatos


formatos.entrada(54)

qtd_maior_idade = 0
qtd_pessoas = 7

for i in range(0, qtd_pessoas):
    idade = date.today().year - int(input(f'Em que ano {i + 1}ª nasceu?  '))
    if idade >= 21:
        qtd_maior_idade += 1

print(f'Das {qtd_pessoas} pessoas {qtd_maior_idade} são maiores de idade.')
print(f'Das {qtd_pessoas} pessoas {7 - qtd_maior_idade} são menores de idade.')

formatos.saida(54)
