import formatos


formatos.entrada(83)

expressao = str(input('Digite sua expressão: '))
pilha = []
for letra in expressao:
    if '(' == letra:
        pilha.append(letra)
    elif ')' == letra:
        if len(pilha):
            pilha.pop()
        else:
            pilha.append(letra)
            break
if not len(pilha):
    print('Sua expressão está válida!')
else:
    print('Sua expressão esta errada!')
                
formatos.saida(83)
