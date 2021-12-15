import formatos


formatos.entrada(73)

tabela_brasileirao = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense', 'América-MG', 'Atlético-GO', 'Santos', 'Ceará SC', 'Internacional', 'São Paulo' , 'Athletico-PR', 'Cuiabá', 'Juventude', 'Grêmio' , 'Bahia', 'Sport Recife', 'Chapecoense')

print(f'Lista de times do Brasileirão: {" ► ".join(tabela_brasileirao)}')
print(f'Os 5 primeiros são: {" ► ".join(tabela_brasileirao[:5])}')
print(f'Os 4 últimos são: {" ► ".join(tabela_brasileirao[-4:])}')
print(f'Times em ordem alfabética: {" ► ".join(sorted(tabela_brasileirao))}')
print(f'O Chapecoense está na {tabela_brasileirao.index("Chapecoense") + 1}ª posição')

formatos.saida(73)
