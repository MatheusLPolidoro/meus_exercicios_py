import formatos


formatos.entrada(77)

palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for item in palavras:
    print(f'\nNa palavra {item.upper()} temos ', end='')
    for letra in item:
        if letra.upper() in 'AEIOU':
            print(letra, end=' ')

formatos.saida(77)
