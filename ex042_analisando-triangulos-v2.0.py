import formatos


formatos.entrada(42)

reta1 = float(input('Informe um valor para uma reta: '))
reta2 = float(input('Informe um outro valor para uma reta: '))
reta3 = float(input('Informe um mais um valor para uma reta: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print(f'Com essas retas {reta1}, {reta2} e {reta3} é possível ter um triângulo ', end='')
    if reta1 == reta2 == reta3:
        print('EQUILÁTERO.')
    elif reta1 == reta2 or reta2 == reta3:
        print('ESCALENO.')
    elif reta1 != reta2 != reta3:
        print('ISÓSCELES.')
else:
    print(f'Com essas retas {reta1}, {reta2} e {reta3} não é possível ter um triângulo.')

formatos.saida(42)