import formatos


formatos.entrada(35)

formatos.verde()
a = float(input('Digite o primeiro número: '))
b = float(input('Digite o segundo número: '))
c = float(input('Digite o terceiro número: '))
if a < b + c and b < a + c and c < a + b:
    formatos.azul()
    print(f'com essas retas {a}, {b} e {c} é possível ter um triângulo')
else:
    formatos.vermelho()
    print(f'Com essas retas {a}, {b} e {c} não é possível ter um triângulo.')
    
formatos.saida(35)
